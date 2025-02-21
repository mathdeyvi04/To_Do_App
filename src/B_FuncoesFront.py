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
    ).place(
        x=0,
        y=0
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
