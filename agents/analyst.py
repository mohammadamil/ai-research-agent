import os

from dotenv import load_dotenv
from groq import Groq

from task_memory import save_memory, get_memory


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



def analyst_agent(research=""):


    print("\n📊 Analyst Agent working...\n")


    if not research:

        research = get_memory(
            "research"
        )


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[

            {
                "role":"system",
                "content":
"""
You are an AI analyst.

Analyze research.

Find:
- insights
- trends
- opportunities
- risks
"""
            },

            {
                "role":"user",
                "content":research
            }

        ]

    )


    analysis = response.choices[0].message.content


    save_memory(
        "analysis",
        analysis
    )


    return analysis