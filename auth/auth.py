from database.database import (
    create_user,
    get_user
)


import hashlib



def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()





def register(username, password):


    hashed = hash_password(password)


    return create_user(
        username,
        hashed
    )







def login(username, password):


    user = get_user(username)



    if user is None:

        return False



    stored_password = user[1]



    hashed = hash_password(password)



    if stored_password == hashed:


        return user


    return False