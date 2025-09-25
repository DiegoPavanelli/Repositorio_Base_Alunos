from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Aloha Mundo'

@app.route('/sobre')
def sobre():
    return 'Teste'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'ola {nome}! tudo bem?'
    
if __name__ == '__main__':
    app.run(debug=True)