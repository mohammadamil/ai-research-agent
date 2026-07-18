from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database.database import SessionLocal
from database.models import User, Report

from auth.security import hash_password, verify_password

from agent import run_agent


app = FastAPI(
    title="AI Research SaaS API"
)



# Database dependency

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@app.get("/")
def home():

    return {
        "status":"AI Research SaaS API Running"
    }



# -------------------------
# Register User
# -------------------------

@app.post("/register")
def register(
    username:str,
    password:str,
    db:Session=Depends(get_db)
):


    existing = db.query(User).filter(
        User.username == username
    ).first()


    if existing:

        return {
            "message":"User already exists"
        }



    user = User(

        username=username,

        password=hash_password(password)

    )


    db.add(user)

    db.commit()


    return {

        "message":"User created successfully"

    }



# -------------------------
# Login
# -------------------------

@app.post("/login")
def login(

    username:str,

    password:str,

    db:Session=Depends(get_db)

):


    user = db.query(User).filter(
        User.username == username
    ).first()



    if not user:

        return {
            "success":False,
            "message":"User not found"
        }



    if verify_password(
        password,
        user.password
    ):


        return {

            "success":True,

            "username":username

        }



    return {

        "success":False,

        "message":"Wrong password"

    }





# -------------------------
# Generate AI Report
# -------------------------


@app.post("/research")
def research(

    username:str,

    topic:str,

    db:Session=Depends(get_db)

):


    result = run_agent(topic)



    report = Report(

        username=username,

        topic=topic,

        content=result

    )


    db.add(report)

    db.commit()



    return {


        "message":"Report generated",

        "report":result


    }



# -------------------------
# User Report History
# -------------------------


@app.get("/reports/{username}")
def reports(

    username:str,

    db:Session=Depends(get_db)

):


    data = db.query(Report).filter(
        Report.username == username
    ).all()



    return [

        {

        "topic":r.topic,

        "report":r.content,

        "date":str(r.created_at)

        }

        for r in data

    ]