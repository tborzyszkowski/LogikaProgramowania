from functools import reduce


def min_for_two(a, b):
    return a if a < b else b


def min_for_n(*args):
    return reduce(min_for_two, args)

def min_for_new(*args):
    if len(args) == 1:
        return args[0]
    min = args[0]
    for arg in args:
        min = min_for_two(arg, min)
    return min


if __name__ == "__main__":
    print(min_for_n(6, 5, 7, 3, 8, 2, 9, 10, 100))
    print(min_for_new(6, 5, 7, 3, 8, 2, 9, 10, 100))
