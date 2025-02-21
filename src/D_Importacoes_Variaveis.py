from customtkinter import *
from tkinter.ttk import Treeview, Style


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

