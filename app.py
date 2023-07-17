import sqlite3
import json
from flask import Flask, request, render_template
from crud import *
from models import *

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/inventory/add', methods=['POST'])
def additem():
    user = request.json

    print(user)

    if 'username' not in user or 'item' not in user:
        return('Incorrect Request', 400)
    
    username = user['username']
    item = Item(user['item']['name'], user['item']['description'])

    inventory = add_item(username, item)

    return(inventory, 200)



@app.route('/inventory/remove', methods=['POST'])
def delete():
    user = request.json

    print(user)

    if 'username' not in user or 'itemname' not in user:
        return('Incorrect Request', 400)
    
    username = user['username']
    itemname = user['itemname']
    
    inventory = remove_item(username, itemname)

    if inventory is not None:
        return(inventory, 200)
    else:
        return('Item not found')
    


@app.route('/login', methods=['POST'])
def login():
    user = request.json

    print(user)

    if 'username' not in user:
        return('Incorrect Request', 400)
    
    username = user['username']

    user = get_user(username)[0]

    return(user, 200)


@app.route('/create', methods=['POST'])
def create():
    user = request.json

    print(user)

    if 'username' not in user:
        return('Incorrect Request', 400)
    
    username = create_user(user['username'])

    return(f'Created account with username: {username}', 200)
        

if __name__ == "__main__":
    app.run(debug=True)