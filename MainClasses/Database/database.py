import mysql.connector

#host = '192.168.0.125'
host = '192.168.1.71'
user = 'root'
#password = 'BigBot'
password = 'root'

connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
connection.autocommit = True

cursor = self.connection.cursor()

def make_query(query):
   """Функция для того чтобы сделать прямой запрос к базе данных"""
   cursor.execute(query)