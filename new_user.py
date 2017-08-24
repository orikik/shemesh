import json
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
