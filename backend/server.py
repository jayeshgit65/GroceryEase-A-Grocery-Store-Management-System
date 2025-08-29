# import the Flask library
from flask import Flask, json, request, jsonify
import products_dao
import orders_dao
import sql_connection
import uom_dau

# Create the Flask instance and pass the Flask
# constructor, the path of the correct module
app = Flask(__name__)


# Default route added using a decorator, for view function 'welcome'
# We pass a simple string to the frontend browser
# @app.route('/')
# def welcome():
#     return "Hello! How are you!"

connection = sql_connection.get_sql_connection()

@app.route("/getProducts", methods = ["GET"])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/getUOM", methods = ["GET"])
def get_uom():
    response = uom_dau.get_uoms(connection)
    response = jsonify(response)
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/insertProduct", methods=["POST"])
def insert_product():
    request_payload = json.loads(request.form["data"])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
    "product_id": product_id
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/insertOrder", methods = ["POST"])
def insert_order():
    request_payload = json.loads(request.form["data"])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        "order_id": order_id
    })
    response.header.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/deleteProduct",methods = ["POST"])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form["product_id"])
    response = jsonify({
        "product_id": return_id
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

# Start with flask web app, with debug as True,# only if this is the starting page
if(__name__ == "__main__"):
    app.run(port=5000, debug=True)