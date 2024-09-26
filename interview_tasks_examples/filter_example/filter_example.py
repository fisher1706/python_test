# https://ru.hexlet.io/courses/python-functions/lessons/map-filter-reduce/theory_unit


def greater_than_some_number(num):
    return num > 5


if __name__ == "__main__":
    numbers = [2, 7, 1, 8, 4, 5]
    result = list(filter(greater_than_some_number, numbers))

    print(result)
