import sqlite3
import os


DB_NAME = "ai_agent.db"


if not os.path.exists(DB_NAME):

    print("❌ Database file not found:", DB_NAME)

    exit()



conn = sqlite3.connect(DB_NAME)

cursor = conn.cursor()


# Check tables

cursor.execute(
    """
    SELECT name 
    FROM sqlite_master 
    WHERE type='table'
    """
)


tables = cursor.fetchall()


print("Existing tables:")

for table in tables:
    print(table[0])



if ("user",) not in tables:

    print("❌ users table does not exist")

else:

    cursor.execute(
        "DELETE FROM users"
    )

    conn.commit()

    print(
        "✅ All users deleted"
    )

    print(
        "First new user will become ADMIN"
    )


conn.close()