import psycopg2
import sys


class DbConnection:
    def __init__(self):
        self.connection = None

    def create_connection(self):
        try:
            self.connection = psycopg2.connect(
                database="meeting-scheduler",
                user="postgres",
                password="postgres"
            )

        except psycopg2.DatabaseError as e:
            print(f'Error {e}')
            sys.exit(1)

        # finally:
            # if self.connection:
                # self.connection.close()

    def get_connection(self):
        if not self.connection:
            self.create_connection()

        return self.connection

    def close_connection(self):
        self.connection.close()
