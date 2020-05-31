from dane import dane_programu


def szukaj_po_nr_buta():
    nr_buta = int(input('Podaj nr buta: '))

    wynik = []
    for wiersz in dane_programu:
        if wiersz["but"] == nr_buta:
            wynik.append(wiersz)
    return wynik

def wypisz_po_nr_buta():
    print(szukaj_po_nr_buta())
