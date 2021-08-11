import psycopg2

class Connect:
    
    @classmethod
    def conn_psycopg2(self):
        connection=psycopg2.connect(
            host= 'localhost',
            database='postgres',
            user='postgres',
            password=1234,
            port= 5432
            
            
        )
        
        return connection