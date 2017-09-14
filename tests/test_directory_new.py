import unittest
import mongo
import requests


class MyTestCase(unittest.TestCase):
    params = {
        'username': 'testing',
        'password': '1234'
    }
    params_dir0 = {
        'name': 'name0'
    }
    params_dir1 = {
        'path': 'name0',
        'name': 'name1'
    }
    params_dir_wrong = {
        'path': 'wrong',
        'name': 'name2'
    }
    requests.post(url=mongo.api_url + 'registration', json=params)
    session = requests.Session()
    response = session.post(url=mongo.api_url + "login", json=params)
    c = response.cookies
    api_url = mongo.api_url + 'new_dir'

    def test_add_dirs(self):
        requests.post(url=self.api_url, cookies=self.c, json=self.params_dir0)
        requests.post(url=self.api_url, cookies=self.c, json=self.params_dir1)
        self.assertTrue(mongo.dir_collection.find_one({"name": self.params_dir0['name']}))
        self.assertTrue(mongo.dir_collection.find_one({"name": self.params_dir1['name'],
                                                       'path1': self.params_dir1['path']}))
        requests.post(url=mongo.api_url + 'remove', json=self.params)

    def test_add_wrond(self):
        requests.post(url=self.api_url, cookies=self.c, json=self.params_dir_wrong)
        self.assertFalse(mongo.dir_collection.find_one({"name": self.params_dir_wrong['name'],
                                                        'path1': self.params_dir_wrong['path']}))
        requests.post(url=mongo.api_url + 'remove', json=self.params)



if __name__ == '__main__':
    unittest.main()
