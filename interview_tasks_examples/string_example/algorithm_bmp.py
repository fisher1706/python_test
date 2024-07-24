# https://www.youtube.com/watch?v=KIUHWMwavQg
# https://www.youtube.com/watch?v=N6G6HVwJ4wQ&t=25s

def preprocess(substring, start_index, end_index):
    alphabet_table = [len(substring) for _ in range(end_index - start_index + 1)]
    for i in range(len(substring) - 1):
        alphabet_table[ord(substring[i]) - start_index] = len(substring) - i - 1
    return alphabet_table


def bmh_search(text, substring):
    if len(substring) > len(text):
        return None
    i = len(substring) - 1
    n = i
    start_index = ord(" ")
    end_index = ord("~")
    alphabet_table = preprocess(substring, start_index, end_index)
    while i < len(text):
        if text[i-n: i + 1] == substring:
            return i - n
        i = i + alphabet_table[ord(text[i]) - start_index]
    return None


if __name__ == '__main__':
    my_substring = "apple"
    my_text = "awersome apple"
    print(bmh_search(my_text, my_substring))

    data = "apple"
    start = ord(" ")
    end = ord("~")

    x = preprocess(data, start, end)
    print(x)
