"""
Monkey patching — это техника изменения поведения кода во время выполнения путем динамической замены или добавления
методов или атрибутов в существующем объекте. Эта техника может быть полезна в том случае, когда изменения не могут
быть внесены в существующий код, и требует минимальных изменений в существующем коде.
"""


class MyBaseClass:
    def my_method(self):
        print(f"My method called: {self}")


def monkey_patch():
    def new_method(self):
        print(f"New method called: {self}")

    MyBaseClass.my_method = new_method


if __name__ == "__main__":
    monkey_patch()
    obj = MyBaseClass()
    obj.my_method()
