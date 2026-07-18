import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def create_plan(question):

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[

            {
                "role":"system",
                "content":
                """
You are a planning agent.

Break the user request into clear steps.

Example:

Question:
Find latest AI trends

Plan:
1. Search latest AI news
2. Collect important trends
3. Summarize findings
4. Provide answer
"""
            },

            {
                "role":"user",
                "content":question
            }

        ]
    )


    return response.choices[0].message.content