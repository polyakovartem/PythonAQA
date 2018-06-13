import re


def increment_string(strng):
        match = re.match(r"(.*?)(\d*)$", strng)
        string = match.group(1)
        number = match.group(2)
        if not number:
            return string + '1'
        else:
            return string + str(int(number)+1).zfill(len(number))


print(increment_string("foo"))  # foo1
print(increment_string("foobar001"))  # foobar002
print(increment_string("foobar1"))  # foobar2
print(increment_string(""))  # 1
