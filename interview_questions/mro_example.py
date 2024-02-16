class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


if __name__ == '__main__':
    print(D.mro())
    print("*" * 300)

    print(D.__mro__)
