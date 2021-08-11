from connection import Connect
from datetime import datetime


class User(Connect):
    def __init__(self):
        self.connection = Connect().conn_ps()
        self.cursor = self.connection.cursor()
    
    def all(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()