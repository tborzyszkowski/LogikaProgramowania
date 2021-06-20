from math import sqrt


def is_prime(num):
    cnt = 0
    for j in range(2, int(sqrt(num)) + 1):
        cnt += 1
        if (num % j) == 0:
            return (False, cnt)
    return (True, cnt)


if __name__ == "__main__":
    for liczba in range(1000*1000, 1000*1000+100):
        print(liczba, is_prime(liczba))
