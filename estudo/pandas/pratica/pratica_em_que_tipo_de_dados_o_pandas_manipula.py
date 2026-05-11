"""

📁 Nome do arquivo:dataframe_com_adicao.py | 👤 m32pinto | 🔄 Repyta |
🎯 Objetivo

Referências

https://pandas.pydata.org/docs/reference/api/pandas.concat.html#pandas.concat
https://docs.python.org/3/tutorial/controlflow.html

"""



import pandas as pd

# Missão 1: Criar dataframe puro para CRT 02 de atendimento, que receberá arquivos de um input.



df = pd.DataFrame(
    {
        "telefone": ["559184924543","559184943243","582384924543",],
        "cpf": ["02183029488", "02432129488", "0432212972"],
    }
)

print(df.head(2))

entrada_do_telefone = input('Digite o Telefone: ') # deverá ser adicionado na coluna telefone


entrada_do_cpf = input('Digite o CPF: ') # deverá ser adicionado na coluna CPF

novos_dados_de_entrada = pd.DataFrame({
    "telefone": [entrada_do_telefone],
    "cpf": [entrada_do_cpf]
})

df = pd.concat([df, novos_dados_de_entrada], ignore_index = True)

print("Dataframe atualizado\n")
print(df)

