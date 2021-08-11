import unittest
from grade import *
import sqlite3



class BookTest(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect('gradedb.sqlite')
        self.cursor= self.conn.cursor()
        self.grade = Grades()
    
    def test_file_save(self):
        result = self.grade.file_save()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertNotIsInstance(result, str)

    def test_read_all(self):
        result = self.grade.read_all()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertNotIsInstance(result, tuple)

    def test_update_grade_record(self):
        result = self.grade.update_grade_record('123-45-6789',50,50,50,50,50,'C')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertNotIsInstance(result, dict)

    def test_delete_grade_record(self):
        result = self.grade.delete_grade_record('123-45-6789')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertNotIsInstance(result, dict)

    def test_student_passed(self):
        result = self.grade.student_passed(8)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertNotIsInstance(result, str) 

    def test_failed_student(self):
        result = self.grade.failed_student(8)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertNotIsInstance(result, tuple) 

    def test_select_student_test1(self):
        result = self.grade.select_student_test1(8)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertNotIsInstance(result, str)    

    def tearDown(self):
        self.conn = None
        self.cursor= None
        self.book = None


if __name__ == '__main__':
    unittest.main()