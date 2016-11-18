import unittest

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_db(self):
        rv = self.app.get('/')
        print(type(rv))
        print(rv)
        # assert b'No entries here so far' in rv.data


if __name__ == '__main__':
    unittest.main()