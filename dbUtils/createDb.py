import psycopg2
from dbUtils.dbConnection import DbConnection


def create_tables():
    commands = (
        """
        CREATE TABLE meetings (
        id SERIAL PRIMARY KEY,
        title VARCHAR(50),
        start_date TIMESTAMPTZ,
        end_date TIMESTAMPTZ
        )
        """,
        """
        CREATE TABLE persons (
        id SERIAL PRIMARY KEY,
        firstname VARCHAR(50),
        lastname VARCHAR(50),
        UNIQUE(firstname, lastname)
        )
        """,
        """
        CREATE TABLE meeting_person (
        id SERIAL PRIMARY KEY,
        meeting_id INTEGER,
        person_id INTEGER,
        UNIQUE(person_id, meeting_id),
        FOREIGN KEY (meeting_id)
        REFERENCES meetings (id),
        FOREIGN KEY (person_id)
        REFERENCES persons (id)
        )
        """
    )

    try:
        db = DbConnection()
        conn = db.get_connection()

        cur = conn.cursor()

        for command in commands:
           cur.execute(command)

        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


create_tables()
