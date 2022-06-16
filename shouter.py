def shout(string):
    return string.upper() + ("!" if not string.endswith("!") else "")
