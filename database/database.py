import sqlite3


DATABASE_NAME = "ai_agent.db"



def get_connection():

    return sqlite3.connect(DATABASE_NAME)





def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()


    # Users table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE,

        password TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)



    # Conversations

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id TEXT,

        role TEXT,

        message TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)



    # Reports

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id TEXT,

        topic TEXT,

        report TEXT,

        pdf_file TEXT,

        excel_file TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)



    conn.commit()

    conn.close()






def create_user(username,password):

    conn=get_connection()

    cursor=conn.cursor()


    try:

        cursor.execute(
        """
        INSERT INTO users(username,password)

        VALUES(?,?)

        """,

        (
            username,
            password
        ))


        conn.commit()

        result=True


    except sqlite3.IntegrityError:

        result=False



    conn.close()


    return result





def get_user(username):

    conn=get_connection()

    cursor=conn.cursor()


    cursor.execute(
    """
    SELECT username,password

    FROM users

    WHERE username=?

    """,

    (
        username,
    ))


    user=cursor.fetchone()


    conn.close()


    return user






def save_report(
        user_id,
        topic,
        report,
        pdf_file,
        excel_file
):

    conn=get_connection()

    cursor=conn.cursor()


    cursor.execute(
    """
    INSERT INTO reports

    (
    user_id,
    topic,
    report,
    pdf_file,
    excel_file
    )

    VALUES(?,?,?,?,?)

    """,

    (
        user_id,
        topic,
        report,
        pdf_file,
        excel_file
    ))


    conn.commit()

    conn.close()






def get_reports(user_id):

    conn=get_connection()

    cursor=conn.cursor()


    cursor.execute(
    """
    SELECT

    topic,
    pdf_file,
    excel_file,
    created_at


    FROM reports

    WHERE user_id=?


    ORDER BY id DESC

    """,

    (
        user_id,
    ))



    reports=cursor.fetchall()


    conn.close()


    return reports