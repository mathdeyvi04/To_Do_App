with open(
        r"C:\Users\deyvi\Documents\ImperioPy\Aplicativos\Tkinter\To_Do_App\src\C_Back.py",
        "r"
) as arq:
    exec(
        arq.read()
    )


def adicionar_papel_de_parede(
        janela: CTk
) -> None:
    """
    Autoexplicativo
    """

    imagem = Image.open(
        variaveis_globais["Janela"]["Papel de Parede"]["Caminho"]
    ).convert("RGBA")

    imagem.putalpha(
        variaveis_globais["Janela"]["Papel de Parede"]["Opacidade"]
    )

    imagem_config = CTkImage(
        imagem,
        size=variaveis_globais["Janela"]["Dimensoes"]
    )

    CTkLabel(
        janela,
        image=imagem_config,
        text=""
    ).pack(
        fill="both"
    )


def criar_janela() -> CTk:
    """
    Descrição:
        Cria uma janela CTk. Note não haver a possibilidade
        de criação de uma subjanela. Apenas mexeremos com
        frames.
    """

    janela = CTk()
    janela.title(
        variaveis_globais["Janela"][
            "Titulo"
        ]
    )
    dimensoes = variaveis_globais["Janela"][
        "Dimensoes"
    ]
    janela.geometry(
        f"{dimensoes[0]}x{dimensoes[1]}"
    )
    janela.iconbitmap(
        variaveis_globais["Janela"]["Icone"]
    )

    if "Papel de Parede" in variaveis_globais["Janela"]:
        adicionar_papel_de_parede(
            janela
        )

    CTkLabel(
        janela,
        font=(
            None, 25
        ),
        text="Gerenciador"
    ).place(
        x=(
                  dimensoes[0] - 130
          ) // 2,
        y=10
    )

    return janela


def permitindo_entrada(
        janela: CTk,
        tv: Treeview
) -> CTkEntry:
    """Autoexplicativo"""
    entrada_do_usuario = CTkEntry(
        janela,
        font=(
            "Helvetica",
            15
        ),
        placeholder_text="Insira uma nova tarefa",
        corner_radius=0,
        width=variaveis_globais["Janela"]["Dimensoes"][0],
        height=40
    )
    entrada_do_usuario.place(
        x=0,
        y=100
    )

    entrada_do_usuario.bind(
        "<Return>",
        lambda event: adicionar_tarefa(entrada_do_usuario.get(), tv)
    )

    return entrada_do_usuario


def apresenta_tarefas(
        janela: CTk
) -> Treeview:
    # Dispor as tarefas cadastradas.
    tv = Treeview(
        janela,
        columns=[
            "Data",
            "Corpo"
        ],
        show="headings",
    )

    tv.heading(
        "Data",
        text="Data"
    )
    tv.heading(
        "Corpo",
        text="Corpo"
    )

    tv.column(
        "Data",
        anchor="center",
    )
    tv.column(
        "Corpo",
        anchor="center"
    )

    style = Style()
    style.theme_use("default")  # Usa o tema padrão do Tkinter

    # Configurações para o tema escuro
    style.configure("Treeview",
                    font=(
                        "Helvetica",
                        15
                    ),
                    rowheight=40,
                    background="#2e2e2e",  # Cor de fundo
                    foreground="white",  # Cor do texto
                    fieldbackground="#2e2e2e",  # Cor de fundo dos campos
                    borderwidth=0
                    )

    style1 = Style()

    style1.configure(
        "Treeview.Heading",
        font=("Arial", 12, "bold"),  # Fonte personalizada
        foreground="white",  # Cor do texto
        background="#2e2e2e",  # Cor de fundo
        padding=10  # Espaçamento interno
    )

    style.map("Treeview", background=[("selected", "#3e3e3e")])
    style1.map("Treeview.Heading", background=[("selected", "#3e3e3e")])

    for tarefa in variaveis_globais["Tarefas"]:
        tv.insert(
            "",
            "end",
            values=(
                tarefa["Data"],
                tarefa["Corpo"]
            )
        )

    tv.place(
        x=0,
        y=200,
        # Devemos realizar uma regressão e descobrir como esses
        # números estão sendo alterados.
        width=variaveis_globais["Janela"]["Dimensoes"][0]
    )

    return tv
