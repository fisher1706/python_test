class NetworkOne:
    all_allocated_ip = []

    def some_update(self, var):
        type(self).all_allocated_ip.append(var)


class NetworkTwo:
    all_allocated_ip = []

    def some_update(self, var):
        self.all_allocated_ip.append(var)


if __name__ == '__main__':
    n1 = NetworkOne()
    n1.some_update(5)
    print(n1.all_allocated_ip)
    print(NetworkOne.all_allocated_ip)

    n2 = NetworkTwo()
    n2.some_update(5)
    print(n2.all_allocated_ip)
    print(NetworkTwo.all_allocated_ip)
