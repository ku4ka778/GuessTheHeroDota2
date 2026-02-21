import json

def ParsingJson():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data
