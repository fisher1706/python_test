class A:
    def foo(self):
        print('test')
        
a = A()

# print(a.foo)
# print(A.foo)
# print(a.foo())

class Counter:
    def __init__(self, initial_count=0):
        self.count = initial_count

    def increment(self):
        self.count += 1

    @property
    def iz_zero(self):
        return self.count == 0


c = Counter()
# assert c.iz_zero()
assert c.iz_zero

c.increment()
# assert not c.iz_zero()
assert not c.iz_zero
