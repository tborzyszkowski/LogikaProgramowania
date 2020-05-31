from random import random

N = 100
values = [int(random() * 1000) for y in range(N)]
# values = [1 for y in range(N)]
# values = [1, 2, 3, 4, 5, 100, 99, 33]
print(values)

value_max = values[0]
value_min = values[0]

for element in values[1:]:
    if element > value_max:
        value_max = element
    if element < value_min:
        value_min = element

print("max:", value_max)
print("min:", value_min)
