import streamlit as st
from database.database import get_connection

st.set_page_config(
    page_title="Reset Database",
    page_icon="⚠️"
)

st.title("⚠️ Database Reset Tool")

st.warning(
    "This will permanently delete ALL users, reports, conversations, and usage data."
)

confirm = st.checkbox("I understand that this action cannot be undone.")

if confirm:
    if st.button("🗑 Delete Everything"):

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("DELETE FROM users")
            cursor.execute("DELETE FROM reports")
            cursor.execute("DELETE FROM conversations")
            cursor.execute("DELETE FROM usage_tracking")

            conn.commit()

            st.success("✅ Database has been cleared successfully.")
            st.info("You can now register a new admin account.")

        except Exception as e:
            st.error(f"Error: {e}")

        finally:
            conn.close()