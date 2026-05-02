# m32pinto livro de receitas.

Esse repositório servirá para facilitar a análise de dados, e criação de scripts, contém requisitos básicos para processamentos eficientes e boas práticas.

##  Cabeçalho e rodapé padrão

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    """

    📁 ${FILENAME} | 👤 m32pinto | 🔄 Repyta | 🗓️ ${DATE}
    🎯 ${1:Objetivo em uma linha}

    """

    # >>> CONFIG INICIAL

    %matplotlib inline
    import pandas as pd, matplotlib.pyplot as plt, os
    plt.style.use('ggplot'); plt.rcParams['figure.figsize'] = (15, 5)

    # >>> SEU CÓDIGO AQUI

    $0

    # >>> FIM: ✅ OK | 🧪 Testar: [ ] Leitura [ ] Processamento [ ] Saída

## Importações.
### Sempre que inicar um projeto:

    # Renderize nossos gráficos em linha
    %matplotlib inline

    import pandas as pd
    import matplotlib.pyplot as plt

    # Deixe os gráficos um pouco mais bonitos e maiores
    plt.style.use('ggplot')
    plt.rcParams['figure.figsize'] = (15, 5)

    # Lidar com pastas/arquivos
    import os

## Leitura dos dados.

### Apenas um conjunto:

    # =============================================================================
    # LEITURA DE UM ÚNICO CONJUNTO DE DADOS
    # =============================================================================

    # Lê um arquivo CSV e armazena em um DataFrame (tabela estruturada do pandas)
    # './local_do_arquivo.csv' deve ser substituído pelo caminho real do seu arquivo
    # Atenção no tipo de arquivo: read_csv, execel, odf
    
    df = pd.read_csv('./local_do_arquivo.csv')

    # 💡 Dica: Sempre verifique as primeiras linhas após o carregamento
    # print(df.head())  # Exibe as 5 primeiras linhas
    # print(df.info())  # Mostra tipos de dados e valores não nulos

### Vários conjuntos:

    # =============================================================================
    # LEITURA DE MÚLTIPLOS ARQUIVOS E CONSOLIDAÇÃO EM UM ÚNICO DATAFRAME
    # Ideal para: dados particionados por mês, regiões, ou lotes grandes
    # =============================================================================

    # Lista com os caminhos de todos os arquivos CSV que serão processados
    arquivos = [
        './dados/janeiro.csv',
        './dados/fevereiro.csv',
        './dados/marco.csv'
    ]

    # Lista vazia que armazenará temporariamente cada DataFrame lido
    dfs = []

    # Loop para percorrer cada caminho de arquivo na lista
    for arquivo in arquivos:
    """
    Parâmetros importantes do pd.read_csv():
    
    - sep=';' : Define o delimitador do arquivo (padrão é vírgula ',')
    - encoding='iso-8859-1' : Codificação para ler caracteres especiais (acentos, ç, etc.)
                              Use 'utf-8' se seu arquivo estiver nesse formato
    - on_bad_lines='skip' : Ignora linhas com formato incorreto sem interromper a execução
                            (em versões antigas do pandas, use 'error_bad_lines=False')
    """
    df_temp = pd.read_csv(
        arquivo,
        sep=';',
        encoding='iso-8859-1',
        on_bad_lines='skip'
    )
    
    # Adiciona o DataFrame lido à lista temporária
    dfs.append(df_temp)
    
    # 💡 Boa prática: Log simples para acompanhar o progresso
    print(f"✓ Arquivo lido: {os.path.basename(arquivo)} | Linhas: {len(df_temp)}")

    # Concatena todos os DataFrames da lista em um único DataFrame
    # ignore_index=True renumera as linhas sequencialmente (0, 1, 2, ...)
    df = pd.concat(dfs, ignore_index=True)

    # Libera memória removendo a lista temporária (opcional, mas recomendado para grandes volumes)
    del dfs

    print(f"\n✅ Dados consolidados! Total de linhas: {len(df)}")

## Bibliotecas muito interessantes:

[Phonenumbers](https://pypi.org/project/phonenumbers/)

[Selenium](https://www.selenium.dev/)

[Time](https://docs.python.org/pt-br/3/library/time.html)

[Openpyxl](https://pypi.org/project/openpyxl/)

[Os](https://docs.python.org/3/library/os.html)

[Matplotlib](https://matplotlib.org/stable/)




