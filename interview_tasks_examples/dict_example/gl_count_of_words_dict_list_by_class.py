class WordCounterDict:
    words = {}
    count = 1

    def add_word(self, word: str):
        if self.words.get(word, 0) != 0:
            self.words.update({word: self.words[word] + 1})
        else:
            self.words[word] = self.count

    def get_count(self, word: str) -> int:
        count_inner = self.words.get(word, 0)
        return count_inner

    def get_inner_dict(self):
        return self.words


class WordCounterList:
    words = []

    def add_word(self, word: str):
        self.words.append(word)

    def get_count(self, word: str) -> int:
        count_inner = self.words.count(word)
        return count_inner


if __name__ == "__main__":
    wc = WordCounterDict()
    wc.add_word("apple")
    wc.add_word("banana")
    wc.add_word("apple")

    print(wc.get_inner_dict())

    assert wc.get_count("apple") == 2
    assert wc.get_count("banana") == 1
    assert wc.get_count("cucumber") == 0

    print(wc.get_count("apple"))
    print(wc.get_count("banana"))
    print(wc.get_count("cucumber"))

    print("*" * 200)

    wc = WordCounterList()
    wc.add_word("apple")
    wc.add_word("banana")
    wc.add_word("apple")

    assert wc.get_count("apple") == 2
    assert wc.get_count("banana") == 1
    assert wc.get_count("cucumber") == 0

    print(wc.get_count("apple"))
    print(wc.get_count("banana"))
    print(wc.get_count("cucumber"))
