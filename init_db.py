from database.database import engine,Base
from database.models import User,Report


Base.metadata.create_all(
    bind=engine
)


print("Database Created")