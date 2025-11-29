"""
Przykład 11: Mapa cieplna (heatmap)
====================================

OPIS MERYTORYCZNY:
Dane przedstawiają korelację między różnymi aktywnościami użytkowników
w aplikacji fitness (kroki, kalorie, czas ćwiczeń, dystans, sen)
dla 8 tygodni treningowych.

JAK URUCHOMIĆ:
1. pip install matplotlib numpy
2. python 11_heatmap.py

JAK MODYFIKOWAĆ:
- Zmień paletę kolorów (cmap)
- Dostosuj rozmiar adnotacji
- Użyj różnych skal kolorów
- Dodaj więcej danych do analizy
"""

import matplotlib.pyplot as plt
import numpy as np

# DANE: Tygodniowe aktywności użytkownika
# Dane znormalizowane do skali 0-100 dla lepszej wizualizacji

dane_aktywnosci = [
    {"tydzien": "Tydzień 1", "kroki": 65, "kalorie": 58, "cwiczenia": 42, "dystans": 55, "sen": 68},
    {"tydzien": "Tydzień 2", "kroki": 72, "kalorie": 65, "cwiczenia": 48, "dystans": 62, "sen": 71},
    {"tydzien": "Tydzień 3", "kroki": 78, "kalorie": 71, "cwiczenia": 55, "dystans": 68, "sen": 65},
    {"tydzien": "Tydzień 4", "kroki": 85, "kalorie": 78, "cwiczenia": 62, "dystans": 75, "sen": 72},
    {"tydzien": "Tydzień 5", "kroki": 88, "kalorie": 82, "cwiczenia": 68, "dystans": 80, "sen": 75},
    {"tydzien": "Tydzień 6", "kroki": 92, "kalorie": 88, "cwiczenia": 75, "dystans": 85, "sen": 78},
    {"tydzien": "Tydzień 7", "kroki": 95, "kalorie": 92, "cwiczenia": 82, "dystans": 90, "sen": 82},
    {"tydzien": "Tydzień 8", "kroki": 98, "kalorie": 95, "cwiczenia": 88, "dystans": 95, "sen": 85},
]

# KROK 1: Przygotowanie danych do macierzy
tygodnie = [d["tydzien"] for d in dane_aktywnosci]
kategorie = ["Kroki\n(tys./dzień)", "Kalorie\n(kcal/dzień)", 
             "Ćwiczenia\n(min/dzień)", "Dystans\n(km/dzień)", 
             "Sen\n(godz./noc)"]

# Tworzymy macierz 2D: wiersze = tygodnie, kolumny = kategorie
macierz_danych = []
for dane in dane_aktywnosci:
    macierz_danych.append([
        dane["kroki"],
        dane["kalorie"],
        dane["cwiczenia"],
        dane["dystans"],
        dane["sen"]
    ])

macierz_danych = np.array(macierz_danych)

# KROK 2: Obliczenie macierzy korelacji
# Dodatkowa analiza: korelacja między różnymi aktywnościami
macierz_korelacji = np.corrcoef(macierz_danych.T)

# KROK 3: Tworzenie dwóch wykresów
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# ===== HEATMAPA 1: Postępy tygodniowe =====
# plt.imshow() wyświetla macierz jako obraz
# cmap - paleta kolorów (YlOrRd = żółty-pomarańczowy-czerwony)
# aspect='auto' - automatyczne dopasowanie proporcji

im1 = ax1.imshow(macierz_danych, 
                 cmap='YlOrRd',          # Paleta kolorów
                 aspect='auto',          # Automatyczne proporcje
                 interpolation='nearest',
                 vmin=0,                 # Minimum skali
                 vmax=100)               # Maksimum skali

# KROK 4: Dodanie paska kolorów (colorbar)
cbar1 = plt.colorbar(im1, ax=ax1)
cbar1.set_label('Poziom aktywności (%)', fontsize=11, rotation=270, labelpad=20)

# KROK 5: Ustawienie etykiet osi
ax1.set_xticks(np.arange(len(kategorie)))
ax1.set_yticks(np.arange(len(tygodnie)))
ax1.set_xticklabels(kategorie, fontsize=10)
ax1.set_yticklabels(tygodnie, fontsize=10)

# KROK 6: Dodanie wartości w każdej komórce
for i in range(len(tygodnie)):
    for j in range(len(kategorie)):
        wartość = macierz_danych[i, j]
        # Kolor tekstu: biały dla ciemnych komórek, czarny dla jasnych
        kolor_tekstu = 'white' if wartość > 70 else 'black'
        
        ax1.text(j, i, f'{wartość}%',
                ha='center', va='center',
                color=kolor_tekstu,
                fontsize=10,
                fontweight='bold')

# KROK 7: Opisy
ax1.set_title('Postęp aktywności fitness w ciągu 8 tygodni', 
             fontsize=14, fontweight='bold', pad=15)

# Obracamy etykiety górnej osi X
plt.setp(ax1.get_xticklabels(), rotation=0, ha='center')

# Dodajemy obramowanie komórek
ax1.set_xticks(np.arange(len(kategorie)) - 0.5, minor=True)
ax1.set_yticks(np.arange(len(tygodnie)) - 0.5, minor=True)
ax1.grid(which="minor", color="white", linestyle='-', linewidth=2)

