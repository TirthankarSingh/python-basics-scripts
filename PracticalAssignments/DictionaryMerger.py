import json


def dict_merger():
    try:
        d1 = json.loads(input("enter first dictionary: "))
        d2 = json.loads(input("enter second dictionary: "))
        d1.update(d2)
        return d1
    except json.JSONDecodeError:
        return "invalid Input"


print(dict_merger())