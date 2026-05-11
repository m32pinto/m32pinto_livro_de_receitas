import pandas as pd


df = pd.read_csv("./banco_de_dados/titanic.csv") 
    # Leitura(armazenamento) #csv #./banco_de_dados/titanic.csv

# Missão 1: Selecionar a coluna Age e saber se tem algum valor nulo (NaN) nessa coluna.
# Total de linhas na série ? R:891
# Quantas linhas preechidas ? R: 714
# Quantas linhas vazias ? R: 177

# Missão 2: Verificar tipo de valores que estão na coluna tickets.
# Total de linhas na séries ? R: 891
# Quantas séries preechidas ? R: 891
# Quantas séries vazias ? R: 0
# Tipos de valores contidos na série ? R: object

# Missão 3: Verificar quantas mulheres tinham no titanic.
# Total de linhas na séries ? R: 891
# Quantas séries preechidas ? R: 891
# Quantas séries vazias ? R: 0
# Tipos de valores contidos na série ? R: object 
# Quantas mulheres tinham no titanic ? R: 314

# Missão 5: Quantos homens menores de 18 anos tinham no titanic.
# Total de linhas na séries ? R: 891
# Quantas séries preechidas ? R: 891
# Quantas séries vazias ? R: 0
# Tipos de valores contidos na série ? R: object
# Quantas mulheres tinham no titanic ? R: 314
# Quantos homens menores de 18 anos tinham no titanic ? R: 53 Porém na planilha da 58.


# Descobertas:
# .isna() => Retorna um booleano indicando se os valores são NaN ou não.
# https://docs.python.org/pt-br/3/library/operator.html Aula de operadores lógicos


armazenar_coluna_Sex  = df["Sex"]  
    # Armazenar colunas específicas na série Sex

valores_nao_nulos_em_Sex = df[df["Sex"].notna()]
    # Armazenar linhas não nulas em Sex

valores_nulos_em_Sex = df[df["Sex"].isna()]
    # Armazenar linhas nulas em Sex

armazenar_tipos_de_valores_em_Sex = df["Sex"]
    # Armazenar o tipo de dado na coluna Sex.
    
armazenar_quantidade_de_mulheres = df[(df['Sex'] == "female")]
    # Armazenar quantidade de mulheres

armazenar_quantidade_de_homens_menores_de_18_anos = df[(df["Sex"] == "male") & (df["Age"] < 18)]

print(armazenar_coluna_Sex.shape)
    # Impressão da quantidade linhas na coluna selecionada. 

print(valores_nao_nulos_em_Sex.shape) 
    # Impressão de quantidade de linhas não nulas

print(valores_nulos_em_Sex.shape)
    # Impressão de linhas nulas em Sex.

print(armazenar_tipos_de_valores_em_Sex)
    # Impressão de tipo de dado na coluna Sex.

print(armazenar_quantidade_de_mulheres.shape)
    # Impressão da quantidade de mulheres que tinham no titanic.

print(armazenar_quantidade_de_homens_menores_de_18_anos)
    # Impressão da quantidade de homens menores de 18 anos tinham no titanic.