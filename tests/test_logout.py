import unittest
import requests
import mongo


class MyTestCase(unittest.TestCase):
    params = {
        'username': 'testing',
        'password': '1234'
    }
    requests.post(url=mongo.api_url + 'register', json=params)
    requests.post(url=mongo.api_url + 'login', json=params)
    api_url = mongo.api_url + 'logout'

    def test_logout(self):
        requests.get(url=mongo.api_url + 'logout')
        print(mongo.collection.find_one({"username": self.params['username']}))
        self.assertTrue(mongo.collection.find_one({"username": self.params['username'], "session" : {'$exists': True}}))
#Не работает!

if __name__ == '__main__':
    unittest.main()
