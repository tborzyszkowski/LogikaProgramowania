from functools import reduce
import math


def is_prime(num):
    for j in range(2, int(math.sqrt(num)) + 1):
        if (num % j) == 0:
            return False
    return True


def euklides(a, b):
    counter = 0
    while a != b: # a rozne od b
        if a > b:
            a = a % b
            # a -= b # a = a - b
        else:
            b = b % a
            # b -= a
        counter += 1
        if counter % 10000 == 0:
            print(counter, a ,b)
    return a


def euklides2(*args):
    return reduce(euklides, args)


if __name__ == "__main__":
    fst = 1000000
    snd = 1001000
    big_primes = [el for el in filter(is_prime, range(fst, snd))]
    print(len(big_primes), big_primes)
    print(euklides(big_primes[0]*big_primes[1], big_primes[0]*big_primes[1]*big_primes[2]))

    # a = 2 * 3 * 7
    # b = 2 * 7 * 13
    # c = 3 * 7
    # result = euklides2(a, b, c)
    # print(result)
