import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def context_resolver(task, history):

    print("\n🧠 Context Resolver working...\n")


    conversation = ""


    for msg in history:

        conversation += f"""
{msg['role']}:
{msg['content']}

"""


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[

            {
                "role":"system",
                "content":
"""
You are a Context Resolver AI.

Your job:

Convert user follow-up questions into complete research requests.

Use previous conversation history.

Examples:

History:
User: Research TCS

New question:
Compare it with Infosys

Output:
Compare TCS with Infosys


History:
User: Research Tesla

New question:
What about revenue?

Output:
Tesla revenue analysis


Rules:

- Return only the rewritten task.
- No explanation.
- No markdown.
"""
            },

            {
                "role":"user",
                "content":f"""

Conversation History:

{conversation}


Current User Request:

{task}

"""
            }

        ],

        temperature=0
    )


    return response.choices[0].message.content.strip()