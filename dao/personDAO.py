import psycopg2
from model.dbConnection import DbConnection
from exception.exceptions import *


class PersonDAO:
    def __init__(self):
        self.insert_sql = """INSERT INTO persons (firstname, lastname) VALUES (%s, %s)"""
        self.select_sql_by_firstname_and_lastname = """SELECT * FROM persons WHERE firstname=%s AND lastname=%s"""
        self.select_sql_by_id = """SELECT * FROM persons WHERE id=%s"""

    def insert_person(self, firstname, lastname):
        db_connection = DbConnection()

        try:
            connection = db_connection.get_connection()

            cursor = connection.cursor()
            cursor.execute(self.insert_sql, (firstname, lastname))
            connection.commit()

            cursor.close()
            db_connection.close_connection()
        except psycopg2.DatabaseError as e:
            if e.pgcode == '23505':
                raise PersonExists

            else:

                raise

    def select_person_by_firstname_and_lastname(self, firstname, lastname):
        db_connection = DbConnection()

        try:
            connection = db_connection.get_connection()

            cursor = connection.cursor()
            cursor.execute(self.select_sql_by_firstname_and_lastname, (firstname, lastname))
            row = cursor.fetchone()

            cursor.close()
            db_connection.close_connection()
        except Exception:
            raise

        else:

            return row

    def select_person_by_id(self, person_id):
        db_connection = DbConnection()

        try:
            connection = db_connection.get_connection()

            cursor = connection.cursor()
            cursor.execute(self.select_sql_by_id, (person_id, ))
            row = cursor.fetchone()

            cursor.close()
            db_connection.close_connection()
        except Exception:
            raise

        else:

            return row

