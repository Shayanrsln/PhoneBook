import sqlite3

class Db():

    def __init__(self,path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
    
    def creat_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS contacts(id integer PRIMARY KEY, name text, phone text, email text, address text)")
        self.connection.commit()

    def close(self):
        self.connection.close()