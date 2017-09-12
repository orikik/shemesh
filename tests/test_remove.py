import unittest
import requests
import mongo


class MyTestCase(unittest.TestCase):
    params = {
        'username': 'testing',
        'password': '1234'
    }
    requests.post(url=mongo.api_url + 'register', json=params)
    api_url = mongo.api_url + 'remove'

    def test_remove_post(self):
        requests.post(url=mongo.api_url + 'login', json=self.params)
        requests.post(url=self.api_url, json=self.params)
        self.assertFalse(mongo.collection.find_one({"username": self.params['username']}))

    def test_remove_get(self):
        session = requests.Session()
        response = session.post(url=mongo.api_url + "login", json=self.params)
        c = response.cookies
        requests.get(url=mongo.api_url + "remove", cookies=c)
        self.assertFalse(mongo.collection.find_one({"username": self.params['username']}))

if __name__ == '__main__':
    unittest.main()
