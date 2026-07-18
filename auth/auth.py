from database.database import (
    create_user,
    get_user
)


from auth.security import (
    hash_password,
    verify_password
)




def register(username,password):


    hashed = hash_password(password)


    return create_user(
        username,
        hashed
    )






def login(username,password):


    user=get_user(username)



    if not user:

        return False



    stored_password=user[1]



    return verify_password(
        password,
        stored_password
    )