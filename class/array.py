x = [4, 5, 5, 7]
y = [1, 2, 3]

num = 6
class A:
    def test(self, x, y, num):
        out = []
        for a in range(len(x)):
            for b in range(len(y)):
                if x[a] + y[b] == num:
                    out.append([a, b])
        return out

print(A().test(x, y, num))


def fib(num):
    out = []
    x, y = 0, 1
    for i in range(num):
        x, y = y, x + y
        out.append(y)
    return out

if __name__ == '__main__':
    print(fib(15))

