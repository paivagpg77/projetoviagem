import sqlite3

class DBConnectionHandler:
    def __init__(self, db_path: str = "storage.db"):
        self.db_path = db_path
        self.__conn = None

    def connect(self):
        if self.__conn is None:
            self.__conn = sqlite3.connect(self.db_path)
        return self.__conn

    def get_connection(self):
        if self.__conn is None:
            raise Exception("Database not connected. Call connect() first.")
        return self.__conn

db_connection_handler = DBConnectionHandler()
