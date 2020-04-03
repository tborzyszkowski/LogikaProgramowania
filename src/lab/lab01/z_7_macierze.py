from random import random

N = 2

m1 = [
        [(1 if i == j else 0) for j in range(N)]
        for i in range(N)
     ]
m2 = [[int(random() * 100) for y in range(N)] for x in range(N)]

print("m1:")
for row in m1:
    print(row)

print("\n-----------\n")
print("m2:")
for row in m2:
    print(row)
print("\n-----------\n")
wynik = [[0 for y in range(N)] for x in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            wynik[i][j] += m1[i][k] * m2[k][j]

for row in wynik:
    print(row)
