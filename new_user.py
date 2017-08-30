import json
import mongo


class User:
    def __init__(self):
        pass

    def params_user(self, data):

        key1 = 'username' in data
        key2 = 'password' in data
        if key1 == True and key2 == True and len(data)==2:
            return data
        else:
            return False

    def user(self, data):
        key1 = 'username' in data
        key2 = 'password' in data
        if key1 == True and key2 == True and len(data) == 2:
            return data
        else:
            return False

    def find_username(self, cookie):
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
