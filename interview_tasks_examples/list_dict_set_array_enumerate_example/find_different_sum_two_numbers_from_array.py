def find_different_sum(array, number):
    left = 0
    right = len(array) - 1

    while True:
        try:
            amount = array[left] + array[right]
            if amount > number:
                right -= 1
            elif amount < number:
                left += 1
            elif amount == number:
                print(array[left], array[right])
                break
        except Exception as e:
            print(e)
            print("Zero")
            break


if __name__ == "__main__":
    data = [-4, -1, 0, 2, 3, 4, 7, 9]
    k = 1

    find_different_sum(data, k)
