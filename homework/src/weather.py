import requests
import csv
from datetime import datetime
import os
import re
from homework.src import variables


def get_data_weather_api(city, url, key):
    params = {
        'q': city,
        'appid': key,
        'units': 'metric'
            }

    resp = requests.get(url=url, params=params)

    if not resp.ok:
        raise Exception('bad api data!')
    return resp.json()

def generate_filename():
    filename = '{}_{}.csv'.format('Weather', datetime.today().strftime('%d_%m_%Y'))
    return filename

def generate_data_csv(resp, fields):
    data_csv = {}
    for k, v in resp.items():
        if k in fields:
            if type(v).__name__ == 'dict':
                data_csv.update(v)
            elif type(v).__name__ == 'list':
                data_csv.update(v[0])
            else:
                data_csv.update({k: v})
    return data_csv

def get_file(filename, path):
    for _file in os.listdir(path):
        file_found = re.search(r'{}'.format(filename), _file)
        if file_found:
            return file_found

def create_csv(filename, data, path):
    first = True
    dir_file = path + filename

    file = get_file(filename, path)
    if file:
        first = False

    try:
        with open(dir_file, "a") as out_file:
            writer = csv.DictWriter(out_file, delimiter=';', fieldnames=list(data))
            if first:
                writer.writeheader()
                writer.writerow(data)
            else:
                writer.writerow(data)
    except:
        raise Exception('file {} is not created!'.format(filename))

def generate_data_weather(city,
                          fields=variables.FIELDS,
                          url=variables.URL,
                          key=variables.KEY,
                          path=variables.PATH):

    resp = get_data_weather_api(city, url, key)
    filename = generate_filename()
    data_csv = generate_data_csv(resp, fields)
    create_csv(filename, data_csv, path)



if __name__ == '__main__':
    cities = ['Kyiv', 'London']

    for city in cities:
        generate_data_weather(city)

