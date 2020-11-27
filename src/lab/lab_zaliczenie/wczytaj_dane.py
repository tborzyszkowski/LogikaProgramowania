import csv


def wczytaj_dane():
    with open('pknorlen_akcje.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        next(readCSV)
        result = []
        for row in readCSV:
            result.append({"data": row[0], "kurs_max": float(row[5]), "kurs_min": float(row[6])})
    return result