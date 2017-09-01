import json

import shutil

import dev_choice
import mongo


class User:
    def __init__(self):
        pass

    def params_user(self, data):#проверяет правильность вводимых данных при регистрации
        key1 = 'username' in data
        key2 = 'password' in data
        if key1 == True and key2 == True and len(data)==2:
            return data
        else:
            return False

    def user(self, data): #проверяет правильность вводимых данных для логина
        key1 = 'username' in data
        key2 = 'password' in data
        if key1 == True and key2 == True and len(data) == 2:
            return data
        else:
            return False

    def find_username(self, cookie):#ищет username
        if mongo.collection.find_one({'session': cookie}):
            n = mongo.collection.find_one({'session': cookie})
            return n['username']
        else:
            return 'You are not authorized'


#print(os.getcwd())
#os.mkdir(path = 'C:/work/shemesh/tests/tet')
#os.rmdir(path= 'C:/work/shemesh/tests/text')
data = {
        'username': 'testing',
        'password': '1234'
    }
params_file = {
    'username':'orik',
    'path':'C:/фотки/example.txt',
    'file_format':'.txt'
}
for men in mongo.collection.find():
    print(men)
for men in mongo.file_collection.find():
    print(men)
for men in mongo.dev_collection.find():
    print(men)
