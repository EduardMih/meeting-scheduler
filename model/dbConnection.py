import psycopg2
from psycopg2.extras import RealDictCursor


class DbConnection:
    def __init__(self):
        self.connection = None

    def create_connection(self):
        try:
            self.connection = psycopg2.connect(
                database="meeting-scheduler",
                user="postgres",
                password="postgres",
                cursor_factory=RealDictCursor
            )

        except psycopg2.DatabaseError as e:
            #print(f'Error {e}')
            #sys.exit(1)
            raise

        # finally:
            # if self.connection:
                # self.connection.close()

    def get_connection(self):
        if not self.connection:
            self.create_connection()

        return self.connection

    def close_connection(self):
        self.connection.close()
