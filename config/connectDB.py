import mysql.connector
import sqlalchemy
from mysql.connector import Error

def connect_mysql_db():
    try:
        connect = mysql.connector.connect(host='localhost', database='py_stkex', user='root', password='root')
        if connect.is_connected():
            print('Connected to MySQL database')
            return connect

    except Error as e:
        print(e)


def connect_db_sqlalchemy():
    DATABSE_URI = "mysql+mysqlconnector://root:root@localhost/py_stkex"
    DATABSE_URI.format(user='root', password='root', server='localhost', database='py_stkex')
    try:
        engine = sqlalchemy.create_engine(DATABSE_URI)
        if (engine != None):
            print('Connected to MySQL database by sqlalchemy')
            return engine

    except Error as e:
        print(e)