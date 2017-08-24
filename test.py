import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
