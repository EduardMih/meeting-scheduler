import psycopg2
from model.dbConnection import DbConnection


class MeetingDAO:
    def __init__(self):
        self.insert_sql = """INSERT INTO meetings (start_date, end_date) VALUES (%s, %s) RETURNING id"""
        self.select_sql = """SELECT * FROM meetings WHERE start_date >= %s AND end_date <= %s"""

    def insert_meeting(self, start_date, end_date):
        db_connection = DbConnection()

        try:
            connection = db_connection.get_connection()

            cursor = connection.cursor()
            cursor.execute(self.insert_sql, (start_date, end_date))
            meeting_id = cursor.fetchone()[0]
            connection.commit()

            cursor.close()
            db_connection.close_connection()
        except psycopg2.DatabaseError as e:
            raise

        else:

            return meeting_id

    def filter_meetings_by_date(self, start_date, end_date):
        db_connection = DbConnection()

        try:
            connection = db_connection.get_connection()

            cursor = connection.cursor()
            cursor.execute(self.select_sql, (start_date, end_date))
            rows = cursor.fetchall()

            cursor.close()
            db_connection.close_connection()
        except Exception:
            raise

        else:

            return rows

