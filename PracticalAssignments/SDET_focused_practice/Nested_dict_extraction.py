api_resp = {
    "user": {
        "id": 101,
        "username": "alice_w",
        "profile": {
            "email": "alice@example.com",
            "address": {
                "city": "Bangalore",
                "zipcode": "560001"
            }
        }
    },
    "posts": [
        {"id": 1, "title": "Intro to Python"},
        {"id": 2, "title": "API Testing"}
    ]
}


"""
Below is expected O/p
Username: alice_w
Email: alice@example.com
City: Bangalore
Zip: 560001
First post title: Intro to Python

"""
def extraction():
    print(api_resp.keys())
    print("User name: ", api_resp["user"]["username"])
    print("Email: ", api_resp["user"]["profile"]["email"])
    print("City: ", api_resp["user"]["profile"]["address"]["city"])
    print("Zip: ", api_resp["user"]["profile"]["address"]["zipcode"])
    print("First post title: ", api_resp["posts"][0]["title"])


extraction()