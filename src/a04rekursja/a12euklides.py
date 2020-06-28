
def euklides(a, b):
    if b == 0:
        return a
    else:
        return euklides(b, a % b)


if __name__ == "__main__":
    result = euklides(997, 999 * 998 * 13)
    print(result)