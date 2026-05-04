    """
    📁 Nome do arquivo:variacao_de_percentual.py | 👤 m32pinto | 🔄 Repyta 
    🎯 Objetivo
    """

    # =============================================================================
    # IMPORTAÇÕES E CONFIGURAÇÕES GLOBAIS
    # =============================================================================

    # pandas: biblioteca padrão para manipulação de dados tabulares (como planilhas)
    import pandas as pd
    # matplotlib.pyplot: módulo principal para criação de gráficos
    import matplotlib.pyplot as plt
    # matplotlib.ticker: controle fino de formatação dos eixos do gráfico
    import matplotlib.ticker as ticker
    # numpy: suporte a operações numéricas e criação de arrays/posições
    import numpy as np

    # Define o estilo visual do gráfico ('ggplot' simula a estética do R)
    plt.style.use('ggplot')
    # Define o tamanho padrão das figuras (largura=12, altura=5 em polegadas)
    plt.rcParams['figure.figsize'] = (12, 5)


    # =============================================================================
    # FUNÇÕES AUXILIARES
    # =============================================================================

    def padronizar_moeda_br(series):
        """
        Converte textos no formato de moeda brasileira (ex: 'R$ 1.250,00')
        para números do tipo float (ex: 1250.0).
        """
        # 1. Converte tudo para string e remove espaços laterais
        s = series.astype(str).str.strip()
        # 2. Remove o símbolo 'R$' e espaços internos
        s = s.str.replace('R$', '', regex=False).str.replace(' ', '', regex=False)
        
        # 3. Se a string contém vírgula (formato BR), troca ponto por vazio 
        #    (remove separador de milhar) e vírgula por ponto (decimal do Python).
        #    Se não tem vírgula, mantém o valor original.
        s_limpo = s.where(
            ~s.str.contains(',', regex=False),
            s.str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
        )
        
        # 4. Converte para número. Erros de conversão viram NaN (valores ausentes)
        return pd.to_numeric(s_limpo, errors='coerce')


    def formatar_real_br(val, pos):
        """
        Formata um número float para exibição no eixo Y no padrão brasileiro.
        'val' é o número, 'pos' é a posição (exigido pelo FuncFormatter, mas não usado).
        """
        # Formata com separador de milhar em vírgula e decimal em ponto (padrão US)
        # Depois inverte: ponto → vírgula, vírgula → ponto
        return f'R$ {val:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')


    def plot_barras_com_valores_e_variacao(df, x, y, titulo='', cor='steelblue', ylim=None):
        """
        Cria um gráfico de barras com:
        - Eixo X categórico
        - Valores em R$ no topo das barras
        - Eixo Y formatado em moeda BR
        - Anotação de variação percentual entre dois anos específicos
        """
        # Cria figura e eixo (axes) com tamanho fixo
        fig, ax = plt.subplots(figsize=(10, 5))

    # Garante que os rótulos do eixo X sejam strings (categorias)
    labels = df[x].astype(str).tolist()
    valores = df[y].tolist()

    # Cria posições numéricas para as barras no eixo X
    x_pos = np.arange(len(labels))
    # Desenha as barras
    bars = ax.bar(x_pos, valores, color=cor, edgecolor='white', linewidth=1.2, width=0.6)

    # Define as marcas do eixo X nas posições calculadas
    ax.set_xticks(x_pos)
    # Define os textos das marcas (rótulos)
    ax.set_xticklabels(labels, fontsize=11)

    # Rótulos dos eixos e título
    ax.set_xlabel('Ano', fontsize=11)
    ax.set_ylabel('Valor (R$)', fontsize=11)
    ax.set_title(titulo, fontsize=13, fontweight='bold')
    
    # Grade de fundo apenas no eixo Y, semi-transparente e tracejada
    ax.grid(axis='y', alpha=0.3, linestyle='--')

    # Define limites do eixo Y se o parâmetro ylim for fornecido
    if ylim:
        ax.set_ylim(ylim)

    # Aplica a função de formatação personalizada ao eixo Y
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(formatar_real_br))
    # Define no máximo 6 marcas no eixo Y para evitar poluição visual
    ax.yaxis.set_major_locator(ticker.MaxNLocator(6))

    # Adiciona o valor formatado no topo de cada barra
    for bar, val in zip(bars, valores):
        height = bar.get_height()
        ax.annotate(
            f'R$ {val:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'),
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 6), textcoords="offset points",
            ha='center', va='bottom', fontsize=10, fontweight='bold'
        )

    # ========================================================================
    # CÁLCULO E ANOTAÇÃO DA VARIAÇÃO ENTRE 2024 E 2025
    # ========================================================================
    if 2024 in df[x].values and 2025 in df[x].values:
        # Extrai os valores correspondentes aos anos
        val_2024 = df.loc[df[x] == 2024, y].iloc[0]
        val_2025 = df.loc[df[x] == 2025, y].iloc[0]

        # Cálculo da variação percentual
        variacao = ((val_2025 - val_2024) / val_2024) * 100
        cor_seta, simbolo = ('green', '▲') if variacao >= 0 else ('red', '▼')

        # Encontra o índice original do DataFrame correspondente a 2025
        idx_2025 = df[df[x] == 2025].index[0]

        # Cria a anotação com seta apontando para o topo da barra de 2025
        ax.annotate(
            f'{simbolo} {variacao:+.1f}%',
            xy=(idx_2025, val_2025),
            xytext=(0, 55), textcoords='offset points',
            ha='center', va='bottom', fontsize=12, fontweight='bold', color=cor_seta,
            arrowprops=dict(arrowstyle='->', color=cor_seta, lw=2.5, shrinkA=1, shrinkB=18)
        )

    # Ajusta automaticamente os espaçamentos para evitar sobreposição
    plt.tight_layout()
    return ax


    # =============================================================================
    # CARREGAMENTO E TRATAMENTO DOS DADOS
    # =============================================================================

    # Lê arquivo ODS. O engine='odf' é necessário pois o pandas não lê .ods nativamente
    df = pd.read_excel('./rotha/rotha.ods', engine='odf')

    # 🔍 Detecta se as colunas 'valor' e 'ano' estão trocadas na planilha
    # Verifica se o primeiro valor da coluna 'valor' começa com '20' (padrão de ano)
    if str(df['valor'].iloc[0]).strip().startswith('20'):
        # Troca os conteúdos das colunas usando .copy() para evitar warnings do pandas
        df['valor'], df['ano'] = df['ano'].copy(), df['valor'].copy()

    # Converte a coluna 'ano' para número. Valores não numéricos viram NaN
    df['ano'] = pd.to_numeric(df['ano'], errors='coerce')
    # Aplica a função de limpeza de moeda à coluna 'valor' usando .pipe()
    df['valor_limpo'] = df['valor'].pipe(padronizar_moeda_br)
    # Remove linhas onde 'ano' ou 'valor_limpo' estão ausentes (NaN)
    df = df.dropna(subset=['ano', 'valor_limpo'])

    # ✅ FILTRO DE ANOS (ajuste aqui se quiser incluir 2026, por exemplo)
    df = df[df['ano'].isin([2024, 2025])]

    # Agrupa por ano e soma os valores. reset_index() transforma o índice em coluna normal
    evolucao_ano = df.groupby('ano')['valor_limpo'].sum().reset_index()
    # Ordena por ano e reindexa para garantir sequência contínua (0, 1, 2...)
    evolucao_ano = evolucao_ano.sort_values('ano').reset_index(drop=True)


    # =============================================================================
    # GERAÇÃO DO GRÁFICO
    # =============================================================================

    plot_barras_com_valores_e_variacao(
        df=evolucao_ano,
        x='ano',
        y='valor_limpo',
        titulo='ROTHA COMERCIO E SERVICOS LTDA  — Evolução 2024 → 2026',
        cor='steelblue',
        ylim=(40_000, 90_000)  # [ADAPTÁVEL] Ajuste conforme a escala dos seus dados
    )
    plt.show()  # Exibe o gráfico na tela

    # >>> FIM.

"""
Prompts: Comente esse código, explicando linha por linha
de forma clara e didática, para que um iniciante possa entender o que cada parte do código faz.
Esse código será utilizado em um livro de receitas de Python,
 então a explicação deve ser detalhada e acessível, evitando jargões técnicos sem explicação prévia, 
 Alem disso o código será reutilizado em outros contextos, então a explicação deve ser 
 genérica o suficiente para ser aplicada a outros casos de uso semelhantes. Os trechos de
 código quem podem ser alterados para se adaptar a outros contextos devem ser destacados, 
 e a explicação deve incluir sugestões de como modificar esses trechos para diferentes situações.
"""