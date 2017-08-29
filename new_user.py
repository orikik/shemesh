import json
from tests import params
import requests
from flask import request
import mongo

doc = 1
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

for men in mongo.collection.find():
    print(men)

print('end \nstart')

api_url1 = mongo.api_url + 'login'
param = {
    'username': 'tes',
    'password': '1234'
}
param1 = {
    'username': 'tests',
    'password': '1256'
}



requests.post(url = mongo.api_url + "register" , json = param)
y = requests.post(url = mongo.api_url + "login", json = param)

for men in mongo.collection.find():
    print(men)

print('end \nstart')

session = requests.Session()
response = session.post(url = mongo.api_url + "login", json = param)
c = response.cookies
r = requests.get(url = mongo.api_url + "remove", cookies = c)


for men in mongo.collection.find():
    print(men)
