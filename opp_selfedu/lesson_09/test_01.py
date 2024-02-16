class ThreadData:
    __shared_attrs = {
        "name": "thread_1",
        "data": {},
        "id": 1
    }

    def __init__(self):
        self.__dict__ = self.__shared_attrs


if __name__ == '__main__':
    th1 = ThreadData()
    th2 = ThreadData()

    print(th1.__dict__)
    print(th2.__dict__)

    th2.id = 3

    print(th1.__dict__)
    print(th2.__dict__)

    th1.attr_new = "new_attr"

    print(th1.__dict__)
    print(th2.__dict__)
