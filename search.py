from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

tavily = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_web(query):
    response = tavily.search(
        query=query,
        max_results=5
    )

    results = []

    for item in response["results"]:
        results.append(
            {
                "title": item["title"],
                "content": item["content"],
                "url": item["url"]
            }
        )

    return results