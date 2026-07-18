import streamlit as st


from database.database import initialize_database,get_reports

from auth.auth import register,login

from agent import run_agent




initialize_database()



st.set_page_config(
    page_title="AI Research SaaS"
)




if "user" not in st.session_state:

    st.session_state.user=None





# ======================
# LOGIN PAGE
# ======================


if st.session_state.user is None:


    st.title("🚀 AI Research Agent")


    option=st.selectbox(
        "Choose",

        [
            "Login",
            "Register"
        ]
    )



    username=st.text_input(
        "Username"
    )


    password=st.text_input(
        "Password",
        type="password"
    )



    if option=="Register":


        if st.button("Create Account"):


            if register(username,password):

                st.success(
                    "Account created. Login now."
                )

            else:

                st.error(
                    "Username already exists"
                )




    else:


        if st.button("Login"):


            if login(username,password):

                st.session_state.user=username

                st.success(
                    "Login successful"
                )

                st.rerun()


            else:

                st.error(
                    "Invalid credentials"
                )





# ======================
# DASHBOARD
# ======================


else:


    username=st.session_state.user



    st.sidebar.write(
        f"Welcome {username} 👋"
    )


    menu=st.sidebar.selectbox(

        "Menu",

        [
            "Generate Research",
            "My Reports",
            "Logout"
        ]

    )



    if menu=="Logout":

        st.session_state.user=None

        st.rerun()





    if menu=="Generate Research":


        st.title(
            "🚀 Generate AI Research"
        )


        topic=st.text_input(
            "Research Topic"
        )



        if st.button("Generate"):


            result=run_agent(
                topic,
                username
            )


            st.write(result)






    if menu=="My Reports":


        st.title(
            "📂 My Reports"
        )


        reports=get_reports(username)



        for r in reports:


            st.subheader(
                r[0]
            )


            st.write(
                "Created:",
                r[3]
            )


            st.write(
                "PDF:",
                r[1]
            )


            st.write(
                "Excel:",
                r[2]
            )