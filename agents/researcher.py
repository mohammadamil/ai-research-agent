from search import search_web
from task_memory import save_memory



def research_agent(topic):


    print("\n🔎 Research Agent working...\n")


    results = search_web(topic)


    research = ""


    for item in results:

        research += f"""
Title:
{item['title']}

Content:
{item['content']}

URL:
{item['url']}

----------------
"""


    save_memory(
        "research",
        research
    )


    return research