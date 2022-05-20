
# def silnia(n):
#     licznik = 1
#     wynik = 1
#     while licznik <= n:
#         wynik = wynik * licznik
#         licznik = licznik + 1
#     return wynik

def silnia(n):
    if n == 1:
        return 1
    else:
        return n * silnia(n-1)

print('1 == silnia(1):', 1 == silnia(1))
print('2 == silnia(2):', 2 == silnia(2))
print('6 == silnia(3):', 6 == silnia(3))
print('24 == silnia(4):', 24 == silnia(4))
print('120 == silnia(5):', 120 == silnia(5))