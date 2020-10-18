import csv
import statistics

with open('wig_d.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    counter = 0
    volumen_lista = []
    diff_lista = []
    for row in readCSV:
        volumen = float(row[5])
        volumen_lista.append(volumen)
        diff = float(row[2]) - float(row[3])
        diff_lista.append(diff)
        counter += 1
print(counter)
print("Srednia: ", statistics.mean(volumen_lista))
print("Odch.Std:", statistics.stdev(volumen_lista))
print("Srednia: ", statistics.mean(diff_lista))
print("Odch.Std:", statistics.stdev(diff_lista))
