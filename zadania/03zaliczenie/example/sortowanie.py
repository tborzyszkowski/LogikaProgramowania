from dane import *

alfabet = ['a', 'ą', 'b', 'c', 'ć']


def porownaj(str1, str2):
    val1 = list(map(lambda x: alfabet.index(x), str1))
    val2 = list(map(lambda x: alfabet.index(x), str2))
    if val1 > val2:
        return 1
    elif val1 < val2:
        return -1
    else:
        return 0

def porownaj_wiersze(w1, w2):
    if porownaj(w1["nazwisko"], w2["nazwisko"]) > 0:
        return 1
    elif porownaj(w1["nazwisko"], w2["nazwisko"]) < 0:
        return -1
    elif porownaj(w1[kol_imie], w2[kol_imie]) > 0:
        return 1
    elif porownaj(w1[kol_imie], w2[kol_imie]) < 0:
        return -1
    else:
        return 0


def sortuj_dane_programu_po_nazwisku():
    rozmiar_danych = len(dane_programu)
    for i in range(0, rozmiar_danych):
        for j in range(rozmiar_danych - 1, i, -1):
            if porownaj_wiersze(dane_programu[j - 1], dane_programu[j]) > 0:
                dane_programu[j - 1], dane_programu[j] = dane_programu[j], dane_programu[j - 1]


if __name__ == "__main__":
    print(porownaj("aąć", "aąc"))