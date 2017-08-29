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
    api_url = mongo.api_url + 'remove'

    def test_remove_post(self):
        f = requests.post(url=self.api_url, json=self.params)
        self.assertFalse(mongo.collection.find_one({"username": self.params['username']}))

    def test_remove_get(self):
        f = requests.get(url=self.api_url)
        self.assertFalse(mongo.collection.find_one({"username": self.params['username']}))

if __name__ == '__main__':
    unittest.main()
