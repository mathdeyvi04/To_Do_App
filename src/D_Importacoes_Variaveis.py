from customtkinter import *

import os
import json as js
from PIL import Image

variaveis_globais = {
    "Janela": {
        "Titulo_Do_App": "To_Do",
        "Dimensoes": (400, 600),
        "Icone": os.getcwd() + r"\icone.ico"  # Sempre conosco.
    },

    "Caminho_de_configuracoes": os.getcwd() + r"\config.json",
    "Caminho_de_Tarefas": os.getcwd() + r"\tarefas.json",
}

# Devemos verificar se o arquivo de tarefas existe.
# Caso não, criaremos ele.
for chave in variaveis_globais:
    if chave.startswith(
        "Cam"
    ):
        if not os.path.exists(
                variaveis_globais[
                    chave
                ]
        ):
            open(
                variaveis_globais[
                    chave
                ],
                "x"
            ).close()
