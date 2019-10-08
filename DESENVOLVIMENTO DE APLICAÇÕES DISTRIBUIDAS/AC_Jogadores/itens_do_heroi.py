import sqlite3
      
class ItensNaoExisteException(Exception):
    pass


connection = sqlite3.connect("rpg.db")

create_sql = """
CREATE TABLE IF NOT EXISTS Item (
    id INTEGER PRIMARY KEY,
    idItem INTEGER NOT NULL,
    idHeroi INTEGER NOT NULL
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

def consulta_itens_por_heroi(idHeroi):

    list_itens = []

    connection = sqlite3.connect("rpg.db")

    cursor = connection.cursor()

    sql = "SELECT * FROM ItemDoHeroi WHERE idHeroi = (?)"

    cursor.execute(sql, [idHeroi])

    sqlteste = "SELECT * FROM ItemDoHeroi WHERE idHeroi = ", idHeroi, ""

    print('\n', sqlteste)

    itens = cursor.fetchone()

    if itens == None:
        raise ItensNaoExisteException

    while (cursor.fetchone() != None):
        itens = cursor.fetchone()
        list_itens.append({'id':itens[0], 'idItem':itens[1], 'idHeroi':itens[2]})
        print('\nmais um')
    cursor.close()

    print('\n',list_itens)    

    return list_itens
