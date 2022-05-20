from math import sqrt
a = 1
b = 7
c = 12

if a == 0:
    if b == 0:
        if c == 0:
            print('Duzo')
        else:
            print("Brak")
    else:
        print('x = ', (-c)/(b*1.0))
else:
    d = b * b - 4 * a * c
    if d > 0:
        dd = sqrt(d)
        print('x1 = ', (-b - dd)/(2*a))
        print('x2 = ', (-b + dd)/(2*a))
    elif d == 0:
        print('x = ', (-b)/(2.0*a))
    else:
        dd = sqrt(-d)*1j
        print('x1 = ', (-b - dd)/(2*a))
        print('x2 = ', (-b + dd)/(2*a))