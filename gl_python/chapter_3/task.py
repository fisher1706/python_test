# Python code below
hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}


# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hex_to_dec_one(hex_num):
    for char in hex_num:
        if char not in hexNumbers:
            return None

    if len(hex_num) == 3:
        return hexNumbers[hex_num[0]] * 256 + hexNumbers[hex_num[1]] * 16 + hexNumbers[hex_num[2]]

    if len(hex_num) == 2:
        return hexNumbers[hex_num[0]] * 16 + hexNumbers[hex_num[1]]

    if len(hex_num) == 1:
        return hexNumbers[hex_num[0]]


def hex_to_dec_two(hex_num):
    for char in hex_num:
        if char not in hexNumbers:
            return None

    converted = 0
    exponent = len(hex_num) - 1

    for char in hex_num:
        converted = converted + (hexNumbers[char] * (16 * exponent))
        exponent = exponent + 1

    return converted


if __name__ == '__main__':
    print(hex_to_dec_one('0'))
    print(hex_to_dec_one('589'))

    print(hex_to_dec_two('0'))
    print(hex_to_dec_two('589'))

