from database.db import cursor,connection



def track_usage(username):


    cursor.execute(
    """
    SELECT queries FROM usage
    WHERE username=?
    """,
    (username,)
    )


    data = cursor.fetchone()


    if data:


        cursor.execute(
        """
        UPDATE usage
        SET queries=queries+1
        WHERE username=?
        """,
        (username,)
        )


    else:


        cursor.execute(
        """
        INSERT INTO usage
        VALUES(NULL,?,1)
        """,
        (username,)
        )


    connection.commit()