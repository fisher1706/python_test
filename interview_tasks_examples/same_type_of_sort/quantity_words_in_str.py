def count_words(my_string):
    words = [word for word in my_string.split() if word != "-" and not word.isdigit()]
    return len(words)


if __name__ == '__main__':
    s = "hello fisher"
    count = count_words(s)
    print(count)
