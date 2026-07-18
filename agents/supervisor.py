import os
import json
import re

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def supervisor_agent(task):


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[

            {
                "role":"system",
                "content":
"""
You are a supervisor AI.

Choose which agents are required.

Available agents:

researcher
analyst
report_writer


Rules:

- Latest information, market research, competitors, companies:
use researcher + analyst + report_writer

- Data analysis or calculations:
use analyst + report_writer


Return ONLY JSON.
No explanation.
No markdown.

Format:

{
"agents":[
"researcher",
"analyst",
"report_writer"
]
}

"""
            },

            {
                "role":"user",
                "content":task
            }

        ],

        temperature=0
    )


    output = response.choices[0].message.content.strip()


    print("\nRaw Supervisor Output:")
    print(output)


    # Remove markdown if model adds it

    output = re.sub(
        r"```json|```",
        "",
        output
    ).strip()


    try:

        return json.loads(output)


    except:


        print("⚠️ Invalid JSON. Using default workflow")


        return {
            "agents":[
                "researcher",
                "analyst",
                "report_writer"
            ]
        }