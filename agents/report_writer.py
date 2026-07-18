import os

from dotenv import load_dotenv
from groq import Groq

from task_memory import save_memory, get_memory


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



def report_writer_agent(analysis=""):


    print("\n📝 Report Writer Agent working...\n")


    if not analysis:

        analysis = get_memory(
            "analysis"
        )


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[

            {
                "role":"system",
                "content":
"""
Create a professional business report.

Structure:

1. Executive Summary
2. Key Findings
3. Market Analysis
4. Recommendations
"""
            },

            {
                "role":"user",
                "content":analysis
            }

        ]

    )


    report = response.choices[0].message.content


    save_memory(
        "report",
        report
    )


    return report