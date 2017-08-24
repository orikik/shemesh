from flask import request

from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registers the user."""
    username = request.get_json()

    return username['username']+username['password']


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Registers the user."""
    username = request.get_json()

    return username['username']+username['password']