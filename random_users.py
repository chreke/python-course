import requests

class RandomUser:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __str__(self):
        return f"{self.name} <{self.email}>"

def deserialize(data):
    return RandomUser(
        data["name"]["first"] + " " + data["name"]["last"],
        data["dob"]["age"],
        data["email"],
    )

def get_random_users():
    url = "https://randomuser.me/api/?results=10"
    return requests.get(url).json()["results"]

def random_users():
    users = []
    while True:
        if not users:
            users = [deserialize(x) for x in get_random_users()]
        yield users.pop()
