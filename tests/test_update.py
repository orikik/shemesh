import unittest
import requests
import mongo


class MyTestCase(unittest.TestCase):
    params = {
        'username': 'testing',
        'password': '1234'
    }
    requests.post(url=mongo.api_url + 'register', json=params)
    api_url = mongo.api_url + 'update'

    def test_update(self):
        params = {
            'username': 'test',
            'password': '1256'
        }
        session = requests.Session()
        response = session.post(url=mongo.api_url + "login", json=self.params)
        c = response.cookies
        requests.post(url=mongo.api_url + "update", cookies=c, json=params)
        self.assertFalse(mongo.collection.find_one({"username": self.params['username'], "password": self.params['password']}))
        self.assertTrue(mongo.collection.find_one({"username": params['username'], "password": params['password']}))


if __name__ == '__main__':
    unittest.main()
