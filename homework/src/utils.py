import csv
import os


def cleaner(path):
    for _file in os.listdir(path):
        os.remove(path + _file)
        print('file: {} - deleted'.format(_file))

def read_csv(filename, path):
    dir_file = path + filename

    try:
        with open(dir_file, "r") as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                return row
    except:
        raise Exception('can not read file {}!'.format(filename))

def convert_dict(data):
    for k, v in data.items():
        if type(v).__name__ in ('int', 'float'):
            data.update({k: str(v)})

    return data






