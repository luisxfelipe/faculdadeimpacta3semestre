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

    retorno = cursor.fetchall()

    #print('\nRetorno: ', retorno)

    tamanho = len(retorno)

    #print('\ntamanho: ', tamanho)

    count = 0

    if tamanho >0 :
        for i in retorno:
            #print('\nItem da lista: ',i)

            list_itens.append({'id':i[0],'idItem':i[1],'idHeroi':i[2]})

            #print('\nlist_itens [', count,']', list_itens[count])

            count += 1

    #print('\nlist_itens: ',list_itens)    

    return list_itens


