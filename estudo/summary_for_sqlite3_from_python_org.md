sqlite3

# sqlite3 módulo geral
# instância getal para abrir, conectar e criar o banco de dados (connect)

import sqlite3
con = sqlite3.connect("tutorial.db")

# Conexão com banco de dados no disco (con)

cur = con.cursor()

# Criar tabela de banco de dados com titulo, ano e pontuação (execute("CREATE TABLE()")
 
cur.execute("CREATE TABLE movie(title, year, score)")

# verificação se a tabela foi criada ("SELECT name FROM sqlite_master")
# saída deve ser: movie

res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()

# verificação se a tabela é inexistente 
# a saída deve ser True

res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
res.fetchone() is None

# adição de dados (INSERT INTO VALUES())
# transação para confirmar alterações 

cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

con.commit()

# verificando se os dados foram corretamente inseridos (SELECT FROM)
# a saída deve ser os valores em score

res = cur.execute("SELECT score FROM movie")
res.fetchall()

# inserindo mais 3 linhas de dados através de uma variável executemany("(?, ?, ?)",X)

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.


# verificação de todas as linhas com loop for
# saída será todas linhas e colunas de informação título e ano

for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
print(row)

# fechando a primeira conexão e abrindo uma nova conexão no banco de dados
# retornando nome do título com maior release e ono


con.close()
new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()
print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')

new_con.close()