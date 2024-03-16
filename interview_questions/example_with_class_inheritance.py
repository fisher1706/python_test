class A:
    def __init__(self, param):
        self.URL = 123
        self.param = param
        print(f"url from class A =: {self.URL}")

    def connect(self):
        print(f"{self.URL}")


class B(A):
    def __init__(self, param):
        super().__init__(param)
        self.URL = 'localhost'


if __name__ == '__main__':
    b = B(100)
    print(b.__dict__)
    b.connect()
