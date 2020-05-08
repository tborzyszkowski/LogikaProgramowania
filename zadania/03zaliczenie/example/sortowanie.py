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


def sortuj_dane_programu_po_nazwisku(poronanie):
    wyn = porownaj_wiersze(dane_programu[0], dane_programu[1])
    if wyn > 0:
        print("Pierwszy wiekszy")
    elif wyn < 0:
        print("Drugi wiekszy")
    else:
        print("Są rowne")