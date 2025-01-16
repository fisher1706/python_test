import json


def encode_string(string_val):
    encoded_list = []
    prev_char = None
    count = 0
    for char in string_val:
        if prev_char != char and prev_char is not None:
            encoded_list.append((prev_char, count))
            count = 0
        prev_char = char
        count = count + 1
    encoded_list.append((prev_char, count))
    return encoded_list


def decode_string(encoded_list):
    decoded_str = ''
    for item in encoded_list:
        decoded_str = decoded_str + item[0] * item[1]
    return decoded_str


def encode_file(filename, new_filename):
    with open(filename, 'r') as f:
        data = encode_string(f.read())

    with open(new_filename, 'w') as f:
        f.write(json.dumps(data))


def decode_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return decode_string(json.loads(data))

