from random import random
from datetime import datetime


N = 5
values = [int(random() * N * 100) for y in range(N)]
print(values)


t1 = datetime.now()

for i in range(0, N):
    for j in range(N-1, i, -1):
        if values[j-1] > values[j]:
            values[j-1], values[j] = values[j], values[j-1]

t2 = datetime.now()

print("Bubble time:   ", (t2 - t1).total_seconds() * 1000)
print(values)

values_benchmark = [int(random() * N) for y in range(N)]

print(values_benchmark)

t1 = datetime.now()
values_sorted = sorted(values_benchmark)
t2 = datetime.now()

print("Sorted time:   ", (t2 - t1).total_seconds() * 1000)
print(values_sorted)
