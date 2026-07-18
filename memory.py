from database.database import get_connection



def save_message(user_id, role, message):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        INSERT INTO conversations
        (user_id, role, message)

        VALUES (?, ?, ?)
        """,

        (
            user_id,
            role,
            message
        )
    )


    conn.commit()

    conn.close()





def get_history(user_id):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute(
        """
        SELECT role,message

        FROM conversations

        WHERE user_id=?

        ORDER BY id ASC
        """,

        (
            user_id,
        )
    )


    rows = cursor.fetchall()


    conn.close()



    history=[]


    for row in rows:

        history.append({

            "role":row[0],

            "content":row[1]

        })


    return history