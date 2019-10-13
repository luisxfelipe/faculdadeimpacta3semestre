import sqlite3

class JogadorNaoExisteException(Exception):
    pass

connection = sqlite3.connect("rpg.db")
#1o passo: criar uma conexao
create_sql = """
CREATE TABLE IF NOT EXISTS Jogador (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
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

def criar_jogador(nome,email):
    connection = sqlite3.connect("rpg.db")
    #1o passo: criar uma conexao
    cursor = connection.cursor()
    #2o passo: pegar o cursor
    try:
        sql_criar = "INSERT INTO Jogador (nome,email) VALUES (?, ?)"
        cursor.execute(sql_criar, [nome,email])
        #3o passo: cursor.execute passando uma string de sql
        #(se for passar parametros, eles aparecem como ? na
        #string, e são passados por uma LISTA
        #no caso a lista [nome,email]

        # Repare que a minha query nao especificou uma coluna: a ID do usuário
        # nesse caso, o sqlite preenche essa coluna sozinho
        connection.commit()
        #4o passo: se voce alterou alguma coisa
        #precisa fazer um connection.commit()
    except sqlite3.IntegrityError as e:
        print('o sql está reclamando que o jogador ja foi criado')
        print('o email em questão: '+email)
    connection.close()
    #5o passo: fechar a conexao
'''
criar_jogador('lucas','lucas.goncalves@faculdadeimpacta.com.br')
criar_jogador('victor','victor.silva@faculdadeimpacta.com.br')
criar_jogador('matheus','email do matheus')
criar_jogador('Luis','luis.simoes@faculdadeimpacta.com.br')
'''
def consultar_jogador(id_j):
    connection = sqlite3.connect("rpg.db")
    #1o passo: criar uma conexao
    cursor = connection.cursor()
    #2o passo: pegar o cursor
    sql = "SELECT * FROM Jogador WHERE id = (?)"
    cursor.execute(sql, [id_j])
    #3o passo: cursor.execute passando uma string de sql
    #(se for passar parametros, eles aparecem como ? na
    #string, e são passados por uma LISTA (no caso [id_j],
    #uma lista com um unico elemento)

    #4o passo: voce nao alterou nada e não
    #precisa fazer um connection.commit()
    #em vez disso, vamos olhar o resultado!

    jogador = cursor.fetchone()
  
    #se o resultado for None, a busca resultou vazia
    if jogador == None:
        raise JogadorNaoExisteException

    connection.close()
    #5o passo: fechar a conexao

    return jogador
    #talvez fosse mais esperto retornar um dicionario?
    return {'id':jogador[0],'nome':jogador[1],'email':jogador[2]}

print(consultar_jogador(2))
def alterar_jogador(id_j,novos_dados):
    #antes de mais nada eu faço um localizar, pra garantir 
    #que o usuario realmente existe
    #se nao existir, o localizar faz o exception pra mim
    #e aborta a execução da funcao
    consultar_jogador(id_j)
    connection = sqlite3.connect("rpg.db")
    #1o passo: criar uma conexao
    cursor = connection.cursor()
    #2o passo: pegar o cursor
    sql = "UPDATE Jogador SET nome=?, email=? WHERE id = ?"
    cursor.execute(sql, [novos_dados['nome'],novos_dados['email'],id_j])
    #3o passo: cursor.execute passando uma string de sql
    #(se for passar parametros, eles aparecem como ? na
    #string, e são passados por uma LISTA

    #4o passo: se vc alterou alguma coisa
    #precisa fazer um connection.commit()
    connection.commit()

    
    connection.close()
    #5o passo: fechar a conexao
'''
print(consultar_jogador(1))
alterar_jogador(1,{'nome': 'lucas goncalves','email':'lucas.goncalves@faculdadeimpacta.com.br'})
print(consultar_jogador(1))
try:
    alterar_jogador(5,{'nome': 'lucas goncalves','email':'lucas.goncalves@faculdadeimpacta.com.br'})
except JogadorNaoExisteException:
    print('alterar jogador funcionou como devia, dando exception ao tentar alterar o jogador inexistente')
'''
def remover_jogador(id_j):
    #antes de mais nada eu faço um localizar, pra garantir 
    #que o usuario realmente existe
    #se nao existir, o deletar faz o exception pra mim
    #e aborta a execução da funcao
    consultar_jogador(id_j)
    connection = sqlite3.connect("rpg.db")
    #1o passo: criar uma conexao
    cursor = connection.cursor()
    #2o passo: pegar o cursor
    sql = "DELETE FROM Jogador WHERE id = ?"
    cursor.execute(sql, [id_j])
    #3o passo: cursor.execute passando uma string de sql
    #(se for passar parametros, eles aparecem como ? na
    #string, e são passados por uma LISTA

    #4o passo: se vc alterou alguma coisa
    #precisa fazer um connection.commit()
    connection.commit()

    
    connection.close()
    #5o passo: fechar a conexao

'''
criar_jogador('quarto','quarto@bol.com.br')
print(consultar_jogador(4))
remover_jogador(4)
try:
    consultar_jogador(4)
except JogadorNaoExisteException:
    print('excelente, depois de removido a consulta tem que dar exception mesmo')
'''
def conta_jogadores():
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM Jogador"
    #agora temos uma consulta que pode retornar muitos resultados
    cursor.execute(sql)

    #para ver quantos foram, basta pegar um a um
    #ate o resultado None
    jogadores = 0
    while (cursor.fetchone() != None):
        jogadores += 1


    connection.close()

    return jogadores

print(f"temos {conta_jogadores()} jogadores na base de dados no momento")

def consultar_jogador_por_email(email):
    connection = sqlite3.connect("rpg.db")

    cursor = connection.cursor()

    sql = "SELECT * FROM Jogador WHERE email = (?)"

    cursor.execute(sql, [email])

    jogador = cursor.fetchone()

    if jogador == None:
        raise JogadorNaoExisteException

    connection.close()

    #return jogador

    return {'id':jogador[0],'nome':jogador[1],'email':jogador[2]}
    
'''
Resumindo:
    * conectar ao banco para fazer um delete, update ou insert envolve 5 passos

    connection = sqlite3.connect("rpg.db")
    #1o passo: criar uma conexao
    
    cursor = connection.cursor()
    #2o passo: pegar o cursor
    
    sql = "DELETE FROM Jogador WHERE id = ?"
    cursor.execute(sql, [id_j])
    #3o passo: cursor.execute passando uma string de sql
    #(se for passar parametros, eles aparecem como ? na
    #string, e são passados por uma LISTA

    #4o passo: se vc alterou alguma coisa (fez delete, update ou insert)
    #precisa fazer um connection.commit()
    connection.commit()

    
    connection.close()
    #5o passo: fechar a conexao

    * se for fazer um select, o passo 4 muda. Em vez de fazer commit,
    fará fetchone para pegar um dado. O fetchone retorna uma linha se
    existir (e passa pra proxima). Retorna None se não existir mais nenhuma
    linha na consulta.
    
    while (cursor.fetchone() != None):
        jogadores += 1

    O retorno do fetchone é uma lista com uma posicao por coluna. Ex:
    jogador = cursor.fetchone()
    return {'id':jogador[0],'nome':jogador[1],'email':jogador[2]}
'''
