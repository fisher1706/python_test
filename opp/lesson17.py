class BankAccount:
    def __init__(self, name, balance):
        print('new obj init')
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            print('__add__ call')
            return BankAccount(self.name, self.balance + other)
        raise NotImplemented

    def __radd__(self, other):
        print('__radd__')
        return self + other

    def __repr__(self):
        return f'Клиент {self.name} с балансом {self.balance}'

