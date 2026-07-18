from search import search_web


def use_tool(tool_name, query):

    if tool_name == "web_search":
        return search_web(query)

    return None