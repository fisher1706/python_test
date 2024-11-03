"""
Customize attribute access with descriptors.
"""


class Descriptor:
    def __get__(self, instance, owner):
        return 'This is a descriptor value.'

    def __set__(self, instance, value):
        print(f'Setting value to {value}.')


class MyClass:
    my_attr = Descriptor()
    

if __name__ == '__main__':
    obj = MyClass()
    print(obj.my_attr) # Output: This is a descriptor value.
    obj.my_attr = 'New value' # Output: Setting value to New value.
