import mysql.connector as mysql


class DatabaseConnector:
    connection = None

    @classmethod
    def connect(cls):
        db_connetion = mysql.connect(
            host="localhost",
            port=3306,
            database="pipeline_db",
            user="root",
            passwd="rickandmorty"
        )
        cls.connection = db_connetion
