"""
Przykład 3: Wiele linii na jednym wykresie
===========================================

OPIS MERYTORYCZNY:
Dane przedstawiają miesięczne ceny akcji trzech polskich spółek giełdowych:
PKN Orlen, PZU oraz PGE w 2024 roku. Pozwala to na porównanie trendów.

JAK URUCHOMIĆ:
1. Upewnij się, że masz zainstalowaną bibliotekę matplotlib:
   pip install matplotlib
2. Uruchom skrypt: python 03_wiele_linii.py

JAK MODYFIKOWAĆ:
- Dodaj więcej spółek
- Zmień style linii (np. '--' dla przerywanej, ':' dla kropkowanej)
- Zmień kolory używając nazw lub kodów hex (np. '#FF5733')
- Dodaj markery (np. 'o', 's', '^', 'D')
"""

import matplotlib.pyplot as plt

# DANE: Miesięczne ceny akcji trzech spółek (w PLN)
dane_gieldowe = [
    {"miesiac": "Sty", "orlen": 65.5, "pzu": 42.3, "pge": 8.2},
    {"miesiac": "Lut", "orlen": 67.2, "pzu": 43.1, "pge": 8.5},
    {"miesiac": "Mar", "orlen": 70.8, "pzu": 41.8, "pge": 8.1},
    {"miesiac": "Kwi", "orlen": 68.5, "pzu": 44.5, "pge": 8.9},
    {"miesiac": "Maj", "orlen": 72.3, "pzu": 45.2, "pge": 9.3},
    {"miesiac": "Cze", "orlen": 75.1, "pzu": 46.8, "pge": 9.8},
    {"miesiac": "Lip", "orlen": 73.8, "pzu": 45.5, "pge": 9.5},
    {"miesiac": "Sie", "orlen": 76.5, "pzu": 47.2, "pge": 10.1},
    {"miesiac": "Wrz", "orlen": 74.2, "pzu": 46.1, "pge": 9.7},
    {"miesiac": "Paź", "orlen": 77.9, "pzu": 48.3, "pge": 10.5},
    {"miesiac": "Lis", "orlen": 79.5, "pzu": 49.1, "pge": 10.8},
    {"miesiac": "Gru", "orlen": 81.2, "pzu": 50.5, "pge": 11.2}
]

# KROK 1: Przygotowanie danych
miesiace = [rekord["miesiac"] for rekord in dane_gieldowe]
ceny_orlen = [rekord["orlen"] for rekord in dane_gieldowe]
ceny_pzu = [rekord["pzu"] for rekord in dane_gieldowe]
ceny_pge = [rekord["pge"] for rekord in dane_gieldowe]

# KROK 2: Tworzenie wykresu
plt.figure(figsize=(14, 8))

# KROK 3: Rysowanie trzech linii
# Każda linia ma inny kolor, styl i marker

# Linia 1: PKN Orlen (niebieski, ciągła linia, kółka)
plt.plot(miesiace, ceny_orlen, 
         color='#1f77b4',      # Niebieski (kod hex)
         linestyle='-',         # Ciągła linia
         marker='o',            # Kółka w punktach danych
         linewidth=2.5,         # Grubość linii
         markersize=8,          # Rozmiar markerów
         label='PKN Orlen')     # Etykieta dla legendy

# Linia 2: PZU (zielony, przerywana, kwadraty)
plt.plot(miesiace, ceny_pzu, 
         color='#2ca02c',       # Zielony
         linestyle='--',        # Linia przerywana
         marker='s',            # Kwadraty
         linewidth=2.5,
         markersize=8,
         label='PZU')

# Linia 3: PGE (czerwony, kropkowana, trójkąty)
plt.plot(miesiace, ceny_pge, 
         color='#d62728',       # Czerwony
         linestyle='-.',        # Linia kropka-kreska
         marker='^',            # Trójkąty
         linewidth=2.5,
         markersize=8,
         label='PGE')

# KROK 4: Dodawanie tytułu i opisów osi
plt.title('Porównanie cen akcji wybranych spółek GPW w 2024 roku', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Miesiąc', fontsize=13)
plt.ylabel('Cena akcji (PLN)', fontsize=13)

# KROK 5: Legenda
# loc='upper left' - pozycja legendy w lewym górnym rogu
# framealpha=0.9 - przezroczystość tła legendy
# shadow=True - dodaje cień
plt.legend(loc='upper left', fontsize=11, framealpha=0.9, shadow=True)

# KROK 6: Siatka
plt.grid(True, alpha=0.3, linestyle='--', linewidth=0.7)

# KROK 7: Dodanie poziomej linii referencyjnej
# np. średnia cena Orlenu
srednia_orlen = sum(ceny_orlen) / len(ceny_orlen)
plt.axhline(y=srednia_orlen, color='blue', linestyle=':', linewidth=1.5, alpha=0.5, 
            label=f'Średnia Orlen: {srednia_orlen:.2f} PLN')

# Aktualizujemy legendę po dodaniu linii referencyjnej
plt.legend(loc='upper left', fontsize=11, framealpha=0.9, shadow=True)

plt.tight_layout()
plt.show()

# ZADANIE DO PRZEMYŚLENIA:
# Która spółka miała najlepszy wzrost w ciągu roku?
# Oblicz wzrost procentowy: ((cena_końcowa - cena_początkowa) / cena_początkowa) * 100
print("\n=== ANALIZA WZROSTU CEN ===")
for nazwa, ceny in [("PKN Orlen", ceny_orlen), ("PZU", ceny_pzu), ("PGE", ceny_pge)]:
    wzrost = ((ceny[-1] - ceny[0]) / ceny[0]) * 100
    print(f"{nazwa}: {wzrost:.2f}% wzrostu")
