from flask import Flask
from flask import jsonify
app = Flask(__name__) #burocra do flask
		
@app.route("/") #decorator associando a funcao a uma URL
def hello():                     #funcao que retorna string
        return "Hello Lucas!"

@app.route("/futebol")
def a():
    print("vasco, tente outra vez...")
    return "Vai curinthia!"

@app.route("/agenda")
def agenda():
    dic = {}
    dic['nome'] = 'lucas'
    dic['email'] = 'lucas.goncalves@faculdadeimpacta.com.br'
    return jsonify(dic)#tem que retornar string
    #entao eu usei o flask pra converter o dicionario
    #em string


if __name__ == '__main__':
        app.run(host = 'localhost', port = 5002, debug = True)
