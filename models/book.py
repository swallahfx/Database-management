from connection import Connect
from datetime import datetime

class Book:
    def __init__(self):
        self.connection= Connect().conn_psycopg2()
        self.cursor= self.connection.cursor()
    
    
    
    def get_all_users(self):
        try:
            self.cursor.execute("SELECT * FROM books")
            return self.cursor.fetchall()
        except Exception as err:
            print(str(err))
        finally:
            self.cursor.close()
        
            
    def get_by_user_id(self,user_id): # get table content with user id
        try:
            self.cursor.execute("SELECT name FROM books WHERE user_id=%s ", (user_id,))
            return self.cursor.fetchall()
        except Exception:
            return "User id not present in table 'Users' "
        finally:
            self.cursor.close()
        
    def create_newbook_record(self,user_id,name,pages): # userid(1-10), bookname, page_size
        try:
            self.cursor.execute(''' INSERT INTO books(user_id,name,pages)
                                    VALUES(%s,%s,%s)''',(user_id,name,pages))
            self.connection.commit()
            return "Record created"
        except Exception:
            return "User id not present in table 'Users' "
        finally:
            self.cursor.close()

    def get_by_bookid(self,num): #book_id
        try:
            self.cursor.execute("SELECT name FROM books WHERE id= %s ", (num,))
            return self.cursor.fetchall()
        except Exception as err:
            print(str(err))
        finally:
            self.cursor.close()
    def update_book_record(self,name,pages,id): #new bookname, pages, bookid_toupdate 
        try:
            updated_time=datetime.now()
            self.cursor.execute(''' UPDATE books
                                SET name=%s,pages=%s,updated_at=%s WHERE id = %s''',(name,pages,updated_time,id)
                                        
                                        )
            self.connection.commit()
            return "Record updated"
        except Exception as err:
            print(str(err))
        finally:
            self.cursor.close()

    def del_user_record(self,id):        #book id
        try:
            self.cursor.execute(''' DELETE FROM books
                                    WHERE id=%s''',(id,))
            self.connection.commit()     
            return "Rocord deleted"
        except Exception as err:
            print(str(err))
        finally:
            self.cursor.close()

if __name__ == '__main__':
    book = Book() 
    # print(book.get_all_users())
    # print(book.del_user_record(123))
    print(book.get_by_bookid(105))
    # print(book.update_book_record('tails of banshee',654, 126 ))
