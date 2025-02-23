# Python code below

def encode_string(string_val):
    encoded_list = []
    prev_char = string_val[0]
    count = 0

    for char in string_val:
        if char != prev_char:
            encoded_list.append((prev_char, count))
            count = 0
        prev_char = char
        count += 1

    encoded_list.append((prev_char, count))

    return encoded_list



def decode_string(encoded_list):
    decoded_str = ""
    for item in encoded_list:
        decoded_str += item[0] * item[1]
    return decoded_str


if __name__ == '__main__':
    example_str = "AAAAABBBBAAA"


    out = encode_string(example_str)
    print(out)

    out_dec = decode_string(out)
    print(out_dec)
