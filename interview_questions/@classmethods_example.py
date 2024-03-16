"""
@classmethod -> change behavior of class
"""


class Bank:
    general_message = "empty"

    def print_general_message(self):
        print(self.general_message)

    @classmethod
    def change_general_message(cls, new_message):
        cls.general_message = new_message


if __name__ == '__main__':
    b1 = Bank()
    b2 = Bank()

    b1.print_general_message()
    b2.print_general_message()
    print("*" * 200)

    b1.change_general_message("new_message")
    b1.print_general_message()
    b2.print_general_message()
