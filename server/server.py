from flask import Flask, request

app = Flask(__name__)
PRODUCTS = [
    {"id": "2", "name": "Product", "desc": "Product teste"},
    {"id": "3", "name": "Product2", "desc": "Product teste 2"}
]
@app.route('/')
def home():
    return {'data': 'Hello world'}


@app.route('/products/')
def get_all_products():
    return {'data': PRODUCTS}

@app.route('/products/', methods=['POST'])
def add_product():
    p = request.get_json()
    PRODUCTS.append(p)
    return {'data': p}

@app.route('/products/<id>')
def get_product(id):
    for prod in PRODUCTS:
        if prod['id'] == id:
            return {'data': prod}
    return {'data': "NOT FOUND"}

@app.route('/products/<id>', methods=['DELETE'])
def del_product(id):
    for prod in PRODUCTS:
        if prod['id'] == id:
            PRODUCTS.remove(prod)
            return {'data': prod}
    return {'data': "NOT FOUND"}

if __name__ == "__main__":
    app.run(port=5000, debug=True)