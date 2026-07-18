from search import search_web


def calculator(expression):

    try:
        result = eval(expression)
        return str(result)

    except:
        return "Unable to calculate"


TOOLS = {

    "web_search": search_web,

    "calculator": calculator

}