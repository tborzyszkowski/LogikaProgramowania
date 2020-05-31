from dane import dane_programu
from sortowanie import sortuj_dane_programu_po_nazwisku, porownaj_wiersze

def wypisz():
    for item in dane_programu:
        print(str(item))


def usun():
    nazwisko = input('Podaj nazwisko: ')
    imie = input('Podaj imię: ')

    usuniete = False
    for wiersz in dane_programu:
        if wiersz["nazwisko"] == nazwisko and wiersz["imie"] == imie and not usuniete:
            dane_programu.remove(wiersz)
            print("Dane: ", wiersz, " USUNIĘTE")
            usuniete = True
            break
    if not usuniete:
        print("Brak danych dla", nazwisko, imie)


def dodaj_wiersz():
    nowy_wiersz = {}
    nowy_wiersz["nazwisko"] = input('Podaj nazwisko: ')
    nowy_wiersz["imie"]= input('Podaj imię: ')
    nowy_wiersz["wiek"] = int(input('Podaj wiek: '))
    nowy_wiersz["but"] = int(input('Podaj but: '))
    nowy_wiersz["kolor_oczu"] = 1
    dane_programu.append(nowy_wiersz)
    print("Dodano nowe dane: ", nowy_wiersz)


def zmien_wiek():
    nazwisko = input('Podaj nazwisko: ')
    imie = input('Podaj imię: ')

    dane_do_zmiany = None
    for wiersz in dane_programu:
        if wiersz["nazwisko"] == nazwisko and wiersz["imie"] == imie and dane_do_zmiany is None:
            dane_do_zmiany = wiersz
            print("Znaleziono wiersz: ", dane_do_zmiany)
            break
    if dane_do_zmiany is not None:
        dane_do_zmiany["wiek"] = int(input('Podaj nowy wiek: '))
        print("Wiek zaktualizowany")
    else:
        print("Brak danych do aktualizacji")


menu = {
    1: {"opis": "Wypisz dane na ekran", "funkcja_realizujaca": wypisz},
    2: {"opis": "Utwórz wiersz", "funkcja_realizujaca": dodaj_wiersz},
    3: {"opis": "Usun dane", "funkcja_realizujaca": usun},
    4: {"opis": "Zmień wiek", "funkcja_realizujaca": zmien_wiek},
    5: {"opis": "Sortuj po nazwisku", "funkcja_realizujaca": sortuj_dane_programu_po_nazwisku},
    9: {"opis": "Koniec programu", "funkcja_realizujaca": exit}
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
        if wybor > 0:
            menu[wybor]["funkcja_realizujaca"]()