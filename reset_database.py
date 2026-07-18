import sqlite3
import os


DB_NAME = "ai_agent.db"


if not os.path.exists(DB_NAME):

    print("Database not found")

else:

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()


    cursor.execute(
        """
        DELETE FROM users
        """
    )


    conn.commit()

    conn.close()


    print("✅ All users deleted")