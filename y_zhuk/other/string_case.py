
def solve(string):
    lowers = []
    uppers = []
    for letter in string:
        if letter.islower():
            lowers.append(letter)
        elif letter.isupper():
            uppers.append(letter)
    # values = [letter for letter in string if letter.islower()]
    if len(lowers) == len(uppers):
        string = string.lower()
    elif len(lowers) > len(uppers):
        string = string.lower()
    elif len(lowers) < len(uppers):
        string = string.upper()
    return string


print(solve("CODe"))
print(solve("COde"))
print(solve("Code"))
