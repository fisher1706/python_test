def reverse_words(my_string: str, symbols: list) -> str:
    words = my_string.split()
    result = []

    for word in words:
        new_world = word[::-1]
        if word[-1] in symbols:
            new_world = word[-2::-1] + word[-1]
        result.append(new_world)
    return ' '.join(result)


if __name__ == '__main__':
    start_string = "Don't worry, be happy!"
    find_symbols = [".", ",", "!", "?"]
    r = reverse_words(start_string, find_symbols)
    print(r)
