import unittest
import requests
import mongo



class MyTestCase(unittest.TestCase):
    params = {
        'username': 'testing',
        'password': '1234'
    }
    api_url = mongo.api_url + 'register'

    def test_add_first(self):
        requests.post(url = self.api_url , json = self.params)
        self.assertTrue(mongo.collection.find_one({"username": self.params['username']}))

    def test_add_similar(self):
        requests.post(url = self.api_url , json = self.params)
        requests.post(url = self.api_url , json = self.params)
        a = mongo.collection.find({"username": self.params['username']}).count()
        self.assertEqual(a, 1)

if __name__ == '__main__':
    unittest.main()