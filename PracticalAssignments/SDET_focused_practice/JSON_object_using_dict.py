import json

data = {
    "name": "Alice",
    "age": 30,
    "city": "Bangalore",
    "skills": ["python", "selenium"]
}


def specific_values():
    if not data:
        print("empty dict")
        return

    for k, v in data.items():
        print(f"{k}: {v}")


