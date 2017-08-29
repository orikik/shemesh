import json
from tests import params
import requests
from flask import request

import mongo

class User:
    def __init__(self):
        pass

    def new_user(self):
        data = json.loads(doc)
        login = data['username']
        if mongo.collection.find({"username": login}).count() > 0:
            print('this account active, choose another login')
            for men in mongo.collection.find():
                print(men)
        else:
            mongo.collection.save(data)
            for men in mongo.collection.find():
                print(men)

    def remove_user(self):
        data = json.loads(doc)
        login = data['username']
        if mongo.collection.find({"username": login}).count() > 0:
            mongo.collection.remove(data)
            for men in mongo.collection.find():
                print(men)

doc = json.dumps({
        'username': 'orikik',
        'password': '1234'
    })


for men in mongo.collection.find():
    print(men)

print('end \nstart')

api_url1 = mongo.api_url + 'login'
param = {
    'username': 'tes',
    'password': '1234'
}
requests.post(url = mongo.api_url + "register" , json = param)
y = requests.post(url = mongo.api_url + "login", json = param)
for men in mongo.collection.find():
    print(men)
requests.get(url = mongo.api_url + "remove", params= y.cookies)

for men in mongo.collection.find():
    print(men)

if mongo.collection.find_one({"username": 'orik', "session" : {'$exists': False}}):
    print('yes')
else:
    print('no')
