import unittest
from  app import app

class TestApp(unittest.TestCase):
    def test_home(self):
        response = app.test_client().get('/')
        self.assertEqual(response.data,b'Hello, World!')

if __name__ == "__main__":
    unittest.main()