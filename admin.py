import streamlit as st

from database.database import (
    get_total_users,
    get_total_reports,
    get_usage_count,
    get_all_users,
    get_all_reports
)



def show_admin_dashboard():


    st.title("👑 Admin Dashboard")


    st.write(
        "Monitor your AI Research SaaS platform"
    )


    col1,col2,col3 = st.columns(3)



    with col1:

        st.metric(
            "Total Users",
            get_total_users()
        )



    with col2:

        st.metric(
            "Reports Generated",
            get_total_reports()
        )



    with col3:

        st.metric(
            "Total Activities",
            get_usage_count()
        )



    st.divider()



    st.subheader(
        "👥 Users"
    )


    users=get_all_users()



    if users:


        for user in users:

            st.write(
                f"""
                Username: {user[0]}
                
                Role: {user[1]}
                
                Created: {user[2]}
                """
            )

            st.divider()



    else:

        st.info(
            "No users found"
        )




    st.subheader(
        "📄 Generated Reports"
    )


    reports=get_all_reports()



    if reports:


        for report in reports:


            st.write(

            f"""
            User:
            {report[0]}

            Topic:
            {report[1]}

            Created:
            {report[2]}
            """

            )


            st.divider()



    else:

        st.info(
            "No reports generated"
        )