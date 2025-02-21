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
    font=(
        "Helvetica",
        15
    ),
    placeholder_text="Insira uma nova tarefa",
    corner_radius=0,
    width=300,
    height=40
)
entrada_do_usuario.pack(
    fill="x",
    pady=100
)

entrada_do_usuario.bind(
    "<Return>",
    lambda event: adicionar_tarefa(entrada_do_usuario.get())
)

# Dispor as tarefas cadastradas.
tv = Treeview(
    janela,
    columns=[
        "Data",
        "Corpo"
    ],
    show="headings"
)

tv.heading(
    "Data",
    text="Data"
)
tv.heading(
    "Corpo",
    text="Corpo"
)




janela.mainloop()
