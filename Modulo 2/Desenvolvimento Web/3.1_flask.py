from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    return "hello flaks"


@app.route('/sobre')
def sobre():
    return 'ola sou aluno'


@app.route('/saudacao/<nome>')
def saudacao(nome):
    return 


if __name__ == '__main__':
    app.run(debug=True)
