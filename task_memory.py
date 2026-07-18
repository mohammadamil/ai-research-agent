import json
import os


MEMORY_FILE = "task_memory.json"


def save_memory(key, value):

    if os.path.exists(MEMORY_FILE):

        with open(MEMORY_FILE, "r") as f:
            memory = json.load(f)

    else:
        memory = {}


    memory[key] = value


    with open(MEMORY_FILE, "w") as f:
        json.dump(
            memory,
            f,
            indent=4
        )



def get_memory(key):

    if not os.path.exists(MEMORY_FILE):
        return ""


    with open(MEMORY_FILE, "r") as f:

        memory = json.load(f)


    return memory.get(key, "")