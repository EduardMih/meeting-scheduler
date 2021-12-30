import psycopg2
from model.dbConnection import DbConnection
from exception.exceptions import *


class PersonDAO:
    """
    Class responsible for performing basic operations on person table: insert, select by firstname and lastname,
    select by id.
    """
    def __init__(self):
        """
        PersonDAO class constructor to initialize the object and declare SQL statements.
        """
        self.insert_sql = """INSERT INTO persons (firstname, lastname) VALUES (%s, %s)"""
        self.select_sql_by_firstname_and_lastname = """SELECT * FROM persons WHERE firstname=%s AND lastname=%s"""
        self.select_sql_by_id = """SELECT * FROM persons WHERE id=%s"""

    def insert_person(self, firstname, lastname):
        """
        Method to insert a person in person table.

        :param firstname: Person's firstname.
        :param lastname: Person's lastname
        :return: None
        """
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
        """
        Method to select a person by firstname and lastname.

        :param firstname: Person's firstname.
        :param lastname: Person's lastname.
        :return: Selected person.
        """
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
        """
        Method to select person by id.

        :param person_id: Person's id.
        :return: Selected person.
        """
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

