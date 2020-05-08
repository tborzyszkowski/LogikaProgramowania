from dane import dane_programu
from sortowanie import sortuj_dane_programu_po_nazwisku

def wypisz():
    for item in dane_programu:
        print(str(item))

def usun():
    pass

menu = {
    1: {"opis": "Wypisz dane na ekran", "funkcja_realizujaca": wypisz},
    2: {"opis": "Usun dane", "funkcja_realizujaca": usun},
    3: {"opis": "Sortuj po nazwisku", "funkcja_realizujaca": sortuj_dane_programu_po_nazwisku},
    9: {"opis": "Koniec programu", "funkcja_realizujaca": exit}
}

def wypisz_menu_item(key):
    print("%d.\t%s" % (key, menu[key]["opis"]))


def wypisz_menu():
    for key in menu:
        wypisz_menu_item(key)


def wybierz_opcje():
    wybor = input("Podaj opcje:")
    wybor_liczba = -1
    try:
        wybor_liczba = int(wybor)
    except ValueError:
       print("Zly wybor")
    if wybor_liczba in menu:
        print("Wybrales opcje nr: %d: %s" % (wybor_liczba, menu[wybor_liczba]["opis"]))
    else:
        print("Nie ma takiej opcji")
    return wybor_liczba


if __name__ == "__main__":
    while True:
        wypisz_menu()
        wybor = wybierz_opcje()
        if wybor > 0:
            menu[wybor]["funkcja_realizujaca"]()