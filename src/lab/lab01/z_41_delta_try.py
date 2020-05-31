from math import sqrt

a = 0
b = 0
c = 1

if a == 0:
    print("to nie jest rownanie kwadratowe")
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("brak rozwazan")
    elif delta == 0:
        print("x = ", -b/(2.0*a))
    else:
        print("x1 = ", (-b - sqrt(delta)) / (2.0 * a))
        print("x2 = ", (-b + sqrt(delta)) / (2.0 * a))

