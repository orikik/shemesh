import json
import pymongo
from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client.sampleDB
collection = db.dataset

class User:
    def __init__(self):
        pass

    def new_user(self):
        data = json.loads(doc)
        login = data['name']
        if collection.find({"name": login}).count() > 0:
            print('this account active, choose another login')
            for men in collection.find():
                print(men)
        else:
            collection.save(data)
            for men in collection.find():
                print(men)

    def remove_user(self):
        data = json.loads(doc)
        login = data['name']
        if collection.find({"name": login}).count() > 0:
            collection.remove(data)
            for men in collection.find():
                print(men)

doc = json.dumps({
        'name': 'orikik',
        'password': '1234'
    })

User.new_user(doc)

User.new_user(doc)