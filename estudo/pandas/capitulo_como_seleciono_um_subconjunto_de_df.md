# Estudo de [pandas pydata org](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)




##  Capítulo Como seleciono um subconjunto de df ? 
O que aprenderemos :

- Leitura. (Armazenar todo(s) o(s) documento(s)). => read
- Impressão de dados brutos. => head
- Impressão da quantidade linhas na série da coluna selecionada. => shape
- Armazenar colunas específicas do dataframe. 
- Armazenar o tipo de dado na coluna selecionada. => type
- Armazenar quantidades de linhas na coluna selecionada.
- Armazenar múltiplas colunas. 
- Armazenar o tipo de dado de múlitplas colunas. 
- Armazenar quantidades de séries e colunas no dataframe. => shape
- Armazenar valores maiores que... de tal coluna. 
- Armazenar valores maiores que... de tal coluna saía em booleanos. 
- Armazenar coluna X valores Y e Z. => isin
- Armazenar valores não nulos na série (preenchidos). => notna
- Armazenar valores maiores que #num da coluna #col ao lado imprima coluna #col
- Armazenar da linha X a Y e coluna B a C: de #lin a #lin e colunas de #num a #num.
- Atribuir o nome anonymous nos #num primeiro itens da  coluna #num


#

    df = pd.read_#tipo("#local") 
    # Leitura(armazenamento) #tipo_de_arquivo #local

    print(df.head(#num)) 
    # Impressão de dados brutos #num (Quantidade de linhas a serem impressas)

    print(#col.shape)
    # Impressão quantidades de linhas na série da coluna selecionada #col

    armazenar_coluna_#col  = df["#col"]  
    # Armazenar colunas específicas do dataframe #col

    armazenar_tipos_de_valores_em_#col = type(df["#col"])
    # Armazenar o tipo de dado na coluna selecionada. #col

    armazenar_quantidade_de_linhas_na_coluna_#col = df['#col'].shape
    # Armazenar quantidade de linhas na coluna. #col

    armazenar_colunas_#col_#col = df[["#col", "#col"]]
    # Armazenar multiplas colunas. #col #col

    armazenar_tipo_de_dado_contidos_nas_colunas_#col_#col_ = type(df[["#col", "#col"]])
    # Armazenar o tipo de dado de múlitplas colunas. #col

    armazenar_quantidade_de_linhas_e_colunas_em_#col = df[["#", "#"]].shape
    # Armazenar quantidades de linhas e colunas no dataframe. #col #col

    armazenar__valores_maiores_que_#num_na_#col = df[df["#"] > #num]
    # Armazenar valores maiores que #num na coluna #col.

    armazenar_valores_maiores_que_#num_na_coluna_#col_saida_em_booleanos = df["#"] > #num
    # Armazenar valores maiores que #num na coluna #col saída em booleanos. #col #num

    armazenar_valores_da_coluna_#col__linhas_#lin_e_#lin = df[df["#"].isin([#, #])]
    # Armazenar valores da coluna #col linha #lin e #lin

    armazenar_valores_nao_nulos_em_#col = df[df["#"].notna()]
    # Armazenar valores não nulos em #col 

    armazenar_valores_maiores_que_#num_na_coluna_#bom__e_ao_lado_imprima_a_coluna_#col = df.loc[df["#"] > #num, "#"]
    # Armazenar valores maiores que #num da coluna #col e ao lado imprima a coluna #col

    armazenar_linhas_#lin_a_#lin_e_colunas_#num_a_#num = df.iloc[#lin:#lin, #col:#col]
    # Armazenar linhas:de #lin a #lin e colunas de #num a #num.

    df.iloc[0:#,#]="anonymous"
    # Atribuir o nome anonymous nos #num primeiro itens da  coluna #num







