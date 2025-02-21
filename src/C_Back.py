with open(
        r"C:\Users\deyvi\Documents\ImperioPy\Aplicativos\Tkinter\To_Do_App\src\D_Importacoes_Variaveis.py",
        "r"
) as arq:
    exec(
        arq.read()
    )


def adicionar_tarefa(
        tarefa: str,
        tv: Treeview
) -> None:
    """Adicionamos a nova tarefa."""

    hoje = str(date.today())

    # Adicionamos nas variáveis globais.
    variaveis_globais["Tarefas"].append(
        {
            "Data": hoje,
            "Corpo": tarefa
        }
    )

    # Adicionamos no Treeview
    tv.insert(
        "",
        "end",
        values=(
            hoje,
            tarefa
        )
    )

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



