from pprint import pprint


def dict_comprehension(data):
    dict_comp = {key: val for key, val in enumerate(data)}
    print(dict_comp)


def list_comprehension(data):
    list_comp = [i for i in range(len(data))]
    print(list_comp)


text = "Hello world"


def list_comprehension_double(data: str = text):
    letters = [letter for word in data.split() for letter in word if letter < "l"]
    print(letters)


def create_set_unique_letters(data: str = text):
    letters = {letter for word in data.split() for letter in word if letter < "l"}
    print(letters)


def create_list_with_ternary_operator(data: list):
    out = [0 if x < 0 else 1 for x in data if x % 2 == 0]
    print(out)


def matrix_example():
    matrix = [list(range(x, x + 3)) for x in range(3)]
    pprint(matrix, indent=1, width=15)


if __name__ == "__main__":
    sample = ["one", "two", "three"]

    dict_comprehension(sample)

    list_comprehension(sample)

    list_comprehension_double()
    matrix_example()
    create_set_unique_letters()

    begin = [-3, 4, 7, -6]
    create_list_with_ternary_operator(begin)
