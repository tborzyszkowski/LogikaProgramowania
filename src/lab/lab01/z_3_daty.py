data1 = (25, 12, 1990)
data2 = (25, 12, 1990)

(d1, m1, r1) = data1
(d2, m2, r2) = data2

if r2 > r1:
    print('Data 1')
elif r2 < r1:
    print('Data 2')
elif m2 > m1:
    print('Data 1')
elif m2 < m1:
    print('Data 2')
elif d2 > d1:
    print('Data 1')
elif d2 < d1:
    print('Data 2')
else:
    print('równe')


dd1 = (r1, m1, d1)
dd2 = (r2, m2, d2)

result = "pierwsza" if dd1 < dd2 else ("druga" if dd1 > dd2 else "równe")
print(result)

if dd1 < dd2:
    result = "pierwsza"
else:
    if dd1 > dd2:
        result = "druga"
    else:
        result = "równe"

print(result)

dl1 = r1 * 10000 + m1 * 100 + d1
dl2 = r2 * 10000 + m2 * 100 + d2

result = "Pierwsza" if dl1 < dl2 else ("Druga" if dl1 > dl2 else "Rowne")
print(result)
