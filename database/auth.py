import bcrypt

from database.db import connection,cursor



def signup(username,password):


    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )


    cursor.execute(
    """
    INSERT INTO users
    VALUES(NULL,?,?)
    """,
    (
        username,
        hashed
    )
    )


    connection.commit()



def login(username,password):


    cursor.execute(
    """
    SELECT password FROM users
    WHERE username=?
    """,
    (username,)
    )


    result = cursor.fetchone()


    if result:

        return bcrypt.checkpw(
            password.encode(),
            result[0]
        )


    return False