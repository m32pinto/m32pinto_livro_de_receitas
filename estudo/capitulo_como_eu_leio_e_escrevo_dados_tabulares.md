



- Leitura (amazenar dataframe em memoria e renomeando)
- Impressão do dataframe, linhas e colunas.
- Impressão de X linhas. => head()
- Armazenar tipos de dados nas colunas. => dtype
- Exportar columas do documento para arquivo. => to_excel()
- Armazenar sumário técnico de um arquivo. => info()

#

    df = pd.read_#tipo("#local_do_arquivo",sheet_name="#str)
    # Leitura (amazenar dataframe em memoria e renomeando)

    print(df)
    # Impressão bruta do dataframe

    tipos_de_dados_nas_colunas = df.dtype
    # Armazenar tipos de dados nas colunas.

    exportar_coluna_#col = df.to_excel("#local_do_arquivo", sheet_name="#str", index=#bol)
    # Exportar as colunas do documento para arquivo. #local_do_arquivo, nome do arquivo: #str, sem índice numérico #false

    sumario_tecnico_de_#nome = df.info()
    # Armazenar sumário técnico de um arquivo

    

    

    

    