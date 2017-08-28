from flask import request
from app import app
import mongo


@app.route('/addfile', methods=['GET', 'POST'])
def addfile():
    params = request.get_json()
    collection_name = params['']