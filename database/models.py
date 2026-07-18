from sqlalchemy import Column,Integer,String,Text,DateTime
from datetime import datetime

from database.database import Base



class User(Base):

    __tablename__="users"


    id = Column(
        Integer,
        primary_key=True
    )


    username = Column(
        String,
        unique=True
    )


    password = Column(
        String
    )



class Report(Base):

    __tablename__="reports"


    id = Column(
        Integer,
        primary_key=True
    )


    username = Column(
        String
    )


    topic = Column(
        String
    )


    content = Column(
        Text
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )