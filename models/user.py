from connection import Connect
from datetime import datetime


class User(Connect):
    def __init__(self):
        self.connection = Connect().conn_ps()
        self.cursor = self.connection.cursor()
    
    def all(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()
    
    def get_by_userid(self,id):
        
        self.cursor.execute("SELECT * FROM users WHERE id=%s ", (id,))
        return self.cursor.fetchall()
    
    def createnew_user_record(self,username,first_name,last_name):
       
            self.cursor.execute(''' INSERT INTO users(username,first_name,last_name)
                                VALUES(%s,%s,%s)''',(username,first_name,last_name))
            self.connection.commit()
            return "Record created"
        
    def update_user_record(self,username,first_name,last_name,id):
        update_time=datetime.now()

        self.cursor.execute(''' UPDATE users
                                    SET username=%s,first_name=%s,last_name=%s,updated_at=%s WHERE id = %s''',
                                    (username,first_name,last_name,update_time,id)
                                    
                                    )
        self.connection.commit()
        return "Record updated"
    
    def del_user_record(self,id):        
            self.cursor.execute(''' DELETE FROM users
                                    WHERE id=%s''',(id,))
            self.connection.commit()    
            return "Record deleted" 
if __name__ == '__main__':  
    user = User()
    #print(user.all())
    #print(user.get_by_userid(4))
    #print(user.createnew_user_record('moshly', 'Moshood', 'Salawudeen'))
    #print(user.update_user_record('folukx', 'Foluke', 'Akpobasa', 1))