def my_func(sentences):
    return [sentence for sentence in sentences if inner_func(sentence)]


def inner_func(sentence):
    words = sentence.split()
    if not words:
        return False
    if not words[0].istitle():
        return False
    for word in words[1:]:
        if not word.islower():
            return False
    return True


if __name__ == "__main__":
    valid = ["Hello there", "Hey there.", "Do you know python?"]
    invalid = ["hello there", "words Of proper Cases are Here", "Where Is The Code"]

    assert my_func(valid) == valid
    assert my_func(invalid) == []
    assert my_func(valid + invalid) == valid

    print(valid[1:])

    print(my_func(valid + invalid))
