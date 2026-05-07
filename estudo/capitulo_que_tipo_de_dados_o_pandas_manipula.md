# Estudo de [pandas pydata org](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)

##  Capítulo Que tipo de dados o pandas manipula ? 
O que aprenderemos

- Aramazenar dados em um dataframe puro.
- Armazenar e criar séries do zero.
- Armazenar o maior valor da série.
- Armazenar (Quantidade de valores, Média, valor mínimo e máximo...) estatistica básica).

     
    df = pd.DataFrame(
        {
            "#col": ["#str","#str","#str",],
            "#col": [#num, #num, #num],
            "#col": ["#str", "#str", "#str"],
        }
    # DataFrame Puro

    serie = pd.Series([#num, #num, #num], name="#str")
    # Criando séries do zero valores em #num nome da coluna em #str.

    maior_valor_da_serie_#col = df["#col"].max()
    # Armazenar o maior valor da série #col.

    estatistica_basica = df.describe()
    # Estatística basica
    



    