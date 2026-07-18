from agents.supervisor import supervisor_agent
from agents.context_resolver import context_resolver

from agents.researcher import research_agent
from agents.analyst import analyst_agent
from agents.report_writer import report_writer_agent


from pdf_generator import create_pdf
from excel_generator import create_excel


from memory import get_history, save_message


from database.database import (
    initialize_database,
    save_report
)


import re



def clean_filename(name):

    name = re.sub(
        r'[^a-zA-Z0-9 ]',
        '',
        name
    )

    name = name.replace(
        " ",
        "_"
    )


    return name[:80]





def run_agent(task,user_id):


    initialize_database()


    original_topic = task


    history=get_history(user_id)



    if history:

        print("🧠 Memory loaded")

        task=context_resolver(
            task,
            history
        )



    print("🧠 Supervisor deciding...")


    plan=supervisor_agent(task)



    data=task



    for agent in plan["agents"]:


        if agent=="researcher":

            data=research_agent(data)



        elif agent=="analyst":

            data=analyst_agent(data)



        elif agent=="report_writer":

            data=report_writer_agent(data)




    filename = clean_filename(
        original_topic
    )



    print("\n📄 Creating PDF...")


    pdf_file=create_pdf(
        data,
        filename
    )



    print("\n📊 Creating Excel...")


    excel_file=create_excel(
        data,
        filename
    )




    save_message(
        user_id,
        "user",
        task
    )


    save_message(
        user_id,
        "assistant",
        data
    )



    save_report(

        user_id,

        original_topic,

        data,

        pdf_file,

        excel_file

    )



    return data