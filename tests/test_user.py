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
    
    # def test_get_by_userid(self):
    #     result = self.book.get_by_userid(4)
    #     self.assertIsNotNone(result)
    #     self.assertIsInstance(result, list)
    #     self.assertNotIsInstance(result, str)

    def test_get_by_userid(self):
        result = self.book.get_by_userid(4)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertNotIsInstance(result, str)

    def test_createnew_user_record(self):
        result = self.book.createnew_user_record('lexy','Lukubam','Omosare')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertNotIsInstance(result, list)

    def test_update_user_record(self):
        result = self.book.update_user_record('lexy','Lukubam','Omosare',4)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertNotIsInstance(result, tuple)

    def test_del_user_record(self):
        result = self.book.del_user_record(8)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertNotIsInstance(result, tuple)    

    def tearDown(self):
        self.conn = None
        self.cursor= None
        self.book = None


if __name__ == '__main__':
    unittest.main()

    def tearDown(self):
        self.conn = None
        self.cursor= None
        self.book = None


if __name__ == '__main__':
    unittest.main()