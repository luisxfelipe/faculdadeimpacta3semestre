from flask import Flask, jsonify, request
import util
app = Flask(__name__)
import disciplina

if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)