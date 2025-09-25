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

@app.route('/dobro/<int:numero>') # uma rota nao aceita '.', ou seja, nao usamos float.
#Sem a informação do tipo de dado o python concatena
def dobro(numero):
    return f'O dobro do número {numero} e {2*numero}.'
    
if __name__ == '__main__':
    app.run(debug=True)