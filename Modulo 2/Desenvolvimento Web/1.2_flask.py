from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Aloha Mundo'

@app.route('/sobre')
def sobre():
    return 'Teste'


if __name__ == '__main__':
    app.run(debug=True)