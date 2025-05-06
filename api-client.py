import requests

BASE_URL = "http://127.0.0.1:5000"

def get_todos_carros():
    response = requests.get(f"{BASE_URL}/carros")
    print("GET /carros:", response.json())

def adicionar_carro(novo_carro):
    
    response = requests.post(f"{BASE_URL}/carros", json=novo_carro)
    print("POST /carros:", response.json())

def get_carro_por_id(id):
    response = requests.get(f"{BASE_URL}/carro/{id}")
    print(f"GET /carro/{id}:", response.json())

def atualizar_carro(id, carro_atualizado):
    
    response = requests.put(f"{BASE_URL}/carro/{id}", json=carro_atualizado)
    print(f"PUT /carro/{id}:", response.json())

def deletar_carro(id):
    response = requests.delete(f"{BASE_URL}/carro/{id}")
    print(f"DELETE /carro/{id}:", response.json())

def get_primeiros_n_carros(n):
    response = requests.get(f"{BASE_URL}/carros/{n}")
    print(f"GET /carros/{n}:", response.json())


def buscar_por_nome(nome):
    response = requests.get(f"{BASE_URL}/carros/{nome}")
    print(f"GET /carros/{nome}:", response.json())

def filtrar_carros(filtros):
    response = requests.post(f"{BASE_URL}/carros/filtrar_carros/", json=filtros)
    print("POST /carros/filtrar_carros:", response.json())


#get_todos_carros()
novo_carro = {
    "mpg": 22,
    "cylinders": 4,
    "displacement": 140,
    "horsepower": 90,
    "weight": 2400,
    "acceleration": 20,
    "model_year": 78,
    "origin": 1,
    "name": "chevrolet nova"
}
#adicionar_carro(novo_carro)
#get_carro_por_id(0)
  
carro_atualizado = {
    "mpg": 25,
    "cylinders": 4,
    "displacement": 120,
    "horsepower": 100,
    "weight": 2200,
    "acceleration": 18,
    "model_year": 79,
    "origin": 2,
    "name": "chevrolet atualizado"
}     
#atualizar_carro(0,carro_atualizado)        
#deletar_carro(0)          
#get_primeiros_n_carros(5)
#buscar_por_nome("mustang")
filtro = {
    "origin": 'usa',
    "weight": 3139,
}
filtrar_carros(filtro)
