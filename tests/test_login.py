import unittest
import requests
import mongo


class MyTestCase(unittest.TestCase):
    params = {
        'username': 'testing',
        'password': '1234'
    }
    api_url = mongo.api_url + 'login'


    def test_login(self):
        requests.post(url=mongo.api_url + 'registration', json=self.params)
        f = requests.post(url= self.api_url, json=self.params)
        self.assertTrue(mongo.collection.find_one({"username": self.params['username'], "session": f.cookies['session']}))
        requests.post(url=mongo.api_url + 'remove',json=self.params)


if __name__ == '__main__':
    unittest.main()
