class RandomUser:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

def deserialize(data):
    return RandomUser(
        data["name"]["first"] + " " + data["name"]["last"],
        data["dob"]["age"],
        data["email"],
    )

def get_random_users():
    pass

def random_users():
    users = []
    while True:
        if not users:
            users = [deserialize(x) for x in get_random_users()]
        yield users.pop()
