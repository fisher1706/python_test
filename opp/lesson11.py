class BankAccount:
    @property
    def my_balance(self):
        return self._my_balance

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get_balance')
        return self.__balance

    def set_balance(self, value):
        print('set_balance')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    def delete_balance(self):
        print('delete_balance')
        del self.__balance

    my_balance = property()
    my_balance = my_balance.getter(get_balance)
    my_balance = my_balance.setter(set_balance)
    my_balance = my_balance.deleter(delete_balance)

if __name__ == '__main__':

    a = BankAccount('Ivan', 100)
    print(a.__dict__)

    print(a.get_balance())
    print(a.my_balance)



