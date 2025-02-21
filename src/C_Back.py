with open(
        r"C:\Users\deyvi\Documents\ImperioPy\Aplicativos\Tkinter\To_Do_App\src\D_Importacoes_Variaveis.py",
        "r"
) as arq:
    exec(
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




