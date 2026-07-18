import pandas as pd
import os
import re



def clean_filename(name):

    name=name.lower()

    name=re.sub(
        r'[^a-zA-Z0-9 ]',
        '',
        name
    )

    name=name.replace(
        " ",
        "_"
    )

    return name[:80]





def create_excel(data, topic="AI_Report"):


    os.makedirs(
        "reports",
        exist_ok=True
    )


    filename=clean_filename(topic)


    path=f"reports/{filename}.xlsx"



    df=pd.DataFrame(
        {
            "Report":[data]
        }
    )


    df.to_excel(
        path,
        index=False
    )


    return path