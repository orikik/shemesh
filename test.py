import unittest
import requests
import mongo

class MyTestCase(unittest.TestCase):
    def test_something(self):
        api_url = "http://127.0.0.1:5000/register"
        params = {
            'username': 'testing',
            'password': '1234'
        }
        res = requests.get(api_url, params=params)
        params = {
            'username': 'testing',
            'password': '1234'
        }
        res = requests.get(api_url, params=params)
        self.assertTrue(mongo.collection.find({"username": params['username']}).count() == 1)


if __name__ == '__main__':
    unittest.main()
