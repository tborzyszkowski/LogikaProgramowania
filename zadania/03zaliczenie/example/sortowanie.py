from dane import dane_programu

def sortuj_dane_programu_po_nazwisku():
    fst = dane_programu[0]
    dane_programu[0] = dane_programu[1]
    dane_programu[1] = fst