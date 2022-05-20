

def czy_liczba_jest_pierwsza(liczba):
    is_prime = True
    candidate = 2
    counter = 0
    while (candidate ** 2 <= liczba) and is_prime:
        if liczba % candidate == 0:
            is_prime = False
        else:
            candidate += 1
        counter += 1
    return {"is_prime": is_prime, "steps": counter}


print(czy_liczba_jest_pierwsza(100))
print(czy_liczba_jest_pierwsza(997))
print(czy_liczba_jest_pierwsza(11587))


# if isPrime:
#     print("TAK")
# else:
#     print("NIE")
# print("Counter:", counter)
