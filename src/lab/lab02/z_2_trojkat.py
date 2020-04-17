

def trojkat(n):
    for row in range(n):
        for col in range(row+1):
            print('*', end='')
        print()


trojkat(20)