import sqlite3


connection = sqlite3.connect(
    "users.db",
    check_same_thread=False
)


cursor = connection.cursor()



def create_tables():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY,

        username TEXT UNIQUE,

        password TEXT

    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usage(

        id INTEGER PRIMARY KEY,

        username TEXT,

        queries INTEGER

    )
    """)


    connection.commit()