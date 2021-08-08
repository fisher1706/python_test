class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_public_data(self):
        self.___print_protected_data()

    def ___print_protected_data(self):
        print(self.__name, self.__balance, self.__passport)


account = BankAccount('oleg', 100, 170678)
account.print_public_data()
print(dir(account))
account._BankAccount___print_protected_data()
print(account._BankAccount__balance)
