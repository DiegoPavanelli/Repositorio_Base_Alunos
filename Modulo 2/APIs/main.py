from flask import Flask, make_response, jsonify, request
from bd import carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS']= False

@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(
        jsonify(
            mensagem="Lista de carros",
            dados =carros
        )
    )

@app.route('/carros', methods=['POST'])
def create_carros():
    carro = request.json
    carros.append(carro)
    return make_response(
        jsonify(
        mensagem ="Novo carro adicionado com Sucesso",
        dados =carro
    ),201)

@app.rout('/carros/<int:id>', methods=['PUT'])
def update_carro(id):
    for carro in carros:
        if carro.get('id') == id:
            novo_carro = request.json
            carro.update(novo_carro)
            return make_response(
                jsonify(
                    mensagem = 'Carro atualizado com sucesso (PUT)',
                    dados =carro
                )
            )
        return make_response(jsonify(mensagem='Carro não encontrado'),404)


app.run()
