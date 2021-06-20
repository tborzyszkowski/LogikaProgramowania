from datetime import datetime


def fib_linear(n):
    f1 = 0
    f2 = 1
    k = n - 2
    if n < 2:
        f2 = n
    else:
        while k >= 0:
            f2, f1, k = f1 + f2, f2, k-1
    return f2


def fib_rek(n):
    if n < 2:
        return n
    else:
        return fib_rek(n - 1) + fib_rek(n - 2)


def mult(m1, m2):
    result = [[0, 0], [0, 0]]
    result[0][0] = m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0]
    result[0][1] = m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1]
    result[1][0] = m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0]
    result[1][1] = m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1]
    return result


def fibMatrixPower(m, n):
    if n == 1:
        return m
    elif n % 2 == 0:
        return fibMatrixPower(mult(m, m), n / 2)
    else:
        return mult(m, fibMatrixPower(mult(m, m), (n-1) / 2))


def fibonacciFast(n):
    result = [[1, 1], [1, 0]]
    return fibMatrixPower(result, n)[0][1]


if __name__ == "__main__":
    n = 1000*1000
    t1 = datetime.now()
    result = fib_linear(n)
    t2 = datetime.now()
    # print(result)
    print("fib_linear time:   ", (t2 - t1).total_seconds() * 1000)
    t1 = datetime.now()
    result = fibonacciFast(n)
    t2 = datetime.now()
    # print(result)
    print("fibonacciFast time:   ", (t2 - t1).total_seconds() * 1000)
