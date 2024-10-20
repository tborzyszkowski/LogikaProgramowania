import csv


def wczytaj_dane():
    with open('pknorlen_akcje.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        result = []
        for row in readCSV:
            result.append({"data": row[0], "kurs_max": float(row[5]), "kurs_min": float(row[6])})
    return result

def wypisz_dane(dane):
    for row in dane:
        print(row)

def policz_srednia(dane):
    suma = 0
    for row in dane:
        suma += row["kurs_max"]
    liczba_danych = len(dane)
    return suma / liczba_danych

if __name__ == '__main__':
    dane = wczytaj_dane()
    print("srednia: ", policz_srednia(dane))