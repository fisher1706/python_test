class Car:
    model = 'BMW'
    engine = 1.6

    @classmethod
    def start(cls):
        print('Start')

    @staticmethod
    def drive():
        print('Let`s go')