# ===== HEATMAPA 2: Macierz korelacji =====
# Pokazuje jak różne aktywności są ze sobą skorelowane

im2 = ax2.imshow(macierz_korelacji, 
                 cmap='coolwarm',        # Niebiesko-czerwona paleta
                 aspect='auto',
                 interpolation='nearest',
                 vmin=-1,                # Korelacja od -1
                 vmax=1)                 # do +1

# Colorbar dla korelacji
cbar2 = plt.colorbar(im2, ax=ax2)
cbar2.set_label('Współczynnik korelacji', fontsize=11, rotation=270, labelpad=20)

# Etykiety
ax2.set_xticks(np.arange(len(kategorie)))
ax2.set_yticks(np.arange(len(kategorie)))
ax2.set_xticklabels(kategorie, fontsize=10)
ax2.set_yticklabels(kategorie, fontsize=10)

# Wartości korelacji w komórkach
for i in range(len(kategorie)):
    for j in range(len(kategorie)):
        wartość = macierz_korelacji[i, j]
        # Kolor tekstu zależny od wartości korelacji
        kolor_tekstu = 'white' if abs(wartość) > 0.7 else 'black'
        
        ax2.text(j, i, f'{wartość:.2f}',
                ha='center', va='center',
                color=kolor_tekstu,
                fontsize=10,
                fontweight='bold')

# Opisy
ax2.set_title('Macierz korelacji między aktywnościami', 
             fontsize=14, fontweight='bold', pad=15)

# Obracamy etykiety
plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')

# Obramowanie
ax2.set_xticks(np.arange(len(kategorie)) - 0.5, minor=True)
ax2.set_yticks(np.arange(len(kategorie)) - 0.5, minor=True)
ax2.grid(which="minor", color="white", linestyle='-', linewidth=2)

# Tytuł główny
fig.suptitle('Analiza danych fitness - 8-tygodniowy program treningowy', 
            fontsize=16, fontweight='bold')

plt.tight_layout()
plt.show()

# ANALIZA SZCZEGÓŁOWA
print("\n" + "="*80)
print("RAPORT POSTĘPÓW FITNESS")
print("="*80)

print("\nPostęp od tygodnia 1 do tygodnia 8:")
kategorie_nazwy = ["Kroki", "Kalorie", "Ćwiczenia", "Dystans", "Sen"]
for idx, nazwa in enumerate(kategorie_nazwy):
    poczatek = macierz_danych[0, idx]
    koniec = macierz_danych[-1, idx]
    wzrost = koniec - poczatek
    wzrost_proc = (wzrost / poczatek) * 100
    print(f"  {nazwa:12} {poczatek:5.0f}% → {koniec:5.0f}%  "
          f"(wzrost: +{wzrost:.0f}pp, +{wzrost_proc:.1f}%)")

print("\n" + "="*80)
print("ANALIZA KORELACJI")
print("="*80)
print("\nNajsilniejsze korelacje (poza przekątną):")

# Znajdujemy najsilniejsze korelacje
korelacje_lista = []
for i in range(len(kategorie_nazwy)):
    for j in range(i+1, len(kategorie_nazwy)):
        korelacje_lista.append((
            kategorie_nazwy[i],
            kategorie_nazwy[j],
            macierz_korelacji[i, j]
        ))

# Sortujemy według siły korelacji
korelacje_lista.sort(key=lambda x: abs(x[2]), reverse=True)

for akt1, akt2, kor in korelacje_lista[:5]:
    interpretacja = "silna dodatnia" if kor > 0.8 else \
                   "umiarkowana dodatnia" if kor > 0.5 else \
                   "słaba dodatnia" if kor > 0 else \
                   "słaba ujemna" if kor > -0.5 else \
                   "umiarkowana ujemna"
    print(f"  {akt1:12} ↔ {akt2:12}  r = {kor:5.2f}  ({interpretacja})")

print("\n" + "="*80)
print("NAJWAŻNIEJSZE WNIOSKI")
print("="*80)
print("""
1. Wszystkie kategorie aktywności pokazują stały wzrost w ciągu 8 tygodni
2. Silna korelacja między krokami a dystansem (oczekiwane)
3. Ćwiczenia korelują pozytywnie ze spalanymi kaloriami
4. Sen może być niezależny od innych aktywności lub słabo skorelowany
5. Program treningowy przynosi systematyczne rezultaty
""")

# ĆWICZENIE:
# 1. Dodaj więcej tygodni danych
# 2. Użyj innych palet kolorów (np. 'viridis', 'plasma')
# 3. Stwórz heatmapę dla danych z różnych użytkowników
# 4. Dodaj clustering (grupowanie podobnych tygodni)

# DOSTĘPNE PALETY KOLORÓW:
print("\nPopularne palety kolorów (cmap):")
print("  Sekwencyjne: 'viridis', 'plasma', 'inferno', 'magma', 'cividis'")
print("  Sekwencyjne: 'Blues', 'Greens', 'Reds', 'YlOrRd', 'YlGnBu'")
print("  Dywergentne: 'coolwarm', 'RdBu', 'RdYlGn', 'Spectral'")
print("  Inne:        'rainbow', 'jet', 'hot', 'cool'")
