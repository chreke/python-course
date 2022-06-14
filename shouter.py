def shouter(string):
    postfix = "!" if not string.endswith("!") else ""
    return string.upper() + postfix
