class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 < item < len(self.values):
            return self.values[item]
        else:
            raise IndexError('Bad index')

    def __setitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        elif key > len(self.values):
            diff = key - len(self.values)
            print('diff: ', diff)
            self.values.extend([0]*diff)
            self.values[key - 1] = value
        else:
            raise IndexError('Bad index')

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('Bad index')







