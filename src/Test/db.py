# https://www.datacamp.com/tutorial/tutorial-postgresql-python
import psycopg2

#### ehck for connecting to Trino: https://github.com/trinodb/trino-python-client

## postgres
def connection():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command
    cur.execute('SELECT * FROM Persons;')

    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)

connection()
