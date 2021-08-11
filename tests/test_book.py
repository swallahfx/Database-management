import unittest
from models.book import Book
from models.connection import Connect



class BookTest(unittest.TestCase):

    def setUp(self):
        self.conn = Connect.conn_psycopg2()
        self.cursor= self.conn.cursor()
        self.book = Book()

    def test_get_all_users(self):
        result = self.book.get_all_users()
        self.assertIsInstance(result, list)
        self.assertNotIsInstance(result, str)
        self.assertIsNotNone(result)
        # self.assertNotEqual(bool(result), True)
    
    def test_get_by_user_id(self):
        result = self.book.get_by_user_id(103)
        self.assertIsNotNone(result)
        # self.assertNotEqual(bool(result), True)
        self.assertIsInstance(result, list)
        self.assertNotIsInstance(result, str)

    def test_create_newbook_record(self):
        result = self.book.create_newbook_record(1,'The spirit meets', 435)
        self.assertIsNotNone(result)
        # self.assertEqual(bool(result), False)
        self.assertIsInstance(result, str)
        self.assertNotIsInstance(result, list)

    def test_get_by_bookid(self):
        result = self.book.get_by_bookid(104)
        self.assertIsNotNone(result)
        # self.assertEqual(bool(result), False)
        self.assertIsInstance(result, list)
        self.assertNotIsInstance(result, tuple)

    def test_update_book_record(self):
        result = self.book.update_book_record('tails of mukkel', 544, 109)
        self.assertIsNotNone(result)
        # self.assertEqual(bool(result), False)
        self.assertIsInstance(result, str)
        self.assertNotIsInstance(result, tuple)

    def test_del_user_record(self):
        result = self.book.del_user_record(109)
        self.assertIsNotNone(result)
        # self.assertEqual(bool(result), False)
        self.assertIsInstance(result, str)
        self.assertNotIsInstance(result, tuple)
        
        

    def tearDown(self):
        self.conn = None
        self.cursor= None
        self.book = None


if __name__ == '__main__':
    unittest.main()