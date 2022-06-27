from flask import Flask, request
from users import *
from recomendacao import getSimilares
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return {"version": 1.0}

@app.route('/similar', methods=['POST'])
def similar():
    user = request.json()["id"]
    users = getUsersInteresses()
    return {"similares": getSimilares(users, user)}

@app.route('/dadosUsers', methods=['GET'])
def dadosUsers():
    return getUsers()

if __name__ == '__main__':
    app.run()
