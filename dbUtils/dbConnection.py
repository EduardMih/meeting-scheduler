import psycopg2
from psycopg2.extras import RealDictCursor


class DbConnection:
    connection = None

    def create_connection(self):
        try:
            self.connection = psycopg2.connect(
                database="meeting-scheduler2",
                user="postgres",
                password="postgres",
                cursor_factory=RealDictCursor
            )

        except psycopg2.DatabaseError as e:
            raise

    def get_connection(self):
        if not self.connection:
            self.create_connection()

        return self.connection

    def close_connection(self):
        self.connection.close()
