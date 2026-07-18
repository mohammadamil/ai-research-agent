import pandas as pd
import os



def create_excel(content, filename):


    os.makedirs(
        "reports",
        exist_ok=True
    )


    file_path=f"reports/{filename}.xlsx"



    df=pd.DataFrame(
        {
            "Report":[content]
        }
    )


    df.to_excel(
        file_path,
        index=False
    )


    return file_path