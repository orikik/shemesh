import unittest
import requests
import mongo


class MyTestCase(unittest.TestCase):
    params = {
        'username': 'testing',
        'password': '1234'
    }
    params_wrong1 = {
        'userna': 'testing_wrong1',
        'passwo': '1234'
    }
    params_wrong2 = {
        'username': 'testing_wrong2',
        'password': '1234',
        'hellboy': 'yeah'
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

    def test_add_wrong(self):
        requests.post(url=self.api_url, json=self.params_wrong1)
        requests.post(url=self.api_url, json=self.params_wrong2)
        self.assertFalse(mongo.collection.find_one({"userna": self.params_wrong1['userna']}))
        self.assertFalse(mongo.collection.find_one({"username": self.params_wrong2['username']}))


if __name__ == '__main__':
    unittest.main()