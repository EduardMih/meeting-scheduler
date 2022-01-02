import psycopg2
from dbUtils.dbConnection import DbConnection


class MeetingPersonDAO:
    """
    Class to perform basic operations on meeting_person junction table: insert and select.
    """
    def __init__(self):
        """
        MeetingPersonDAO class constructor to initialize object and declare SQL statements.
        """
        self.insert_sql = """INSERT INTO meeting_person (meeting_id, person_id) VALUES (%s, %s)"""
        self.select_sql = """SELECT * FROM meeting_person WHERE meeting_id=%s"""

    def insert_meeting_person(self, meeting_id, person_id):
        """
        Method to insert a record in meeting_person table.

        :param meeting_id: Meeting id
        :param person_id: Person id
        :return: None
        """
        db_connection = DbConnection()

        try:
            connection = db_connection.get_connection()

            cursor = connection.cursor()
            cursor.execute(self.insert_sql, (meeting_id, person_id))
            connection.commit()

            cursor.close()
            db_connection.close_connection()
        except psycopg2.DatabaseError:
            raise

    def select_all_meeting_attendees(self, meeting_id):
        """
        Method to select all record with a meeting id, so the selected rows will contain all meeting's attendees id.

        :param meeting_id: Meeting id.
        :return: All attendees ids.
        """
        db_connection = DbConnection()

        try:
            connection = db_connection.get_connection()

            cursor = connection.cursor()
            cursor.execute(self.select_sql, (meeting_id, ))
            rows = cursor.fetchall()

            cursor.close()
            db_connection.close_connection()
        except Exception:
            raise

        else:

            return rows
