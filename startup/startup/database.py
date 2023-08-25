import pyodbc


class DatabaseManager:
    def __init__(self,
                 server="(localdb)\\MSSQLLocalDB;",
                 database="STARTUP;",
                 username="csadmin;",
                 password="CSroqkfwk!!"
                 ):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        if not self.connection:
            self.connection = pyodbc.connect(
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"UID={self.username};"
                f"PWD={self.password};"
            )
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def get_last_crawled_date(self):
        cursor = self.connect().cursor()
        cursor.execute("SELECT TOP 1 Date FROM NewsArticles ORDER BY CONVERT(DATETIME, REPLACE(REPLACE(REPLACE(Date, '년 ', '-'), '월 ', '-'), '일', '')) DESC;")
        last_date = cursor.fetchone()[0]
        cursor.close()
        return last_date
