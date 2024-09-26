def sum_of_digits(some_number):
    return sum([int(val) for val in str(some_number)]) if isinstance(some_number, (int, str)) else "error"



if __name__ == "__main__":
    number = "123"
    data = sum_of_digits(number)
    print(data)
