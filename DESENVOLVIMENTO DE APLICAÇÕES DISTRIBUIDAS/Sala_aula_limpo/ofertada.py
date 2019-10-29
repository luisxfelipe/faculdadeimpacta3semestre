from flask import Flask, jsonify, request
import requests
import sqlite3
app = Flask(__name__)

create_sql = """           
CREATE TABLE IF NOT EXISTS Ofertadas (
    id INTEGER PRIMARY KEY,
    ano NOT NULL,
    semestre NOT NULL,
    turma TEXT NOT NULL,
    data TEXT NOT NULL,
    id_professor integer,
    id_disciplina integer
)
"""
connection = sqlite3.connect("ofertada.db")
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
    
    connection = sqlite3.connect("ofertada.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM Ofertada WHERE id = (?)"
    cursor.execute(sql, [id_item])

    ofertada = cursor.fetchone()
   
    if ofertada == None:
        raise NotFoundError

    return ({'id':ofertada[0],'ano':ofertada[1],'semestre':ofertada[2],
        'turma':ofertada[3], 'data': ofertada[4], 'id_professor':ofertada[5], 'id_disciplina':ofertada[6]})

def remove(id_o):
    connection = sqlite3.connect("ofertada.db")
    cursor = connection.cursor()
    sql = "DELETE FROM Ofertada WHERE id = ?"
    cursor.execute(sql, [id_o])
    connection.commit()
    connection.close()

def add(dic_disciplina):
    connection = sqlite3.connect("ofertada.db")
    cursor = connection.cursor()
    lista = []
    lista.append(dic_disciplina['id'])
    lista.append(dic_disciplina['ano'])
    lista.append(dic_disciplina['semestre'])
    lista.append(dic_disciplina['turma'])
    lista.append(dic_disciplina['data'])
    if 'id_professor' in dic_disciplina:
        lista.append(dic_disciplina['id_professor'])
    else:
        lista.append(None)

    if 'id_disciplina' in dic_disciplina:
        lista.append(dic_disciplina['id_disciplina'])
    else:
        lista.append(None)
    sql_criar = "INSERT INTO Ofertada (id,ano,semestre,turma,data,id_professor,id_disciplina) VALUES (?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(sql_criar, lista)
    connection.commit()
    connection.close()

@app.route('/ofertadas')
def disciplinas():
    return jsonify(todas_ofertadas())

def todas_ofertadas():
    connection = sqlite3.connect("ofertada.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM Ofertadas"
    cursor.execute(sql, [])

    ofertada = cursor.fetchone()
    resposta = []   
    while ofertada != None:
        dic_ofertadas = ({'id':ofertada[0],'ano':ofertada[1],'semestre':ofertada[2],
        'turma':ofertada[3], 'data': ofertada[4], 
        'id_professor':ofertada[5],'id_disciplina':ofertada[6]})
        resposta.append(dic_ofertadas)
        jogador = cursor.fetchone()
    return resposta

@app.route('/ofertadas/<int:id_disciplina>', methods=['GET','PUT','DELETE'])
def get_disciplina(id_disciplina):
    try: 
        disciplina_ofertada = localiza(id_disciplina)
        if request.method == 'PUT':
            novo_disciplina = request.json
            for key in disciplina_ofertada:
                if key in novo_disciplina:
                    disciplina_ofertada[key] = novo_disciplina[key]
            remove(id_disciplina)
            add(disciplina_ofertada)
        if request.method == 'DELETE':
            return remove(id_disciplina)
        return jsonify(disciplina_ofertada)
    except NotFoundError:
        return jsonify({'erro':'disciplina nao encontrada'}),400

def professor_valido(id_professor):
    r = requests.get(f'http://localhost:5002/professores/{id_professor}')
    return r.status_code == 200

def disciplina_valida(id_disciplina):
    r = requests.get(f'http://localhost:5002/disciplinas/{id_disciplina}')
    return r.status_code == 200

@app.route('/ofertadas', methods=['POST'])
def nova_disciplina_ofertada():
    nova_disciplina_ofertada = request.json
    campos_inteiros = ['id','ano','semestre']
    campos_texto = ['turma','data']
    campos_data = []
    campos_opcionais = ['id_professor','id_disciplina']
    valido,dic_erro = verifica_campos(nova_disciplina_ofertada,campos_inteiros,
            campos_texto,campos_data,campos_opcionais)

    if not valido:
        return dic_erro,400
    try:
        ofertadas = localiza(nova_disciplina_ofertada['id'])
        return jsonify({'erro':'id ja utilizada'}),400
    except:
        pass
    if 'id_professor' in nova_disciplina_ofertada:
        if not professor_valido(nova_disciplina_ofertada['id_professor']):
            return jsonify({'erro':'professor existe mas é inválido'}),400

    if 'id_disciplina' in nova_disciplina_ofertada:
        if not disciplina_valida(nova_disciplina_ofertada['id_disciplina']):
            return jsonify({'erro':'disciplina existe mas é inválido'}),400

    add(nova_disciplina_ofertada)
    return jsonify(todas_ofertadas())

@app.route('/reseta', methods=['POST'])
def reseta():
    connection = sqlite3.connect("ofertada.db")
    cursor = connection.cursor()
    sql = "DELETE FROM Ofertada"
    cursor.execute(sql)
    connection.commit()
    connection.close()
    return 'banco resetado'

if __name__ == '__main__':
    app.run(host='localhost', port=5004, debug=True)
