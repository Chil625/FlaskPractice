from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        'name': 'Amazon',
        'items': [
            {
                'name': 'Chil',
                'price': 19.19
            }
            # },
            # {
            #     'name': 'Rei',
            #     'price': 114.514
            # }
        ]
    }
]


@app.route("/")
def home():
    return render_template("index.html")


# @app.route('/')
# def home():
#     return "Ayako-chan!"

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    # Iterate over stores
    for store in stores:
        if store["name"] == name:
            # if the store name matches, return it
            return jsonify(store)
        else:
            # if none match, return an error message
            return jsonify({"message": "There is no store like {}".format(name)})


# GET /store
@app.route('/store/')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    # is_there_the_store = False
    # 1回目のreturnが実行されると2回目は実行されないので不要

    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"]
            }
            store["items"].append(new_item)
            # is_there_the_store = True
            return jsonify(new_item)
    #    if is_there_the_store == False:
    return jsonify({"message": "There is no store like {}".format(name)})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    # is_there_the_store = False
    for store in stores:
        if store["name"] == name:
            # is_there_the_store = True
            return jsonify({"items": store["items"]})
    # if is_there_the_store == False:
    return jsonify({"message": "There is no store like {}".format(name)})


app.run(port=5000)
