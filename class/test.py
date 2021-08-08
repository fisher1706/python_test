
class Counter:
    all_counters = []
    def __init__(self, initial_count=0):
        Counter.all_counters.append(self)
        self.count = initial_count


c1 = Counter(92)
c2 = Counter(62)

print(len(Counter.all_counters))
print(Counter.all_counters)

c = Counter(92)

print(len(Counter.all_counters))
print(Counter.all_counters)

print(c, c1, c2)

print(c.__class__)

print(c2.__dict__)
print(c.all_counters)
print(c2.all_counters)


c.__dict__['foo'] = 62

print(c.foo)
print(c.foo)

del c.foo

print(c.__dict__)

print(Counter.__name__)
print(Counter.__doc__)
print(Counter.__module__)
print(Counter.__bases__)
print(Counter.__dict__)

class A:
    def foo(self):
        pass



