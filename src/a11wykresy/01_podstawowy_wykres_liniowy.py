"""
Przykład 1: Podstawowy wykres liniowy
=====================================

OPIS MERYTORYCZNY:
Dane przedstawiają miesięczną sprzedaż lodów w małej lodziarni w ciągu roku.
Widać wyraźną sezonowość - wzrost sprzedaży latem, spadek zimą.

JAK URUCHOMIĆ:
1. Upewnij się, że masz zainstalowaną bibliotekę matplotlib:
   pip install matplotlib
2. Uruchom skrypt: python 01_podstawowy_wykres_liniowy.py
3. Pojawi się okno z wykresem

JAK MODYFIKOWAĆ:
- Zmień wartości w liście 'dane_sprzedazy' aby zobaczyć inne trendy
- Zmień kolor linii parametrem 'color' (np. 'red', 'green', 'blue')
- Dodaj więcej miesięcy do danych
- Zmień grubość linii parametrem 'linewidth'
"""

import matplotlib.pyplot as plt

# DANE: Sprzedaż lodów w poszczególnych miesiącach (w tysiącach sztuk)
dane_sprzedazy = [
    {"miesiac": "Styczeń", "sprzedaz": 12},
    {"miesiac": "Luty", "sprzedaz": 15},
    {"miesiac": "Marzec", "sprzedaz": 25},
    {"miesiac": "Kwiecień", "sprzedaz": 45},
    {"miesiac": "Maj", "sprzedaz": 78},
    {"miesiac": "Czerwiec", "sprzedaz": 120},
    {"miesiac": "Lipiec", "sprzedaz": 150},
    {"miesiac": "Sierpień", "sprzedaz": 145},
    {"miesiac": "Wrzesień", "sprzedaz": 95},
    {"miesiac": "Październik", "sprzedaz": 55},
    {"miesiac": "Listopad", "sprzedaz": 28},
    {"miesiac": "Grudzień", "sprzedaz": 18}
]

# KROK 1: Przygotowanie danych do wykresu
# Rozdzielamy dane na dwie listy: nazwy miesięcy i wartości sprzedaży
miesiace = [rekord["miesiac"] for rekord in dane_sprzedazy]
sprzedaz = [rekord["sprzedaz"] for rekord in dane_sprzedazy]

# KROK 2: Tworzenie wykresu
# plt.figure() tworzy nowe "płótno" do rysowania wykresu
# figsize określa rozmiar w calach (szerokość, wysokość)
plt.figure(figsize=(12, 6))

# KROK 3: Rysowanie linii
# plt.plot() tworzy wykres liniowy
# Pierwszy argument: oś X (miesiące)
# Drugi argument: oś Y (wartości sprzedaży)
# marker='o' dodaje kropki w miejscach danych punktów
# color='blue' ustawia kolor linii
# linewidth=2 określa grubość linii
plt.plot(miesiace, sprzedaz, marker='o', color='blue', linewidth=2, label='Sprzedaż lodów')

# KROK 4: Dodawanie opisów
# plt.title() - tytuł wykresu
plt.title('Miesięczna sprzedaż lodów w lodziarni "Arktyka" - rok 2024', fontsize=16, fontweight='bold')

# plt.xlabel() - opis osi X
plt.xlabel('Miesiąc', fontsize=12)

# plt.ylabel() - opis osi Y
plt.ylabel('Sprzedaż (tys. sztuk)', fontsize=12)

# KROK 5: Dodatkowe ustawienia
# plt.grid() dodaje siatkę ułatwiającą odczyt wartości
# alpha=0.3 ustawia przezroczystość siatki (0=niewidoczna, 1=pełna)
plt.grid(True, alpha=0.3)

# plt.legend() pokazuje legendę (etykiety z wykresu)
plt.legend()

# plt.xticks() obraca etykiety osi X o 45 stopni dla lepszej czytelności
plt.xticks(rotation=45)

# plt.tight_layout() automatycznie dopasowuje układ, aby etykiety się nie nakładały
plt.tight_layout()

# KROK 6: Wyświetlanie wykresu
# plt.show() otwiera okno z wykresem
plt.show()

# DODATKOWE INFORMACJE:
# Jeśli chcesz zapisać wykres do pliku zamiast go wyświetlać, użyj:
# plt.savefig('wykres_sprzedazy.png', dpi=300, bbox_inches='tight')
# przed plt.show()
