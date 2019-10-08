import sqlite3
      
class HeroiNaoExisteException(Exception):
    pass


connection = sqlite3.connect("rpg.db")

create_sql = """
CREATE TABLE IF NOT EXISTS Heroi (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    fisico INTEGER NOT NULL,
    magia INTEGER NOT NULL,
    agilidade INTEGER NOT NULL
)
"""

cursor = connection.cursor()
#2o passo: pegar o cursor
cursor.execute(create_sql)
#3o passo: cursor.execute passando uma string de sql
connection.commit()
#4o passo: fazer o commit (se for uma query que altera o banco)
connection.close()
#5o passo: fechar a conexao

def consultar_heroi(id_h):
    connection = sqlite3.connect("rpg.db")

    cursor = connection.cursor()

    sql = "SELECT * FROM Heroi WHERE id = (?)"

    cursor.execute(sql, [id_h])

    heroi = cursor.fetchone()

    if heroi == None:
        raise HeroiNaoExisteException

    cursor.close()

    return {'id':heroi[0], 'nome':heroi[1], 'fisico':heroi[2], 'magia':heroi[3], 'agilidade':heroi[4]}
