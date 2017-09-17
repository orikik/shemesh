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
    params_file0 = {
        'my_path': 'C:/work/shemesh/tests/test.txt',
        'storage_path': 'name0'
    }
    params_file1 = {
        'my_path': 'C:/work/shemesh/tests/test1.txt',
        'storage_path': 'name0'
    }
    params_file2 = {
        'my_path': 'C:/work/shemesh/tests/test.txt',
    }
    params_file3 = {
        'my_path': 'C:/work/shemesh/tests/test1.txt',
    }
    params_get0 = {
    }
    params_get1 = {
        "name": 'name0'
    }
    v = ['test.txt', 'test1.txt']
    x = ['test1.txt', 'test.txt']

    requests.post(url=mongo.api_url + 'registration', json=params)
    session = requests.Session()
    response = session.post(url=mongo.api_url + "login", json=params)
    c = response.cookies
    api_url = mongo.api_url + 'new_dir'

    def test_add_dirs(self):
        requests.post(url=self.api_url, cookies=self.c, json=self.params_dir0)
        requests.post(url=mongo.api_url + 'upload', cookies=self.c, json=self.params_file0)
        requests.post(url=mongo.api_url + 'upload', cookies=self.c, json=self.params_file1)
        requests.post(url=mongo.api_url + 'upload', cookies=self.c, json=self.params_file2)
        requests.post(url=mongo.api_url + 'upload', cookies=self.c, json=self.params_file3)
        n = requests.post(url=mongo.api_url + 'get_dir', cookies=self.c, json=self.params_get0)
        m = requests.post(url=mongo.api_url + 'get_dir', cookies=self.c, json=self.params_get1)
        self.assertTrue(n.text == '\n'.join(self.v) or n == '\n'.join(self.x))
        self.assertTrue(m.text == '\n'.join(self.v) or n == '\n'.join(self.x))
        requests.post(url=mongo.api_url + 'remove', json=self.params)


if __name__ == '__main__':
    unittest.main()
