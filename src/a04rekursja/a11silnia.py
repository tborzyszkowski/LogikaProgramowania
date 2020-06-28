
def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)


if __name__ == "__main__":
    for n in range(100):
        print(n, ": ", silnia(n))