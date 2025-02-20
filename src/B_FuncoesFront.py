with open(
        r"C:\Users\deyvi\Documents\ImperioPy\Aplicativos\Tkinter\To_Do_App\src\C_Back.py",
        "r"
) as arq:
    exec(
        arq.read()
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
            "Titulo_Do_App"
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
