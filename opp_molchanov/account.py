"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №8
lesson №9
"""

from datetime import datetime
import pytz


WHITE = "\033[00m"
GREEN = "\033[0;32m"
RED = "\033[1;31m"


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        self._history = []

    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self._history.append([amount, self._get_current_time()])

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f"You spent {amount} units")
            self.show_balance()
            self._history.append([-amount, self._get_current_time()])
        else:
            print("Not enough money")
            self.show_balance()

    def show_balance(self):
        print(f"Balance: {self.__balance}")

    def show_history(self):
        for amount, date in self._history:
            if amount > 0:
                transaction = "deposited"
                color = GREEN
            else:
                transaction = "withdraw"
                color = RED

            print(f"{color} {amount} {WHITE} {transaction} on {date}")


if __name__ == "__main__":
    a = Account("oleg", 0)

    a.deposit(100)
    a.deposit(100)
    a.deposit(100)
    a.withdraw(250)

    a.show_history()

    x = a._get_current_time()
    print(x)

    a.__balance = 100000000
    print(a.__dict__)

    a.show_history()
