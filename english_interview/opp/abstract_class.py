"""
Abstract Base Classes
    Abstract base classes define a common interface that must be implemented by concrete subclasses.
    They provide a way to enforce contracts and ensure consistent behavior across related classes.
"""


import abc


class Parent(abc.ABC):
    @abc.abstractmethod
    def get_info(self, parameter):
        """Get parameter info"""

    @abc.abstractmethod
    def set_info(self, parameter, value):
        """Set parameter to value"""


class Child(Parent):
    def __init__(self):
        self._parameters = {}

    def get_info(self, parameter):
        return self._parameters.get(parameter)

    def set_info(self, parameter, value):
        self._parameters[parameter] = value
        return self._parameters



if __name__ == "__main__":
    ch = Child()
    print(ch.__dict__)

    ch.set_info("name", "Oleg")
    print(ch.__dict__)

