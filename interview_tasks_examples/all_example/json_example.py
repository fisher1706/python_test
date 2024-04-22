import json


data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}


if __name__ == '__main__':
    json_string = json.dumps(data)
    new_data = json.loads(json_string)

    print(type(data))
    print(type(json_string))
    print(type(new_data))

    print(json_string)
    print(new_data)
