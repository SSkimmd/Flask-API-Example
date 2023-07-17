import sqlite3
import json
from app import get_db
from flask import Flask, request


def get_user(username):
    conn = get_db()

    query = 'SELECT * FROM users WHERE username = ?'
    data = (username,)
    user = conn.execute(query, data)

    result = [dict(row) for row in user.fetchall()]

    if user is None:
        return('', 400)
    return result


def create_user(username):
    inventory = ""

    conn = get_db()
    conn.execute('INSERT INTO users (username, inventory) VALUES (?, ?)',
                        (username, inventory))
    conn.commit()
    conn.close()

    return username


def remove_item(username, itemname):
    user = get_user(username)[0]
    conn = get_db()

    if user['inventory'] == '':
        return
    
    inventory = json.loads(user['inventory'])

    for item in inventory:
        if item['name'] == itemname:
            inventory.remove(item)    

    inventory = json.dumps(inventory)

    query = 'UPDATE users SET inventory = ? WHERE username = ?'
    data = (inventory, username)
    conn.execute(query, data)
    
    conn.commit()
    conn.close()  

    return inventory


def add_item(username, item):
    user = get_user(username)[0]
    conn = get_db()

    if user['inventory'] != '':
        tinventory = json.loads(user['inventory'])
        tinventory.append(item)
        inventory = json.dumps(tinventory)
    else:
        inventory = json.dumps([item])

    query = 'UPDATE users SET inventory = ? WHERE username = ?'
    data = (inventory, username)
    conn.execute(query, data)
    
    conn.commit()
    conn.close()

    return inventory