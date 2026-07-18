import streamlit as st
import os


from auth.auth import (
    register,
    login
)


from agent import run_agent


from database.database import (
    initialize_database,
    get_reports
)


from admin import show_admin_dashboard


from usage import track_usage



# ------------------
# APP CONFIG
# ------------------

st.set_page_config(

    page_title="Mohammad AI Research Platform",

    page_icon="🚀",

    layout="wide"

)



initialize_database()



# ------------------
# BRANDING
# ------------------

st.sidebar.title(
    "🚀 Mohammad AI"
)


st.sidebar.write(
    "Autonomous Business Research Agent"
)


st.sidebar.divider()


st.sidebar.caption(
    "Multi-Agent Intelligence System"
)



# ------------------
# SESSION
# ------------------

if "user" not in st.session_state:

    st.session_state.user=None



# ------------------
# LOGIN PAGE
# ------------------

if st.session_state.user is None:


    st.title(
        "🤖 AI Research Platform"
    )


    st.write(
        "Generate AI-powered business research reports"
    )


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


            result=register(
                username,
                password
            )


            if result:

                st.success(
                    "Account created"
                )

            else:

                st.error(
                    "Username already exists"
                )



    else:


        if st.button("Login"):


            result=login(
                username,
                password
            )


            if result:


                st.session_state.user=username

                st.success(
                    "Login successful"
                )

                st.rerun()


            else:

                st.error(
                    "Invalid login"
                )



    st.stop()





# ------------------
# LOGGED IN USER
# ------------------


username=st.session_state.user



st.sidebar.success(
    f"Welcome {username}"
)



menu=st.sidebar.radio(

    "Menu",

    [
        "🏠 Dashboard",
        "💬 AI Research Chat",
        "📂 My Reports",
        "👑 Admin"
    ]

)



# ------------------
# DASHBOARD
# ------------------

if menu=="🏠 Dashboard":


    st.title(
        f"Welcome {username} 👋"
    )


    st.info(
        """
        Your AI Research Assistant can:

        • Perform web research
        • Analyze information
        • Generate professional reports
        • Create PDF and Excel files
        """
    )






# ------------------
# CHAT INTERFACE
# ------------------

elif menu=="💬 AI Research Chat":


    st.title(
        "💬 AI Research Assistant"
    )


    st.write(
        "Ask anything about companies, markets or industries"
    )


    topic = st.chat_input(
        "Example: Compare TCS vs Infosys"
    )



    if topic:


        with st.chat_message("user"):

            st.write(topic)



        with st.chat_message("assistant"):


            with st.spinner(
                "🤖 AI Agents working..."
            ):


                response = run_agent(
                    topic,
                    username
                )


                track_usage(
                    username,
                    "research_generated",
                    topic
                )


            st.success(
                "Report Generated Successfully ✅"
            )


            st.write(response)





# ------------------
# REPORTS
# ------------------

elif menu=="📂 My Reports":


    st.title(
        "📂 My Reports"
    )



    reports=get_reports(
        username
    )



    if reports:


        for report in reports:


            topic=report[0]

            pdf=report[1]

            excel=report[2]



            st.subheader(
                topic
            )



            col1,col2=st.columns(2)



            with col1:


                if os.path.exists(pdf):


                    with open(pdf,"rb") as file:


                        st.download_button(

                            "⬇ Download PDF",

                            file,

                            file_name=os.path.basename(pdf)

                        )




            with col2:


                if os.path.exists(excel):


                    with open(excel,"rb") as file:


                        st.download_button(

                            "⬇ Download Excel",

                            file,

                            file_name=os.path.basename(excel)

                        )


            st.divider()



    else:


        st.info(
            "No reports yet"
        )






# ------------------
# ADMIN
# ------------------

elif menu=="👑 Admin":


    show_admin_dashboard()




# ------------------
# LOGOUT
# ------------------

if st.sidebar.button(
    "Logout"
):

    st.session_state.user=None

    st.rerun()