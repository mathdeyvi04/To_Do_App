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
