class B:
    def b(self, b1, b2):
        print(f"b1: {b1}, b2: {b2}")


class A(B):
    A = 1

    def b(self, a1, **kwargs):
        super().b(self.A, a1)


if __name__ == '__main__':
    a = A()
    a.b(1)
