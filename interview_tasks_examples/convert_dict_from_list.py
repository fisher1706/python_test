# Python3 code to demonstrate
# conversion of lists to dictionary
# using dictionary comprehension

# initializing lists
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]

# Printing original keys-value lists
print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))

# using dictionary comprehension
# to convert lists to dictionary
# res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
res = dict(zip(test_keys, test_values))

# Printing resultant dictionary
print("Resultant dictionary is : " + str(res))


result_dict = dict.fromkeys(test_keys)
print(result_dict)
