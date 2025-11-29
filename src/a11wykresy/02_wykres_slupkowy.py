"""
Przykład 2: Wykres słupkowy (bar chart)
========================================

OPIS MERYTORYCZNY:
Dane przedstawiają najpopularniejsze języki programowania według ankiety
przeprowadzonej wśród 10000 programistów w 2024 roku.

JAK URUCHOMIĆ:
1. Upewnij się, że masz zainstalowaną bibliotekę matplotlib:
   pip install matplotlib
2. Uruchom skrypt: python 02_wykres_slupkowy.py

JAK MODYFIKOWAĆ:
- Dodaj więcej języków programowania do danych
- Zmień kolory słupków (parametr 'color')
- Wypróbuj wykres poziomy używając plt.barh() zamiast plt.bar()
- Zmień szerokość słupków parametrem 'width'
"""

import matplotlib.pyplot as plt

# DANE: Popularność języków programowania (procent respondentów)
dane_jezykow = [
    {"jezyk": "Python", "popularnosc": 68.5},
    {"jezyk": "JavaScript", "popularnosc": 65.3},
    {"jezyk": "Java", "popularnosc": 45.7},
    {"jezyk": "C#", "popularnosc": 34.2},
    {"jezyk": "C++", "popularnosc": 28.9},
    {"jezyk": "TypeScript", "popularnosc": 25.6},
    {"jezyk": "PHP", "popularnosc": 22.1},
    {"jezyk": "Go", "popularnosc": 18.4}
]

# KROK 1: Przygotowanie danych
jezyki = [rekord["jezyk"] for rekord in dane_jezykow]
popularnosc = [rekord["popularnosc"] for rekord in dane_jezykow]

# KROK 2: Tworzenie wykresu słupkowego
plt.figure(figsize=(12, 7))

# plt.bar() tworzy wykres słupkowy pionowy
# Pierwszy argument: pozycje słupków (nazwy języków)
# Drugi argument: wysokości słupków (wartości popularności)
# color='skyblue' - kolor słupków
# edgecolor='navy' - kolor obramowania słupków
# linewidth=1.5 - grubość obramowania
slupki = plt.bar(jezyki, popularnosc, 
                 color='skyblue', 
                 edgecolor='navy', 
                 linewidth=1.5)

# KROK 3: Dodanie wartości na słupkach
# Pętla dodaje etykiety z wartościami na każdym słupku
for i, (jezyk, wartosc) in enumerate(zip(jezyki, popularnosc)):
    # plt.text() dodaje tekst w określonym miejscu
    # i - pozycja X (numer słupka)
    # wartosc + 1 - pozycja Y (nad słupkiem)
    # f'{wartosc}%' - formatowany tekst
    # ha='center' - wyrównanie poziome do środka
    # va='bottom' - wyrównanie pionowe do dołu
    plt.text(i, wartosc + 1, f'{wartosc}%', 
             ha='center', va='bottom', fontsize=10, fontweight='bold')

# KROK 4: Kolorowanie najlepszego wyniku
# Znajdujemy indeks najwyższej wartości
max_index = popularnosc.index(max(popularnosc))
# Zmieniamy kolor tego słupka na złoty
slupki[max_index].set_color('gold')
slupki[max_index].set_edgecolor('orange')

# KROK 5: Opisy wykresu
plt.title('Najpopularniejsze języki programowania w 2024 roku', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Język programowania', fontsize=12)
plt.ylabel('Popularność (%)', fontsize=12)

# KROK 6: Dodatkowe ustawienia
# Ustawiamy zakres osi Y od 0 do 80
plt.ylim(0, 80)

# Dodajemy siatkę tylko dla osi Y
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Obracamy etykiety osi X dla lepszej czytelności
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()

# ĆWICZENIE DO SAMODZIELNEGO WYKONANIA:
# 1. Zmień wykres na poziomy (użyj plt.barh())
# 2. Dodaj drugi rok danych i stwórz wykres porównawczy
# 3. Posortuj języki według popularności malejąco
