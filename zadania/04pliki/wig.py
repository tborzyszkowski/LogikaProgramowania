import csv
import statistics

with open('wig_d.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    counter = 0
    volumen_lista = []
    for row in readCSV:
        print(counter)
        volumen = float(row[1])
        volumen_lista.append(volumen)
        counter += 1

print(statistics.mean(volumen_lista))
print(statistics.mean([1,2,3,4,5,6,7,8,9,10]))
