
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

def fib(n):
    f0 = 0
    f1 = 1
    if n <= 1:
        return n
    else:
        licznik = 1
        while licznik < n:
            f0, f1 = f1, f1 + f0
            licznik +=1
    return f1


print('0 == fib(0):', 0 == fib(0))
print('1 == fib(1):', 1 == fib(1))
print('1 == fib(2):', 1 == fib(2))
print('2 == fib(3):', 2 == fib(3))
print('377 == fib(14):', 377 == fib(14))

print(fib(350))