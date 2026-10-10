def reverse_words(text):
    # words = text.split()
    # result = []
    #
    # for word in words:
    #     if len(word) > 1:
    #         word = word[-1] + word[1:-1] + word[0]
    #     result.append(word)
    #
    # return result
    # return " ".join(result)

    out = [word[-1] + word[1:-1] + word[0] if len(word) > 1 else word for word in text.split()]

    return " ".join(out)


if __name__ == '__main__':
    # Example
    print(reverse_words("Hello world"))
    