import unittest
from models.user import User
from models.connection import Connect



class BookTest(unittest.TestCase):

    def setUp(self):
        self.conn = Connect.conn_psycopg2()
        self.cursor= self.conn.cursor()
        self.book = User()

    def test_all(self):
        result = self.book.all()
        self.assertIsInstance(result, list)
        self.assertNotIsInstance(result, str)
        self.assertIsNotNone(result)


    def tearDown(self):
        self.conn = None
        self.cursor= None
        self.book = None


if __name__ == '__main__':
    unittest.main()