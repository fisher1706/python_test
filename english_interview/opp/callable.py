"""
Classes that implement __call__ can be invoked like functions.
"""


class CallableClass:
    def __init__(self, value):
        self.value = value

    def __call__(self, new_value):
        self.value = new_value
        return f'Value updated to {self.value}'


if __name__ == '__main__':
    obj = CallableClass(10)
    print(obj(20))
    