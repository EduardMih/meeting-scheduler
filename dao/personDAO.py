from model.dbConnection import DbConnection


class PersonDAO:
    def __init__(self):
        self.insert_sql = """INSERT INTO persons (firstname, lastname) VALUES (%s, %s)"""
        self.select_sql = """SELECT * FROM persons WHERE firstname=%s AND lastname=%s"""

    def insert_person(self, firstname, lastname):
        db_connection = DbConnection()
        connection = db_connection.get_connection()

        cursor = connection.cursor()
        cursor.execute(self.insert_sql, (firstname, lastname))
        connection.commit()

        cursor.close()
        db_connection.close_connection()

    def select_person_by_firstname_and_lastname(self, firstname, lastname):
        db_connection = DbConnection()
        connection = db_connection.get_connection()

        cursor = connection.cursor()
        cursor.execute(self.select_sql, (firstname, lastname))
        row = cursor.fetchone()

        cursor.close()
        db_connection.close_connection()

        return row
