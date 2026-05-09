# Estudo de [pandas pydata org](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)




##  Capítulo Como eu crio gráficos em pandas?
O que aprenderemos :

- Importar biblioteca de gráficos.
- Parametrizar a leitura. => index_col=#num ; parse_date=#bol
- Checagem visual simples. Plotar somente a data e mostrar o gráfico.
- 
-

#

    import matplotlib.pyplot as plt
    # Biblioteca pra análise de gráficos

    df = pd.read_#tipo("#local_do_arquivo", index_col=0, parse_dates=#bol)
    # index_col = 0 define a primeira coluna como índice.
    # parse_date = True converte a data em objetos em timestamp.

    df.plot() # plotar somente a data
    plt.show() # mostra os gráficos
    

    

