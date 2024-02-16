my_list = [1, 2, 3, 4, 5]
my_iterator_one = iter(my_list)


def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


my_iterator_two = my_generator()


class MyIterator:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result


if __name__ == '__main__':
    print(next(my_iterator_one))
    print(next(my_iterator_one))
    print(next(my_iterator_one))
    print("*" * 300)

    print(next(my_iterator_two))
    print(next(my_iterator_two))
    print(next(my_iterator_two))
    print("*" * 300)

    i = MyIterator([2, 2, 3])
    print(i.__dict__)

    for val in i:
        print(val)
