"""
Przykład 5: Wykres kołowy (pie chart)
======================================

OPIS MERYTORYCZNY:
Dane przedstawiają udział rynkowy różnych platform streamingowych
w Polsce w 2024 roku (w procentach subskrybentów).

JAK URUCHOMIĆ:
1. pip install matplotlib
2. python 05_wykres_kolowy.py

JAK MODYFIKOWAĆ:
- Zmień kolory używając listy kolorów
- Użyj parametru 'explode' aby wysunąć wybrane wycinki
- Zmień format etykiet (parametr 'autopct')
- Dodaj cień (parametr 'shadow=True')
"""

import matplotlib.pyplot as plt

# DANE: Udziały platform streamingowych
dane_streaming = [
    {"platforma": "Netflix", "udzial": 35.2},
    {"platforma": "HBO Max", "udzial": 22.5},
    {"platforma": "Disney+", "udzial": 18.3},
    {"platforma": "Prime Video", "udzial": 12.8},
    {"platforma": "Apple TV+", "udzial": 5.4},
    {"platforma": "Inne", "udzial": 5.8}
]

# KROK 1: Przygotowanie danych
platformy = [d["platforma"] for d in dane_streaming]
udzialy = [d["udzial"] for d in dane_streaming]

# KROK 2: Definicja kolorów dla każdego wycinka
# Możemy użyć nazw kolorów lub kodów hex
kolory = ['#E50914',    # Netflix czerwony
          '#7B2CBF',    # HBO Max fioletowy
          '#113CCF',    # Disney+ niebieski
          '#00A8E1',    # Prime Video błękitny
          '#000000',    # Apple TV+ czarny
          '#95a5a6']    # Inne - szary

# KROK 3: Wysunięcie największego wycinka (Netflix)
# explode to krotka określająca jak daleko wysunąć każdy wycinek
# 0 = nie wysuwaj, 0.1 = wysuń trochę
wysuniecie = [0.1, 0, 0, 0, 0, 0]  # Tylko pierwszy wycinek (Netflix) jest wysunięty

# KROK 4: Tworzenie wykresu
plt.figure(figsize=(12, 8))

# plt.pie() tworzy wykres kołowy
# Parametry:
# - udzialy: wartości dla każdego wycinka
# - labels: etykiety wycinków
# - colors: kolory wycinków
# - autopct: format wyświetlania procentów ('%1.1f%%' = jedna cyfra po przecinku + znak %)
# - startangle: kąt początkowy (90 = start od góry)
# - explode: wysunięcie wycinków
# - shadow: cień pod wykresem
# - textprops: właściwości tekstu (rozmiar czcionki, kolor)

wykres = plt.pie(udzialy, 
                 labels=platformy, 
                 colors=kolory,
                 autopct='%1.1f%%',      # Format: 35.2%
                 startangle=90,          # Zaczynamy od góry
                 explode=wysuniecie,     # Wysuń Netflix
                 shadow=True,            # Dodaj cień
                 textprops={'fontsize': 11, 'weight': 'bold'})

# KROK 5: Tytuł wykresu
plt.title('Udziały platform streamingowych w Polsce (2024)', 
          fontsize=16, fontweight='bold', pad=20)

# KROK 6: Dodanie legendy z wartościami bezwzględnymi
# Zakładamy, że mamy 10 milionów subskrybentów łącznie
calkowita_liczba = 10.0  # w milionach
etykiety_legendy = [f'{platforma}: {udzial:.1f}% ({(udzial/100)*calkowita_liczba:.2f}M)' 
                    for platforma, udzial in zip(platformy, udzialy)]

plt.legend(etykiety_legendy, 
          loc='center left', 
          bbox_to_anchor=(1, 0, 0.5, 1),  # Pozycja legendy poza wykresem
          fontsize=10)

# KROK 7: Zapewnienie, że koło jest kołem (nie elipsą)
plt.axis('equal')

plt.tight_layout()
plt.show()

# DODATKOWA ANALIZA
print("\n=== RANKING PLATFORM ===")
# Sortujemy platformy według udziału
posortowane = sorted(dane_streaming, key=lambda x: x["udzial"], reverse=True)
for i, platform in enumerate(posortowane, 1):
    print(f"{i}. {platform['platforma']}: {platform['udzial']}%")

# Oblicz dominację top 3
top3_suma = sum([d["udzial"] for d in posortowane[:3]])
print(f"\nTop 3 platformy mają łącznie: {top3_suma:.1f}% rynku")

# ĆWICZENIE:
# 1. Stwórz wykres pokazujący podział budżetu domowego
# 2. Użyj różnych stylów wyświetlania procentów
# 3. Wysuń wszystkie wycinki poniżej 10%
