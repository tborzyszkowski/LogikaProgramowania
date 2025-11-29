"""
Przykład 7: Wykres słupkowy grupowany
======================================

OPIS MERYTORYCZNY:
Dane przedstawiają porównanie sprzedaży trzech produktów (smartfony, laptopy, tablety)
w czterech kwartałach roku 2024 dla sklepu elektronicznego.

JAK URUCHOMIĆ:
1. pip install matplotlib numpy
2. python 07_grupowany_slupkowy.py

JAK MODYFIKOWAĆ:
- Zmień szerokość słupków
- Dodaj więcej kategorii lub produktów
- Zmień na wykres skumulowany (stacked bar chart)
- Eksperymentuj z różnymi kolorami
"""

import matplotlib.pyplot as plt
import numpy as np

# DANE: Sprzedaż produktów w poszczególnych kwartałach (w tysiącach sztuk)
dane_sprzedazy = [
    {"kwartal": "Q1 2024", "smartfony": 145, "laptopy": 89, "tablety": 56},
    {"kwartal": "Q2 2024", "smartfony": 168, "laptopy": 102, "tablety": 64},
    {"kwartal": "Q3 2024", "smartfony": 192, "laptopy": 115, "tablety": 71},
    {"kwartal": "Q4 2024", "smartfony": 234, "laptopy": 138, "tablety": 85}
]

# KROK 1: Przygotowanie danych
kwartaly = [d["kwartal"] for d in dane_sprzedazy]
smartfony = [d["smartfony"] for d in dane_sprzedazy]
laptopy = [d["laptopy"] for d in dane_sprzedazy]
tablety = [d["tablety"] for d in dane_sprzedazy]

# KROK 2: Ustawienie pozycji słupków
# np.arange tworzy tablicę liczb [0, 1, 2, 3] dla 4 kwartałów
x = np.arange(len(kwartaly))

# Szerokość pojedynczego słupka
width = 0.25

# KROK 3: Tworzenie wykresu
fig, ax = plt.subplots(figsize=(14, 8))

# KROK 4: Rysowanie trzech grup słupków
# Każda grupa jest przesunięta o 'width' w prawo

# Słupki dla smartfonów (najbardziej na lewo)
slupki1 = ax.bar(x - width, smartfony, width, 
                 label='Smartfony',
                 color='#3498db',
                 edgecolor='navy',
                 linewidth=1.5)

# Słupki dla laptopów (w środku)
slupki2 = ax.bar(x, laptopy, width, 
                 label='Laptopy',
                 color='#e74c3c',
                 edgecolor='darkred',
                 linewidth=1.5)

# Słupki dla tabletów (najbardziej na prawo)
slupki3 = ax.bar(x + width, tablety, width, 
                 label='Tablety',
                 color='#2ecc71',
                 edgecolor='darkgreen',
                 linewidth=1.5)

# KROK 5: Dodanie wartości nad słupkami
# Funkcja pomocnicza do dodawania etykiet
def dodaj_etykiety(slupki):
    """Dodaje wartości nad słupkami"""
    for slupek in slupki:
        wysokosc = slupek.get_height()
        ax.annotate(f'{int(wysokosc)}',
                   xy=(slupek.get_x() + slupek.get_width() / 2, wysokosc),
                   xytext=(0, 3),  # 3 punkty nad słupkiem
                   textcoords="offset points",
                   ha='center', va='bottom',
                   fontsize=9,
                   fontweight='bold')

dodaj_etykiety(slupki1)
dodaj_etykiety(slupki2)
dodaj_etykiety(slupki3)

# KROK 6: Opisy wykresu
ax.set_title('Sprzedaż produktów elektronicznych w 2024 roku', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Kwartał', fontsize=13)
ax.set_ylabel('Sprzedaż (tys. sztuk)', fontsize=13)

# KROK 7: Ustawienie etykiet osi X
# Ustawiamy etykiety w środku każdej grupy słupków
ax.set_xticks(x)
ax.set_xticklabels(kwartaly, fontsize=11)

# KROK 8: Legenda i siatka
ax.legend(fontsize=12, loc='upper left', framealpha=0.9)
ax.grid(True, alpha=0.3, axis='y', linestyle='--')

# Dodajemy margines na górze wykresu
ax.set_ylim(0, max(smartfony + laptopy + tablety) * 1.15)

plt.tight_layout()
plt.show()

# ANALIZA DANYCH
print("\n" + "="*70)
print("RAPORT SPRZEDAŻY PRODUKTÓW ELEKTRONICZNYCH - 2024")
print("="*70)

# Suma sprzedaży dla każdego produktu
suma_smartfony = sum(smartfony)
suma_laptopy = sum(laptopy)
suma_tablety = sum(tablety)
suma_total = suma_smartfony + suma_laptopy + suma_tablety

print(f"\nSprzedaż roczna:")
print(f"  Smartfony:  {suma_smartfony:,} tys. szt. ({suma_smartfony/suma_total*100:.1f}%)")
print(f"  Laptopy:    {suma_laptopy:,} tys. szt. ({suma_laptopy/suma_total*100:.1f}%)")
print(f"  Tablety:    {suma_tablety:,} tys. szt. ({suma_tablety/suma_total*100:.1f}%)")
print(f"  RAZEM:      {suma_total:,} tys. szt.")

print(f"\nNajlepszy kwartał dla każdego produktu:")
print(f"  Smartfony:  {kwartaly[smartfony.index(max(smartfony))]} ({max(smartfony)} tys. szt.)")
print(f"  Laptopy:    {kwartaly[laptopy.index(max(laptopy))]} ({max(laptopy)} tys. szt.)")
print(f"  Tablety:    {kwartaly[tablety.index(max(tablety))]} ({max(tablety)} tys. szt.)")

# Wzrost sprzedaży Q1 vs Q4
print(f"\nWzrost sprzedaży Q1 → Q4:")
for nazwa, dane in [("Smartfony", smartfony), ("Laptopy", laptopy), ("Tablety", tablety)]:
    wzrost = ((dane[-1] - dane[0]) / dane[0]) * 100
    print(f"  {nazwa:12} {wzrost:+6.1f}%")

# ĆWICZENIE:
# 1. Przekształć wykres na skumulowany (stacked) używając parametru 'bottom'
# 2. Dodaj czwarty produkt (np. słuchawki)
# 3. Stwórz drugi wykres pokazujący udziały procentowe każdego produktu
