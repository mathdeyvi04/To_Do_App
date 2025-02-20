with open(
        r"C:\Users\deyvi\Documents\ImperioPy\Aplicativos\Tkinter\To_Do_App\src\B_FuncoesFront.py",
        "r"
) as arq:
    # Faremos dessa forma para não utilizarmos o path
    # da biblioteca sys.
    exec(
        arq.read()
    )

janela = criar_janela()
from customtkinter import *
# Dispor uma entrada para o usuário acrescentar tarefas
entrada_do_usuario = CTkEntry(
    janela,
    placeholder_text="Insira uma nova tarefa",
    corner_radius=0
)
entrada_do_usuario.place(
    x=10,
    y=100
)

janela.mainloop()
