from flask import Flask, request
from users import *
from recomendacao import getSimilares
app = Flask(__name__)

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
