import unittest
from frijoles import app


class FrijolesAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_basic(self):
        res = self.app.get('/api/v1/')
        self.assertEqual(res.status_code, 200)
