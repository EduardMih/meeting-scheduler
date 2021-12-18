import psycopg2
from model.dbConnection import DbConnection


class MeetingPersonDAO:
    def __init__(self):
        self.insert_sql = """INSERT INTO meeting_person (meeting_id, person_id) VALUES (%s, %s)"""
        self.select_sql = """SELECT * FROM meetings WHERE star_date >= %s AND end_date <= %s"""

    def insert_meeting_person(self, meeting_id, person_id):
        db_connection = DbConnection()

        try:
            connection = db_connection.get_connection()

            cursor = connection.cursor()
            cursor.execute(self.insert_sql, (meeting_id, person_id))
            connection.commit()

            cursor.close()
            db_connection.close_connection()
        except psycopg2.DatabaseError as e:
            raise
