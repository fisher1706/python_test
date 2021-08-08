class DepartmentIT:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_DEV = 2

    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    def info2(self):
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)
    @property
    def info_prop(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    @classmethod
    def info_class(cls):
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)

    @staticmethod
    def info_static():
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    def make_backend(self):
        print('Python and Go')

    def make_frontend(self):
        print('React')

    def hiring_python_dev(self):
        DepartmentIT.PYTHON_DEV += 1


it1 = DepartmentIT()

# it1.info()
# it1.info2()
# it1.info_prop
# it1.info_class()
# it1.info_static()

print(it1.PYTHON_DEV)
it1.hiring_python_dev()
print(it1.PYTHON_DEV)

