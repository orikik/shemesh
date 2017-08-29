import unittest
import requests
import mongo


class MyTestCase(unittest.TestCase):
    params = {
        'username': 'testing',
        'password': '1234'
    }
    api_url = mongo.api_url + 'login'
    requests.post(url=mongo.api_url+'register', json=params)

    def test_login(self):
        f = requests.post(url= self.api_url, json=self.params)
        self.assertTrue(mongo.collection.find_one({"username": self.params['username'], "session": f.cookies['session']}))


if __name__ == '__main__':
    unittest.main()
