"""
https://www.patreon.com/oleg_molchanov/posts?filters[tag]=%23%D0%BA%D1%83%D1%80%D1%81%D0%9E%D0%9E%D0%9F
password: xau8ahPh
lesson №21
"""


class ValidString:
    def __set_name__(self, owner_class, property_name):
        # print(f'self: {self}')
        # print(f'owner_class: {owner_class}')
        # print(f'property_name: {property_name}')

        self.property_name = property_name

    def __set__(self, instance, value):
        print("__set__ was called")

        if not isinstance(value, str):
            raise ValueError(
                f"{self.property_name} must be a String, "
                f"but {type(value).__name__} was passed"
            )

        # key = '_' + self.property_name
        # setattr(instance, key, value)

        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner):
        print("__get__ was called")

        if instance is None:
            return self

        # key = '_' + self.property_name
        # return getattr(instance, key, None)

        return instance.__dict__.get(self.property_name, None)


class Person:
    name = ValidString()
    surname = ValidString()


if __name__ == "__main__":
    p = Person()
    print(p)
    print(p.__dict__)

    p.name = "Ivan"
    # print(p.name)

    p.surname = "Zapel"
    print(p.__dict__)
