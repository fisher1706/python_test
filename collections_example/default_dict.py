from collections import defaultdict


"""
defaultdict - для создания словаря со значением по умолчанию. 
Значение подставляется при обращении к несуществующему ключу.
"""


a_dict = defaultdict(int)
for char in "hello":
    a_dict[char] += 1


b_dict = defaultdict(list)
for char in "hello":
    b_dict[char].append(char)


if __name__ == "__main__":
    print(a_dict)
    print(a_dict.get("h"))

    print(sorted(a_dict.items(), key=lambda x: x[0]))  # sort by key
    print(sorted(a_dict.items(), key=lambda x: x[1], reverse=True))  # sort by value

    print(b_dict)
