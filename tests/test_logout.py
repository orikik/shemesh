import unittest
import requests
import mongo


class MyTestCase(unittest.TestCase):
    params = {
        'username': 'testing',
        'password': '1234'
    }
    requests.post(url=mongo.api_url + 'registration', json=params)
    api_url = mongo.api_url + 'logout'

    def test_logout(self):
        session = requests.Session()
        response = session.post(url=mongo.api_url + "login", json=self.params)
        c = response.cookies
        requests.get(url=self.api_url, cookies=c)
        self.assertTrue(mongo.collection.find_one({"username": self.params['username'], "session" : {'$exists': False}}))
        requests.post(url=mongo.api_url + 'remove', json=self.params)

if __name__ == '__main__':
    unittest.main()
