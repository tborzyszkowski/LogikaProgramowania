from functools import reduce


def min_for_two(a, b):
    return a if a < b else b


def min_for_n(*args):
    return reduce(min_for_two, args)


if __name__ == "__main__":
    print(min_for_n(6, 5, 7, 3, 8, 2, 9, 10, 1))
