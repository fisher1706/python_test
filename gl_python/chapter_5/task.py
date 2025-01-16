def all_primes_up_to_one(number):
    out = []
    for num in range(2, number):
        for factor in range(2, int(num**0.5)+1):
            if num % factor == 0:
                break
        else:
            out.append(num)
    return out


def all_primes_up_to_two(number):
    primes = [2]
    for num in range(3, number):
        sqrt_num = num**0.5
        for factor in primes:
            if num % factor == 0:
                break
            if factor > sqrt_num:
                primes.append(num)
                break
    return primes


if __name__ == '__main__':
    print(all_primes_up_to_one(100))
    print(all_primes_up_to_two(100))
