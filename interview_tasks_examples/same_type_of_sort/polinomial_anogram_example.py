import re

"""
Анограмма — это слово, термин, или фраза, образованные путём перестановки букв другого слова, термина, или фразы, 
при этом все исходные буквы должны быть использованы ровно один раз. Например, 
слово "рама" является анограммой слова "мара".
"""


def polynomial(data):
    forwards = "".join(re.findall(r"[a-z]+", data.lower()))
    result = forwards[::-1]
    return result == data


def is_anagram(s1, s2):
    print(set(s1))
    print(set(s2))
    return set(s1) == set(s2)


if __name__ == "__main__":
    s = "madamimadam"

    print(s[::-1])
    r = polynomial(s)
    print(r)
    print("*" * 200)

    print(is_anagram("elvis", "lives"))
