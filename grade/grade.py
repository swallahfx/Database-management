import sqlite3, csv
class Grades:
    def __init__(self):
        self.conn = sqlite3.connect('gradedb.sqlite')
        self.cur = self.conn.cursor()

    def create_sqlite(self):
        sql = """
            CREATE TABLE IF NOT EXISTS grades(
                id SERIAL PRIMARY KEY,
                last_name VARCHAR(50),
                first_name VARCHAR(50),
                SSN VARCHAR,
                test1 NUMERIC,
                test2 NUMERIC,
                test3 NUMERIC,
                test4 NUMERIC,
                final NUMERIC,
                grade VARCHAR(50) 
            )
          """
        
        self.conn.execute(sql)
        self.conn.commit()
    
    def file_save(self):
        file_path = '/Users/decagon/Desktop/6th-week/week-6-assignment-swallahfx/grade/grades.csv'
        with open(file_path,'r') as fin: 
            grade_file = csv.DictReader(fin) 
            to_database = [(i['last_name'], i['first_name'],i['SSN'],i['Test1'],
                      i['Test2'],i['Test3'],i['Test4'],i['Final'],i['Grade']) for i in grade_file]
            return to_database

    def insert_to_table(self):
    
            self.cur.executemany('''INSERT INTO grades ('last_name', 
                             'first_name', SSN, Test1, Test2, Test3, Test4, Final, Grade) 
                             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);''',self.file_save())
            self.conn.commit()
            

    def create_new_record(self,first_name,last_name,ssn,test1,test2,test3,test4,final,grade):
        self.cur.execute("""INSERT INTO grades('last_name','first_name',SSN,test1,test2,test3,test4,test5,final,grade)
             VALUES(%s,%s,%s,%s,%s,%s%s,%s,%s,%s);""", (first_name,last_name,ssn,test1,test2,test3,test4,final,grade))
        self.conn.commit()
        
    
    def read_all(self):
        self.cur.execute("SELECT * FROM grades")
        print(self.cur.execute("SELECT * FROM grades"))
        record = self.cur.fetchall()
        return record

    def update_grade_record(self,ssn,test1,test2,test3,test4,final,grade):
        self.cur.execute("""UPDATE grades SET 'first name'=%s,SSN=%s, 
                test1=%s,test2=%s,test3=%s,test4=%s,final=%s,grade=%s
                WHERE ssn=?
                """,(ssn,test1,test2,test3,test4,final,grade))

        self.conn.commit()
        return 'Records updated successfully'
    
    def delete_grade_record(self, ssn):
        self.cur.execute('DELETE FROM users WHERE ssn=%s', (ssn,))
        self.conn.commit()
        return "deletion completed"

    def student_passed(self):
        self.cur.execute("SELECT * FROM grades WHERE final >= 50 ")
        return self.cur.fetchall()
         
    
    def failed_student(self):
        self.cur.execute("SELECT * FROM grades WHERE final < 50")
        record = self.cur.fetchall()
        return record
    
    def select_student_test1(self):
        self.cur.execute("SELECT * FROM grades WHERE test1 > 45")
        record = self.cur.fetchall()
        return record



if __name__ == '__main__':      
    user_one = Grades()
    # user_one.create_sqlite()
    # user_one.insert_to_table()



    # print(user_one.read_all())

    # print(user_one.student_passed())
    # print(user_one.failed_student())
    print(user_one.select_student_test1())
