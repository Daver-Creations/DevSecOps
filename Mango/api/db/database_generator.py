import sqlite3

def connect():
    connection = sqlite3.connect('mango.db')
    return connection

def init_db():
    connection = connect()
    cursor = connection.cursor()

    query = f""" CREATE TABLE IF NOT EXISTS sessions (
                session_id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER,
                start_time DATETIME,
                end_time DATETIME,
                location TEXT
            )"""

    cursor.execute(query)
    connection.commit()
    connection.close()

def get_sessions_by_user(client_id):
    connection = connect()
    cursor = connection.cursor()

    query = f""" SELECT * FROM sessions WHERE client_id = {client_id}"""

    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

def insert_start_time(client_id, start_time, location):
    connection = connect()
    cursor = connection.cursor()

    query = f""" insert into sessions(client_id, start_time, location) values({client_id}, "{start_time}", "{location}")"""

    cursor.execute(query)
    connection.commit()
    connection.close()

def insert_end_time(client_id, end_time):
    connection = connect()
    cursor = connection.cursor()

    query = f"""
        update sessions
        set end_time = "{end_time}"
        where client_id = {client_id}
    """

    cursor.execute(query)
    connection.commit()
    connection.close()