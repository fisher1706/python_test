def encrypt_message(message):
    original = ["a", "b", "c", " "]
    encrypt = ["z", "y", "x", "$"]
    i = 0
    while i < len(original) and i < len(encrypt):
        message = message.replace(original[i], encrypt[i])
        i += 1
    return message


if __name__ == "__main__":
    unencrypted_message = "I want to become a Data Scientist."

    print("unencrypted message = ", unencrypted_message)
    print("encrypted message = ", encrypt_message(unencrypted_message))
