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

    page_title="AI Research Platform",

    page_icon="🚀",

    layout="wide"

)



initialize_database()

from reset_database import *

# ------------------
# SESSION
# ------------------

if "user" not in st.session_state:

    st.session_state.user = None


if "role" not in st.session_state:

    st.session_state.role = None





# ------------------
# LOGIN / REGISTER
# ------------------

if st.session_state.user is None:


    st.title(
        "🤖 AI Research Platform"
    )


    st.write(
        "Generate AI-powered business research reports"
    )


    option = st.selectbox(

        "Choose",

        [
            "Login",
            "Register"
        ]

    )


    username = st.text_input(
        "Username"
    )


    password = st.text_input(
        "Password",
        type="password"
    )



    if option == "Register":


        if st.button("Create Account"):


            result = register(
                username,
                password
            )


            if result:

                st.success(
                    "Account created successfully"
                )

            else:

                st.error(
                    "Username already exists"
                )



    else:


        if st.button("Login"):


            result = login(
                username,
                password
            )


            if result:


                st.session_state.user = result[0]

                st.session_state.role = result[2]

                st.rerun()



            else:

                st.error(
                    "Invalid username or password"
                )



    st.stop()






# ------------------
# USER INFO
# ------------------

username = st.session_state.user

role = st.session_state.role





# ------------------
# TOP BAR
# ------------------

col1,col2 = st.columns(
    [8,1]
)


with col1:

    st.title(
        f"Welcome {username} 👋"
    )


with col2:


    if st.button(
        "Logout"
    ):

        st.session_state.user = None

        st.session_state.role = None

        st.rerun()






# ------------------
# SIDEBAR
# ------------------

st.sidebar.markdown(

    f"## 🤖 {username} Research AI"

)


st.sidebar.write(

    "Autonomous Business Research Agent"

)


st.sidebar.caption(

    f"Role : {role}"

)


st.sidebar.divider()





# ------------------
# MENU
# ------------------

menu_items = [

    "🏠 Dashboard",

    "💬 AI Research Chat",

    "📂 My Reports"

]


if role == "admin":

    menu_items.append(
        "👑 Admin"
    )



menu = st.sidebar.selectbox(

    "☰ Menu",

    menu_items

)






# ==================================================
# DASHBOARD
# ==================================================

if menu == "🏠 Dashboard":


    st.header(
        "🔎 AI Research Dashboard"
    )


    search_topic = st.text_input(

        "What do you want to research?",

        placeholder="Example: Top AI companies in India 2026"

    )



    if st.button(
        "🚀 Generate Report"
    ):


        if search_topic:


            with st.spinner(

                "🤖 AI Agents researching..."

            ):


                result = run_agent(

                    search_topic,

                    username

                )


                track_usage(

                    username,

                    "dashboard_search",

                    search_topic

                )



            st.success(

                "Report Generated Successfully ✅"

            )



            if isinstance(result,dict):


                st.write(

                    result.get(
                        "report"
                    )

                )


                st.divider()


                st.subheader(
                    "📥 Download Report"
                )



                pdf = result.get(
                    "pdf_file"
                )


                excel = result.get(
                    "excel_file"
                )



                c1,c2 = st.columns(2)



                with c1:


                    if pdf and os.path.exists(pdf):


                        with open(pdf,"rb") as file:


                            st.download_button(

                                "📄 Download PDF",

                                file,

                                file_name=os.path.basename(pdf),

                                mime="application/pdf",

                                key="dashboard_pdf"

                            )



                with c2:


                    if excel and os.path.exists(excel):


                        with open(excel,"rb") as file:


                            st.download_button(

                                "📊 Download Excel",

                                file,

                                file_name=os.path.basename(excel),

                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

                                key="dashboard_excel"

                            )



            else:


                st.write(result)



        else:


            st.warning(
                "Please enter a research topic"
            )





# ==================================================
# AI CHAT
# ==================================================

elif menu == "💬 AI Research Chat":


    st.header(
        "💬 AI Research Assistant"
    )


    topic = st.chat_input(

        "Ask your research question..."

    )



    if topic:


        with st.chat_message("user"):

            st.write(topic)



        with st.chat_message("assistant"):


            with st.spinner(

                "🤖 AI Agents working..."

            ):


                result = run_agent(

                    topic,

                    username

                )


                track_usage(

                    username,

                    "chat",

                    topic

                )



            st.success(

                "Report Generated Successfully ✅"

            )



            if isinstance(result,dict):

                st.write(

                    result["report"]

                )

            else:

                st.write(result)






# ==================================================
# MY REPORTS
# ==================================================

elif menu == "📂 My Reports":


    st.header(
        "📂 My Reports"
    )



    reports = get_reports(
        username
    )



    if reports:


        for index,report in enumerate(reports):


            topic = report[0]

            pdf = report[1]

            excel = report[2]



            st.subheader(
                topic
            )



            if pdf and os.path.exists(pdf):


                with open(pdf,"rb") as file:


                    st.download_button(

                        "📄 Download PDF",

                        file,

                        file_name=os.path.basename(pdf),

                        mime="application/pdf",

                        key=f"report_pdf_{index}"

                    )



            if excel and os.path.exists(excel):


                with open(excel,"rb") as file:


                    st.download_button(

                        "📊 Download Excel",

                        file,

                        file_name=os.path.basename(excel),

                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

                        key=f"report_excel_{index}"

                    )


            st.divider()



    else:


        st.info(
            "No reports yet"
        )






# ==================================================
# ADMIN
# ==================================================

elif menu == "👑 Admin":


    if role == "admin":

        show_admin_dashboard()


    else:

        st.error(
            "Access denied"
        )