from dane import dane_programu


def porownaj_wiersze(w1, w2):
    if w1["nazwisko"] > w2["nazwisko"]:
        return 1
    elif w1["nazwisko"] < w2["nazwisko"]:
        return -1
    elif w1["imie"] > w2["imie"]:
        return 1
    elif w1["imie"] < w2["imie"]:
        return -1
    else:
        return 0


def sortuj_dane_programu_po_nazwisku():
    rozmiar_danych = len(dane_programu)
    for i in range(0, rozmiar_danych):
        for j in range(rozmiar_danych - 1, i, -1):
            if porownaj_wiersze(dane_programu[j - 1], dane_programu[j]) == -1:
                dane_programu[j - 1], dane_programu[j] = dane_programu[j], dane_programu[j - 1]
