str1 = "cats"
str2 = "dog"

max_len = max(len(str1), len(str2))
str1_padded = str1.ljust(max_len, 'A')
print(str1_padded)

str2_padded = str2.ljust(max_len, 'A')
print(str2_padded)

result = [str1_padded[i] + str2_padded[i] for i in range(max_len)]
print(result)
# Output: ['cd', 'ao', 'tg', 'sA']
