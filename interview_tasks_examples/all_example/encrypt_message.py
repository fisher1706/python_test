def encrypt_message(message):
    orignal = ['a', 'b', 'c', ' ']
    encrypt = ['z', 'y', 'x', '$']
    i = 0
    while i < len(orignal) and i < len(encrypt):
        message = message.replace(orignal[i], encrypt[i])
        i += 1
    return message


if __name__ == '__main__':
    unencrypted_message = "I want to become a Data Scientist."

    print("unencrypted message = ", unencrypted_message)
    print("encrypted message = ", encrypt_message(unencrypted_message))
