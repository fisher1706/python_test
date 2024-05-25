from pprint import pprint


def dict_comprehension(data):
    dict_comp = {key: val for key, val in enumerate(data)}
    print(dict_comp)


def list_comprehension(data):
    list_comp = [i for i in range(len(data))]
    print(list_comp)


text = "Hello world"


def list_comprehension_double(data=text):
    letters = [letter for word in data.split() for letter in word if letter < "l"]
    print(letters)


def matrix_example():
    matrix = [list(range(x, x + 3)) for x in range(3)]
    pprint(matrix, indent=1, width=15)


def create_set_unique_letters(data=text):
    letters = {letter for word in data.split() for letter in word if letter < "l"}
    print(letters)


if __name__ == "__main__":
    sample = ["one", "two", "three"]

    dict_comprehension(sample)
    list_comprehension(sample)
    list_comprehension_double()
    matrix_example()
    create_set_unique_letters()
