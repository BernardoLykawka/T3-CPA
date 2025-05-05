from flask import Flask, abort, jsonify, make_response, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('cars.csv')
df['id'] = df.index  

lista_carros = df.to_dict(orient='records')

@app.route('/carros', methods=['GET', 'POST'])
def carros():
    if request.method == 'GET':
        return make_response(jsonify(lista_carros), 200)
    
    elif request.method == 'POST':
        dados = request.get_json()
        novo_carro = dados 

        novo_id = max([carro['id'] for carro in lista_carros], default=0) + 1
        novo_carro['id'] = novo_id
        lista_carros.append(novo_carro)

        return make_response(jsonify({"mensagem": "Carro adicionado", "carro": novo_carro}), 201)

@app.route('/carro/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def carro_por_id(id):
    carro = next((c for c in lista_carros if c['id'] == id), None)
    if carro is None:
        return make_response(jsonify("Carro não encontrado"), 404)

    if request.method == 'GET':
        return make_response(jsonify(carro), 200)

    elif request.method == 'PUT':
        dados = request.get_json()
        for i, c in enumerate(lista_carros):
            if c['id'] == id:
                dados['id'] = id 
                lista_carros[i] = dados
                return make_response(jsonify("Carro atualizado"), 200)

    elif request.method == 'DELETE':
        for i, c in enumerate(lista_carros):
            if c['id'] == id:
                lista_carros.pop(i)
                return make_response(jsonify("Carro deletado"), 200)

    else:
        abort(404)

@app.route('/carros/<int:n>', methods=['GET'])
def carros_por_n(n):
    if n > len(lista_carros):
        return make_response(jsonify("Número de carros solicitado é maior que o disponível"), 404)
    
    lista_carros_n = lista_carros[:n]
    return make_response(jsonify(lista_carros_n), 200)

@app.route('/carros/<string:name>', methods=['GET'])
def carros_por_nome(name):
    lista_filtrada = [
        carro for carro in lista_carros 
            if name.lower() in carro.get('name', '').lower()
    ]
    if not lista_filtrada:
        return make_response(jsonify("Nome do carro não encontrado"), 404)
    return make_response(jsonify(lista_filtrada), 200)

@app.route('/carros/filtrar_carros/', methods=['POST'])
def filtrar_carros():
    filtros = request.get_json()
    if not filtros:
        return jsonify({"erro": "JSON de filtros ausente ou inválido"}), 400

    resultados = lista_carros
    for campo, valor in filtros.items():
        resultados = [carro for carro in resultados if str(carro.get(campo)) == str(valor)]

    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=True)
