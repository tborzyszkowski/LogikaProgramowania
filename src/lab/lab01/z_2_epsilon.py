epsilon = 1.0
poprzedni_epsilon = epsilon
licznik = 0
limit = 10 * 1000

while epsilon > 0.0 and licznik < limit:
    poprzedni_epsilon = epsilon
    epsilon = epsilon / 2.0
    # licznik = licznik + 1
    licznik += 1

print("Epsilon:", poprzedni_epsilon)
print("Licznik:", licznik)