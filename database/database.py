import sqlite3
from datetime import datetime


DB_NAME = "ai_agent.db"



def get_connection():

    conn = sqlite3.connect(
        DB_NAME,
        check_same_thread=False
    )

    return conn





def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()



    # USERS TABLE

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT UNIQUE,

        password TEXT,

        role TEXT DEFAULT 'user',

        created_at TEXT

    )
    """)



    # REPORTS TABLE

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        topic TEXT,

        report TEXT,

        pdf_file TEXT,

        excel_file TEXT,

        created_at TEXT

    )
    """)



    # USAGE TRACKING

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usage_tracking(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        action TEXT,

        topic TEXT,

        created_at TEXT

    )
    """)



    # CONVERSATION MEMORY

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversations(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id TEXT,

        role TEXT,

        message TEXT,

        created_at TEXT

    )
    """)



    conn.commit()

    conn.close()







# ---------------- USERS ----------------



def create_user(
        username,
        password,
        role="user"
):


    conn=get_connection()

    cursor=conn.cursor()


    try:


        cursor.execute(
        """
        INSERT INTO users
        (
        username,
        password,
        role,
        created_at
        )

        VALUES(?,?,?,?)

        """,

        (
        username,
        password,
        role,
        datetime.now().isoformat()
        )

        )


        conn.commit()


        return True


    except Exception as e:


        print(e)

        return False


    finally:


        conn.close()





def get_user(username):


    conn=get_connection()

    cursor=conn.cursor()


    cursor.execute(
    """
    SELECT
    username,
    password,
    role

    FROM users

    WHERE username=?

    """,

    (username,)

    )


    user=cursor.fetchone()


    conn.close()


    return user






def get_all_users():


    conn=get_connection()

    cursor=conn.cursor()


    cursor.execute(
    """
    SELECT
    username,
    role,
    created_at

    FROM users

    """
    )


    data=cursor.fetchall()


    conn.close()


    return data







# ---------------- REPORTS ----------------




def save_report(
        username,
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
    username,
    topic,
    report,
    pdf_file,
    excel_file,
    created_at
    )

    VALUES(?,?,?,?,?,?)

    """,

    (
    username,
    topic,
    report,
    pdf_file,
    excel_file,
    datetime.now().isoformat()
    )

    )


    conn.commit()

    conn.close()





def get_user_reports(username):


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

    WHERE username=?

    ORDER BY id DESC

    """,

    (username,)

    )


    reports=cursor.fetchall()


    conn.close()


    return reports






# Compatibility function

def get_reports(username=None):


    if username:

        return get_user_reports(username)



    conn=get_connection()

    cursor=conn.cursor()


    cursor.execute(
    """
    SELECT *

    FROM reports

    ORDER BY id DESC

    """
    )


    reports=cursor.fetchall()


    conn.close()


    return reports






def get_all_reports():


    conn=get_connection()

    cursor=conn.cursor()


    cursor.execute(
    """
    SELECT

    username,
    topic,
    created_at

    FROM reports

    ORDER BY id DESC

    """
    )


    reports=cursor.fetchall()


    conn.close()


    return reports







# ---------------- USAGE ----------------




def save_usage(
        username,
        action,
        topic=""
):


    conn=get_connection()

    cursor=conn.cursor()


    cursor.execute(
    """
    INSERT INTO usage_tracking

    (
    username,
    action,
    topic,
    created_at
    )

    VALUES(?,?,?,?)

    """,

    (
    username,
    action,
    topic,
    datetime.now().isoformat()
    )

    )


    conn.commit()

    conn.close()





def get_usage_count():


    conn=get_connection()

    cursor=conn.cursor()


    cursor.execute(
    """
    SELECT COUNT(*)

    FROM usage_tracking

    """
    )


    count=cursor.fetchone()[0]


    conn.close()


    return count






def get_total_users():


    conn=get_connection()

    cursor=conn.cursor()


    cursor.execute(
    """
    SELECT COUNT(*)

    FROM users

    """
    )


    count=cursor.fetchone()[0]


    conn.close()


    return count






def get_total_reports():


    conn=get_connection()

    cursor=conn.cursor()


    cursor.execute(
    """
    SELECT COUNT(*)

    FROM reports

    """
    )


    count=cursor.fetchone()[0]


    conn.close()


    return count







# ---------------- MEMORY ----------------




def save_message(
        user_id,
        role,
        message
):


    conn=get_connection()

    cursor=conn.cursor()


    cursor.execute(
    """
    INSERT INTO conversations

    (
    user_id,
    role,
    message,
    created_at
    )

    VALUES(?,?,?,?)

    """,

    (
    user_id,
    role,
    message,
    datetime.now().isoformat()
    )

    )


    conn.commit()

    conn.close()





def get_history(user_id):


    conn=get_connection()

    cursor=conn.cursor()


    cursor.execute(
    """
    SELECT

    role,
    message

    FROM conversations

    WHERE user_id=?

    ORDER BY id ASC

    """,

    (user_id,)

    )


    history=cursor.fetchall()


    conn.close()


    return history

# ---------------- ADMIN FUNCTIONS ----------------


def get_total_users():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    result = cursor.fetchone()[0]

    conn.close()

    return result





def get_total_reports():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM reports"
    )

    result = cursor.fetchone()[0]

    conn.close()

    return result





def get_usage_count():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM usage_tracking"
    )

    result = cursor.fetchone()[0]

    conn.close()

    return result





def get_all_users():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT username, role, created_at
        FROM users
        """
    )

    result = cursor.fetchall()

    conn.close()

    return result





def get_all_reports():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT username, topic, created_at
        FROM reports
        ORDER BY id DESC
        """
    )

    result = cursor.fetchall()

    conn.close()

    return result