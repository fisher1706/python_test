import re


def polynomial(data):
    forwards = ''.join(re.findall(r'[a-z]+', data.lower()))
    result = forwards[::-1]
    return result == data


if __name__ == '__main__':
    s = "madamimadam"

    print(s[::-1])
    r = polynomial(s)
    print(r)
