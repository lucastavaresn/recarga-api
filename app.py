from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def list_companies():
    
    return companies_data()

@app.route('/buy/product/<string:product_id>/number/<int:client_number>')
def make_recharge(product_id, client_number):
    companies = companies_data()
    print(companies)
    if not is_valid(client_number):
        return {
            "error": "Number isn't valid"
        }

    for company in companies:
        for product in company['products']:
            if product_id == product['id']:
                return build_recharge(client_number, product["value"], product_id)
    return {
        "error": "Product id not found"
    }

def companies_data():
    with open('db.json') as file:
        data = json.load(file)
    return data

def is_valid(client_number):
    number = str(client_number) 
    if len(number) == 11:
        return True
    return False

def build_recharge(client_number, value, product_id):

    return {
        "phone_number": client_number,
        "price": value,
        "product_id": product_id
    }


if __name__ == '__main__':
    app.run(debug=True)
