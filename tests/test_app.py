import unittest
from src.app import app

class TestApp(unittest.TestCase):

    def test_home(self):
        with app.test_client() as client: #use the imported app variable.
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'Hello, World!')

if __name__ == '__main__':
   unittest.main()