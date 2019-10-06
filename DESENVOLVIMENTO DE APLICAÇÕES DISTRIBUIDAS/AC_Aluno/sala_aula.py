from flask import Flask, jsonify, request

app = Flask(__name__)

database = {}
database['ALUNO'] = []
database['PROFESSOR'] = []

@app.route('/')
def all():
    return jsonify(database)

@app.route('/alunos')
def alunos():
    return jsonify(database['ALUNO'])

@app.route('/alunos', methods=['POST'])
def novo_aluno():
    novo_aluno = request.json
    database['ALUNO'].append(novo_aluno)
    return jsonify(database['ALUNO'])

@app.route('/alunos/<int:id_aluno>', methods=['GET']) 
def localiza_aluno(id_aluno):
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return 'nao achei', 404

@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def deleta_aluno(id_aluno):

    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            
            database['ALUNO'].pop(database['ALUNO'].index(aluno))
            #database['ALUNO'].pop(index)
            return jsonify(database['ALUNO'])
     
    return 'nao achei', 404


@app.route('/alunos/<int:id_aluno>/<string:nome_aluno>', methods=['PUT']) 
def edita_aluno(id_aluno,nome_aluno):
    
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            aluno['nome'] = nome_aluno['nome']
            #database['ALUNO'].pop(database['ALUNO'].index(aluno))
            #database['ALUNO'].pop(index)
            return jsonify(database['ALUNO'])
     
    return 'nao achei', 404

@app.route('/reseta', methods=['POST'])
def reseta():
    database['ALUNO'] = []
    database['PROFESSOR'] = []
    return jsonify(database['ALUNO'])



@app.route('/professores')
def professores():
    return jsonify(database['PROFESSOR'])

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)