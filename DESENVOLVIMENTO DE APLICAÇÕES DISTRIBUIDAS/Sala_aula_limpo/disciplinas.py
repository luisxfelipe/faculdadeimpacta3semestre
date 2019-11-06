from flask import Flask, jsonify, request
import requests
import sqlite3
app = Flask(__name__)

create_sql = """
CREATE TABLE IF NOT EXISTS Disciplina (
    id INTEGER PRIMARY KEY,
    status INTEGER NOT NULL,
    carga_horaria INTEGER NOT NULL,
    id_coordenador INTEGER,
    nome TEXT NOT NULL,
    plano_ensino TEXT NOT NULL
)
"""
connection = sqlite3.connect("disciplina.db")
cursor = connection.cursor()
cursor.execute(create_sql)
connection.commit()
connection.close()



class NotFoundError(Exception):
    pass


def erro(texto):
    return jsonify({'erro':texto})

def verifica_campos(dicionario,campos_inteiros=[], campos_texto=[], campos_data=[],campos_opcionais=[]):
    for campo in campos_inteiros+campos_texto+campos_data:
        if campo not in dicionario and campo not in campos_opcionais:
            return False,jsonify({'erro':campo+' faltando'})
    for campo in campos_inteiros:
        try:
            if campo in dicionario:
                int(dicionario[campo])
        except ValueError:
            return False, erro(campo+' deve ser inteiro')
    return True,''


def localiza(id_item):
    
    connection = sqlite3.connect("disciplina.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM Disciplina WHERE id = (?)"
    cursor.execute(sql, [id_item])

    jogador = cursor.fetchone()
   
    if jogador == None:
        raise NotFoundError

    return ({'id':jogador[0],'status':jogador[1],'carga_horaria':jogador[2],
        'id_coordenador':jogador[3], 'nome': jogador[4], 'plano_ensino':jogador[5]})


def remove(id_d):
    connection = sqlite3.connect("disciplina.db")
    cursor = connection.cursor()
    sql = "DELETE FROM Disciplina WHERE id = ?"
    cursor.execute(sql, [id_d])
    connection.commit()
    connection.close()

def add(dic_disciplina):
    connection = sqlite3.connect("disciplina.db")
    cursor = connection.cursor()
    lista = []
    lista.append(dic_disciplina['id'])
    lista.append(dic_disciplina['status'])
    lista.append(dic_disciplina['carga_horaria'])
    if 'id_coordenador' in dic_disciplina:
        lista.append(dic_disciplina['id_coordenador'])
    else:
        lista.append(None)
    lista.append(dic_disciplina['nome'])
    lista.append(dic_disciplina['plano_ensino'])
    sql_criar = "INSERT INTO Disciplina (id,status,carga_horaria,id_coordenador,nome,plano_ensino) VALUES (?, ?, ?, ?, ?, ?)"
    cursor.execute(sql_criar, lista)
    connection.commit()
    connection.close()
    

@app.route('/disciplinas')
def disciplinas():
    return jsonify(todas_disciplinas())

def todas_disciplinas():
    connection = sqlite3.connect("disciplina.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM Disciplina"
    cursor.execute(sql, [])

    jogador = cursor.fetchone()
    resposta = []   
    while jogador != None:
        dic_disciplina = ({'id':jogador[0],'status':jogador[1],
            'carga_horaria':jogador[2],
        'id_coordenador':jogador[3], 'nome': jogador[4], 'plano_ensino':jogador[5]})
        resposta.append(dic_disciplina)
        jogador = cursor.fetchone()
    return resposta

@app.route('/disciplinas/<int:id_disciplina>', methods=['GET','PUT','DELETE'])
def get_disciplina(id_disciplina):
    try: 
        disciplina = localiza(id_disciplina)
        if request.method == 'PUT':
            novo_disciplina = request.json
            for key in disciplina:
                if key in novo_disciplina:
                    disciplina[key] = novo_disciplina[key]
            remove(id_disciplina)
            add(disciplina)
        if request.method == 'DELETE':
            return remove(id_disciplina)
        return jsonify(disciplina)
    except NotFoundError:
        return jsonify({'erro':'disciplina nao encontrada'}),400

def professor_valido(id_professor):
    r = requests.get(f'http://localhost:5002/professores/{id_professor}')
    return r.status_code == 200

@app.route('/disciplinas', methods=['POST'])
def nova_disciplina():
    nova_disciplina = request.json
    campos_inteiros = ['id','status','carga_horaria','id_coordenador']
    campos_texto = ['nome','plano_ensino']
    campos_data = []
    campos_opcionais = ['id_coordenador']
    valido,dic_erro = verifica_campos(nova_disciplina,campos_inteiros,
            campos_texto,campos_data,campos_opcionais)
    if not valido:
        return dic_erro,400
    try:
        disciplina = localiza(nova_disciplina['id'])
        return jsonify({'erro':'id ja utilizada'}),400
    except:
        pass
    if 'id_coordenador' in nova_disciplina:
        if not professor_valido(nova_disciplina['id_coordenador']):
            return jsonify({'erro':'coordenador existe mas é inválido'}),400
    add(nova_disciplina)
    return jsonify(todas_disciplinas())


@app.route('/reseta', methods=['POST'])
def reseta():
    connection = sqlite3.connect("disciplina.db")
    cursor = connection.cursor()
    sql = "DELETE FROM Disciplina"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    return 'banco resetado'

if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)

