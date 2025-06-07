a = 997

b = 1
jest = False

while b <= a and not jest:
    if b * b == a:
        jest = True
        print("Wynik: ", b)
    else:
        b = b + 1

if not jest:
    print("Wynik: brak")