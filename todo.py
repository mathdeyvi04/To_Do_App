# Vamos criar o Sanha aqui
from tkinter import *
import pandas
import os
from tkinter import ttk


def criar():
    janela = Tk()
    janela.title("To-Do")
    janela.geometry("400x550+1000+100")
    janela.resizable(False, False)
    janela.config(bg='#dde')

    # Vamos colocar o icone
    icone = PhotoImage(file='Figuras/task.png')
    janela.iconphoto(False, icone)

    # Observe como colocar um bg só para não ficar tão feio.
    # Vamos colocar a barra superior que abre um Sanha mais bonito
    superior = PhotoImage(file='Figuras/topbar.png')
    Label(janela, image=superior, bg='#dde').pack()

    # Vamos colocar o icone de menu lateral
    menu_lateral = PhotoImage(file='Figuras/dock.png')
    Label(janela, image=menu_lateral, bg='#32405b').place(x=30, y=25)

    note = PhotoImage(file='Figuras/task.png')
    Label(janela, image=note, bg='#32405b').place(x=340, y=25)

    Titulo = Label(janela, text='SANHAS', bg='#32405b', font='arial 20 bold', fg='white')
    Titulo.place(x=130, y=20)

    # Vamos agora colocar o Sanha para ser disponível para o usuário colocar o que deseja.
    tamanho_letra = 12

    frame = Frame(janela, width=400, height=30, bg='white')
    frame.place(x=0, y=180)

    # A entrada para colocarmos o texto
    tarefa_a_ser_adicionada = Entry(frame, font=f'arial {tamanho_letra}', bd=0)
    tarefa_a_ser_adicionada.place(x=10, y=7, width=300)
    tarefa_a_ser_adicionada.focus()
    tarefa_a_ser_adicionada.focus_set()

    Label(frame, text='Press. Enter', font=f'arial {tamanho_letra} bold', bd=0, bg='white').place(x=305, y=0, height=30)

    # Vamos implementar 2 sanhas agora, o de adicionar as tarefas

    def mostrar_tarefas():
        # Vamos ler o Sanha e colocá-lo a mostra

        tv = ttk.Treeview(janela, columns=[''], show='headings')

        tv.column('', minwidth=0, width=300)
        tv.heading('', text='')

        estilo = ttk.Style()
        estilo.configure("Treeview", font=("Helvetica", 12))
        estilo.map("Treeview", background=[("selected", 'white')], foreground=[('selected', 'black')])

        tv.place(x=0, y=230, width=400, height=250)

        p = open('tarefas.txt', 'r')
        linhas = [linha.replace('\n', '') for linha in p.readlines()]
        p.close()

        for linha in linhas:
            tv.insert('', 'end', values=[linha])

        return tv

    tree = mostrar_tarefas()

    # Devemos permitir eliminar uma tarefa
    def apagando_tarefa(eve):
        try:
            tarefa_a_ser_apagada = tree.focus()
            tarefa_de_fato = tree.item(tarefa_a_ser_apagada)['values'][0]

            # Apagando do treeview
            tree.delete(tarefa_a_ser_apagada)

            # Vamos apagar do Sanha
            p = open('tarefas.txt', 'r')
            linhas = [linha.replace('\n', '') for linha in p.readlines()]
            p.close()

            linhas.remove(tarefa_de_fato)

            os.remove('tarefas.txt')

            primeira = True
            with open("tarefas.txt", 'x') as base:
                for linha in linhas:
                    if primeira:
                        base.write(linha)
                        primeira = False
                    else:
                        base.write(f'\n{linha}')
        except:
            pass

    tree.bind('<Double-1>', apagando_tarefa)

    def adicionando_tarefa(event):
        vai_ser_adicionada = tarefa_a_ser_adicionada.get()

        # Limpando
        tarefa_a_ser_adicionada.delete(0, 'end')
        tarefa_a_ser_adicionada.focus()

        p = open('tarefas.txt', 'r')
        linhas = [linha.replace('\n', '') for linha in p.readlines()]
        p.close()

        linhas.append(vai_ser_adicionada)

        os.remove('tarefas.txt')

        primeira = True
        with open("tarefas.txt", 'x') as base:
            for linha in linhas:
                if primeira:
                    base.write(linha)
                    primeira = False
                else:
                    base.write(f'\n{linha}')

        # Devemos reiniciar, em teoria o treevoew, mas estava dando muito erro
        # Logo, só nos resta o Sanha
        janela.destroy()
        criar()

    tarefa_a_ser_adicionada.bind("<Return>", adicionando_tarefa)

    janela.mainloop()


if __name__ == '__main__':
    criar()
