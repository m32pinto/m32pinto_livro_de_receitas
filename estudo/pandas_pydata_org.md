##  Capítulo Como seleciono um subconjunto de df ? 
O que aprenderemos

- Leitura.
- Impressão de dados brutos.
- Quantidades de linhas na colunas selecionada.
- Seleção de colunas específicas do dataframe.
- Solicitar o tipo de dado na coluna selecionada.
- Solicitar quantidades de linhas na coluna selecionada.
- Seleção de múltiplas colunas.

#

    df = pd.read_#tipo("#local") 
    # Leitura #tipo_de_arquivo #local

    print(df.head(#num)) 
    # Impressão de dados brutos #num (Quantidade de linhas a serem impressas)

    print(#col.shape)
    #quantidades de linhas na coluna #col

    coluna_#col  = df["#col"]  
    # Seleção de colunas específicas do dataframe #col

    tipos_de_valores_em_#col = type(df["#col"])
    # Solicitar o tipo de dado na colunas selecionada. #col

    contagem_de_linhas_na_coluna_#col = df['#col'].shape
    # Solicitar quantidades de linhas na coluna. #col

    selecao_de_colunas_#col_#col = df[["#col", "#col"]]
    # Seleção de múlitplas colunas. #col #col

    solicitar_o_tipo_de_dado_contidos_nas_colunas_#col_#col_ = type(df[["#col", "#col"]])
    # Solicitar o tipo de dado nas colunas selecionadas. #col

    solicitar_quantidade_de_linhas_e_colunas_em_#col = df[["#", "#"]].shape
    # Solicitar quantidades de linhas e colunas no dataframe. #col #col

    solicitar_em_#col_valores_maiores_que_#num = df[df["#"] > #num]
    #Estou interessado nos valores maiores que 35 dessa coluna imprima todos. #com #num

    solicitar_em_#col_valores_maiores_que_#num_saida_em_booleanos = df["#"] > #num]
    #Estou interessado nos valores maiores que 35 dessa coluna imprima todos saída em booleanos. #col #num

    valores_na_coluna_#col_nas_linhas_#lin_e_#lin = titanic[titanic["#"].isin([#, #])]
    # valores na coluna #col linha #lin e #lin

    solicitar_valores_nao_nulos_em_#col = df[df["#"].notna()]

    quantidade_de_valores_nao_nulos_em_# = df[df["#"].notna()]
    # Retornar quantidade de linhas e colunas que contém valores não nulos em #col

    valores_maiores_que_35_na_coluna_#_ao_lado_imprima_coluna_#col = df.loc[df["#"] > 35, "#"]
    # Valores maiores que 35 na coluna #col ao lado imprima coluna #col

    linhas_#lin_a_#lin_e_colunas_#num_a_#num = df.iloc[#lin:#lin, #col:#col]
    # Estou interessado nas linhas #lin a #lin e nas colunas #num a #num.

    df.iloc[0:#,#]="anonymous"
    # Atribuir o nome anonymous nos #num primeiro itens da  coluna #num







