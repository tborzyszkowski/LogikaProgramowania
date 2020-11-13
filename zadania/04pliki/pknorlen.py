import csv
import statistics
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
import numpy as np

with open('pknorlen_akcje.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    counter = 0
    kursy_lista = []
    for row in readCSV:
        kursy_lista.append({"data": row[0], "kurs_max": float(row[5]), "kurs_min": float(row[6])})
        counter += 1
        if counter > 500:
            break

print(counter)
print("Srednia: ", statistics.mean([k["kurs_max"] for k in kursy_lista]))
print("Odch.Std:", statistics.stdev([k["kurs_max"] for k in kursy_lista]))
print("Max: ", max([k["kurs_max"] for k in kursy_lista]))
print("Min:", min([k["kurs_max"] for k in kursy_lista]))

y_es = [k["kurs_max"] for k in kursy_lista]
x_es = range(0,len(y_es))
f_linear = interp1d(x_es, y_es, kind='linear')
# xnew = np.arange(1, len(y_es), 0.1)

plt.plot(x_es, y_es, 'o',
    x_es, f_linear(x_es), '-')
plt.show()