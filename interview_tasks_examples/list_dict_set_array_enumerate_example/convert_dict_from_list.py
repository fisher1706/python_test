"""
conversion of lists to dictionary using dictionary comprehension_and_generators
"""

if __name__ == "__main__":
    test_keys = ["Rash", "Kil", "Varsha"]
    test_values = [1, 4, 5]

    # using dictionary comprehension_and_generators
    res_one = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
    print(res_one)

    # to convert lists to dictionary
    res_two = dict(zip(test_keys, test_values))
    print(res_two)

    # Printing resultant dictionary
    result_dict = dict.fromkeys(test_keys)
    print(result_dict)
