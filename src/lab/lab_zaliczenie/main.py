def stub():
    pass

menu = {
    1: {"opis": "Wczytaj dane", "funkcja": stub},
    2: {"opis": "Liczba wierszy", "funkcja": stub},
    3: {"opis": "Wykres", "funkcja": stub},
    4: {"opis": "Statystyka danych", "funkcja": stub},
    0: {"opis": "Koniec programu", "funkcja": exit}
}


def wypisz_menu_item(key):
    print("%d.\t%s" % (key, menu[key]["opis"]))


def wypisz_menu():
    for key in menu:
        wypisz_menu_item(key)


def wybierz_opcje():
    wybor = input("Podaj opcje: ")
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
        if wybor >= 0:
            menu[wybor]["funkcja"]()