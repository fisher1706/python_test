from functools import reduce


def get_even_numbers(data: list) -> list:
    event_number = list(filter(lambda x: x % 2 == 0, data))
    print(event_number)
    return event_number


def get_sum_of_numbers(data: list) -> int:
    sum_of_numbers = reduce(lambda x, y: x + y, data)
    print(sum_of_numbers)
    return sum_of_numbers


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    get_even_numbers(numbers)

    get_sum_of_numbers(numbers)
    