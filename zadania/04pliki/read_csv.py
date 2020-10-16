import csv

with open('plik.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    counter = 0
    suma_wieku = 0
    for row in readCSV:
        # print(row)
        # print(row[0])
        print(row[0],row[1],row[2],)
        suma_wieku += int(row[2])
        counter+=1
    print("Suma wieku:", suma_wieku)
    print("Licznik:", counter)
    print("Sredni wiek:", suma_wieku*1.0/counter)