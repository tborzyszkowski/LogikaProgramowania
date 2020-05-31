from functools import reduce
from dane import dane_programu

def sredni_wiek():
    lista_wiek = [dane["wiek"] for dane in dane_programu]
    liczba_danych = len(lista_wiek)
    # suma = 0
    # for w in lista_wiek:
    #     suma = suma + w
    suma =reduce(lambda x, y: x + y, lista_wiek)
    return (1.0 * suma) / liczba_danych


def wypisz_sredni_wiek():
    print("Sredni wiek: %.3f" % sredni_wiek())