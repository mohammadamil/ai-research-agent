from database.database import save_usage



def track_usage(username, action, topic=""):

    try:

        save_usage(
            username,
            action,
            topic
        )

        return True


    except Exception as e:

        print("Usage tracking error:", e)

        return False