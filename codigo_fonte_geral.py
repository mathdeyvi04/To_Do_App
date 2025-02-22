from customtkinter import *
from tkinter.ttk import Treeview, Style
from tkinter import filedialog
from tkinter import messagebox as msb

import os
import json as js
from PIL import Image
from datetime import date

# Devemos verificar se o arquivo base está disponível.
# Caso não, devemos criá-lo do zero.
CAMINHO_DO_ARQUIVO_DE_CONFIG = os.getcwd() + r"\config.json"
if not os.path.exists(
        CAMINHO_DO_ARQUIVO_DE_CONFIG
):
    variaveis_globais = {
        "Janela": {
            "Titulo": "To_Do",
            "Dimensoes": (400, 600),
            "Icone": os.getcwd() + "\icone.ico"
        },
        "Tarefas": [
            # Dentro da lista, haverá dicionários
            # na forma de {"Data": ..., "Corpo": ...}
        ]
    }

    with open(
            CAMINHO_DO_ARQUIVO_DE_CONFIG,
            "x"
    ) as arq:
        js.dump(
            variaveis_globais,
            arq,
            indent=4
        )
else:
    with open(
            CAMINHO_DO_ARQUIVO_DE_CONFIG,
            "r"
    ) as arq:
        variaveis_globais = js.loads(
            arq.read()
        )


def adicionar_tarefa(
        entrada_de_tarefa: CTkEntry,
        tv: Treeview
) -> None:
    """Adicionamos a nova tarefa."""

    if entrada_de_tarefa.get() == "":
        return None

    hoje = str(date.today())

    # Adicionamos nas variáveis globais.
    variaveis_globais["Tarefas"].append(
        {
            "Data": hoje,
            "Corpo": entrada_de_tarefa.get()
        }
    )

    # Adicionamos no Treeview
    tv.insert(
        "",
        "end",
        values=(
            hoje,
            entrada_de_tarefa.get()
        )
    )
    entrada_de_tarefa.delete(0, "end")

    return None


def salvar_variaveis_globais(
        janela: CTk
) -> None:
    with open(
            CAMINHO_DO_ARQUIVO_DE_CONFIG,
            "w"
    ) as arq:
        js.dump(
            variaveis_globais,
            arq,
            indent=4
        )

    janela.destroy()


def selecionar_tarefa(
        tv: Treeview
) -> None:
    """
    Vamos apagar uma determinada tarefa selecionada.
    """

    item_sel = tv.selection()[0]

    tarefa_selecionada = tv.item(
        item_sel
    )["values"]

    tarefa_selecionada = {
        "Corpo": tarefa_selecionada[1],
        "Data": tarefa_selecionada[0]
    }

    variaveis_globais["Tarefas"].remove(
        tarefa_selecionada
    )

    tv.delete(item_sel)


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
        lambda event: adicionar_tarefa(entrada_do_usuario, tv)
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

    height = (variaveis_globais["Janela"]["Dimensoes"][1] - 70) - 50
    tv.place(
        x=0,
        y=200,
        # Função que define a variação de comprimento:
        width=variaveis_globais["Janela"]["Dimensoes"][0] * 1.235 + 8,
        height=height
    )

    tv.bind(
        "<Double-1>",
        lambda event: selecionar_tarefa(tv)
    )

    CTkLabel(
        janela,
        text="Clique duas vezes para apagar tarefa.",
        font=("Helvetica", 12),
        fg_color="#2e2e2e"
    ).place(
        x=5,
        y=height + 35
    )

    return tv


def possibilitar_customizacao(
        janela: CTk
) -> None:
    """
    Permitir algumas alterações na janela.
    """

    def puxar_barra_lateral() -> None:
        brl = CTkFrame(
            janela,

            width=variaveis_globais["Janela"]["Dimensoes"][0],
            height=variaveis_globais["Janela"]["Dimensoes"][1]
        )
        brl.place(
            x=0,
            y=0
        )

        # filedialog.askopenfilename()

        # Possibilitando modificações de tamanho.

        def verificar_novo_tam(
                novo_tam_digitado: str
        ) -> None:
            """Verificará se está no formato correto e se os números são válidos."""
            try:
                novo_comp, nova_alt = novo_tam_digitado.split("x")
                novo_comp = int(novo_comp)
                nova_alt = int(nova_alt)

                variaveis_globais["Janela"]["Dimensoes"] = [novo_comp, nova_alt]

                return None
            except:
                msb.showwarning(
                    "Atenção",
                    "Entrada de Novo Tamanho Inválida."
                )

        novo_tam = CTkEntry(
            brl,
            placeholder_text="Informe as novas dimensoes como COMPXALT",
            corner_radius=0,
            width=300
        )
        novo_tam.place(
            x=10,
            y=30
        )

        CTkLabel(
            brl,
            text=variaveis_globais["Janela"]["Papel de Parede"]["Caminho"],
            font=("Helvetica", 10)
        ).place(
            x=10,
            y=150
        )

        def obter_novo_wallpaper() -> None:
            caminho_para_novo_wp = filedialog.askopenfilename()

            if not os.path.exists(
                    caminho_para_novo_wp
            ):
                msb.showwarning(
                    "Atenção",
                    "Caminho não existe."
                )

                return None

            variaveis_globais[
                "Janela"
            ][
                "Papel de Parede"
            ]["Caminho"] = caminho_para_novo_wp

            CTkLabel(
                brl,
                text=variaveis_globais["Janela"]["Papel de Parede"]["Caminho"],
                font=("Helvetica", 10)
            ).place(
                x=10,
                y=150
            )

        CTkButton(
            brl,
            text="Alterar Papel de Parede",
            command=obter_novo_wallpaper
        ).place(
            x=7,
            y=120
        )

        novo_tam.bind(
            "<Return>",
            lambda event: verificar_novo_tam(novo_tam.get())
        )

        CTkButton(
            brl,
            text="Fechar",
            command=lambda: brl.destroy()
        ).place(
            x=10,
            y=variaveis_globais["Janela"]["Dimensoes"][1] - 40
        )

    CTkButton(
        janela,
        text="",
        width=30,
        height=30,
        fg_color="#65709c",
        bg_color="#65709c",
        hover_color="#495273",
        corner_radius=0,
        command=puxar_barra_lateral
    ).place(
        x=10,
        y=20
    )


janela = criar_janela()

tv = apresenta_tarefas(
    janela
)

entrada_do_usuario = permitindo_entrada(
    janela,
    tv
)

janela.protocol(
    "WM_DELETE_WINDOW",
    lambda: salvar_variaveis_globais(janela)
)

possibilitar_customizacao(
    janela
)

janela.mainloop()
