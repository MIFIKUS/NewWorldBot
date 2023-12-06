import mysql.connector

class Database:
    """Класс для работы с базой данных"""
    def __init__(self):
        # self.host = '192.168.0.125'
        self.host = '192.168.1.71'
        self.user = 'root'
        # self.password = 'BigBot'
        self.password = 'root'

        self.connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def make_query(self, query):
        """Функция для того чтобы сделать прямой запрос к базе данных"""
        self.cursor.execute(query)