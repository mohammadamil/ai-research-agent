import sqlite3

def make_admin():
    # Connect to your local database
    conn = sqlite3.connect("ai_agent.db")
    cursor = conn.cursor()
    
    # Update all users to admin temporarily, or use a specific username/email filter if known
    # e.g., "UPDATE users SET role = 'admin' WHERE username = 'amil'"
    try:
        cursor.execute("UPDATE users SET role = 'admin'")
        conn.commit()
        print("Successfully updated database roles to admin!")
    except sqlite3.OperationalError as e:
        print(f"Error updating table: {e}. Please check your database table columns.")
    finally:
        conn.close()

if __name__ == "__main__":
    make_admin()