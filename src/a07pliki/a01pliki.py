# operacje na plikach

f = open('plik.txt', 'w')
print(f)

f.write('1234567890abcdefghijk\n')
f.write('Ala ma kota\n')
t = ('a', 1, 3.14)
f.write(str(t))
f.write('\n')
f.flush()
f.write('Ola ma kota\n')
f.close()

print(f)

f = open('plik.txt', 'r')

print('Pocz   : ', f.tell())
s = f.read(10)
print(s)
print('Read 1 : ', f.tell())
print(f.read())
print('Read 2 : ', f.tell())
f.seek(3, 0)
print('Read 3 : ', f.tell())
print(f.read(3))
print('Seek 2 : ', f.tell())
print(f.read())

f.close()

f = open(r'a01pliki.py', 'r')
lista = f.readlines()
print("".join(lista))

f.close()
