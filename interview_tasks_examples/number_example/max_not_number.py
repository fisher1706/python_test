a = [1, -3, 6, 4, 1, 2]


def max_non_number(array: list):
    return abs(min(array)) if min(array) < 0 else max(array) + 1


if __name__ == "__main__":
    print(max_non_number(a))
