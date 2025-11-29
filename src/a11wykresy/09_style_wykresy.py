"""
Przykład 9: Style wykresów i dostosowywanie wyglądu
====================================================

OPIS MERYTORYCZNY:
Ten przykład pokazuje różne style wizualne dostępne w Matplotlib
na przykładzie danych o wzroście liczby użytkowników aplikacji mobilnej.

JAK URUCHOMIĆ:
1. pip install matplotlib
2. python 09_style_wykresy.py

JAK MODYFIKOWAĆ:
- Wypróbuj różne style (lista poniżej)
- Stwórz własny styl
- Łącz różne elementy stylów
- Zapisz wykres w różnych formatach (PNG, PDF, SVG)
"""

import matplotlib.pyplot as plt
import matplotlib.style as style

# DANE: Wzrost liczby użytkowników aplikacji (w tysiącach)
dane_uzytkownikow = [
    {"miesiac": "Styczeń", "aktywni": 45, "nowi": 12, "platny": 8},
    {"miesiac": "Luty", "aktywni": 52, "nowi": 15, "platny": 10},
    {"miesiac": "Marzec", "aktywni": 68, "nowi": 22, "platny": 14},
    {"miesiac": "Kwiecień", "aktywni": 89, "nowi": 28, "platny": 19},
    {"miesiac": "Maj", "aktywni": 112, "nowi": 35, "platny": 26},
    {"miesiac": "Czerwiec", "aktywni": 145, "nowi": 42, "platny": 35},
]

miesiace = [d["miesiac"] for d in dane_uzytkownikow]
aktywni = [d["aktywni"] for d in dane_uzytkownikow]
nowi = [d["nowi"] for d in dane_uzytkownikow]
platny = [d["platny"] for d in dane_uzytkownikow]

# KROK 1: Lista dostępnych stylów
print("Dostępne style w Matplotlib:")
print(plt.style.available)
print("\n" + "="*70)

# KROK 2: Tworzymy wykres w różnych stylach
# Wybieramy 6 najpopularniejszych stylów do porównania

style_do_pokazania = [
    'default',      # Domyślny styl Matplotlib
    'seaborn-v0_8',     # Styl inspirowany Seaborn (czytelny, akademicki)
    'ggplot',       # Styl inspirowany ggplot2 z R
    'bmh',          # Bayesian Methods for Hackers
    'fivethirtyeight',  # Styl portalu FiveThirtyEight
    'dark_background'   # Ciemne tło
]

# Tworzymy siatkę 2x3 dla 6 stylów
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
axes = axes.flatten()  # Zamieniamy tablicę 2D na 1D dla łatwiejszej iteracji

for idx, styl in enumerate(style_do_pokazania):
    # KROK 3: Ustawiamy styl dla danego subplota
    with plt.style.context(styl):
        ax = axes[idx]
        
        # Rysujemy trzy linie
        ax.plot(miesiace, aktywni, marker='o', linewidth=2.5, 
                markersize=8, label='Aktywni użytkownicy')
        ax.plot(miesiace, nowi, marker='s', linewidth=2.5, 
                markersize=8, label='Nowi użytkownicy')
        ax.plot(miesiace, platny, marker='^', linewidth=2.5, 
                markersize=8, label='Płatni użytkownicy')
        
        # Tytuł pokazujący nazwę stylu
        ax.set_title(f'Styl: {styl}', fontsize=12, fontweight='bold', pad=10)
        ax.set_xlabel('Miesiąc', fontsize=10)
        ax.set_ylabel('Liczba użytkowników (tys.)', fontsize=10)
        ax.legend(loc='upper left', fontsize=8)
        ax.grid(True, alpha=0.3)
        
        # Obracamy etykiety
        ax.tick_params(axis='x', rotation=45)

fig.suptitle('Porównanie stylów wykresów w Matplotlib', 
             fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

print("\n" + "="*70)
print("TWORZENIE WYKRESU Z ZAAWANSOWANYM DOSTOSOWANIEM")
print("="*70)

# KROK 4: Wykres z pełnym dostosowaniem (bez predefiniowanego stylu)
fig, ax = plt.subplots(figsize=(14, 8))

# Ustawienie koloru tła
fig.patch.set_facecolor('#f8f9fa')  # Jasne tło całej figury
ax.set_facecolor('#ffffff')          # Białe tło obszaru wykresu

# Rysowanie danych z niestandardowymi kolorami
linia1 = ax.plot(miesiace, aktywni, 
                 color='#2ecc71',           # Zielony
                 marker='o', 
                 linewidth=3, 
                 markersize=10,
                 markerfacecolor='#27ae60', # Ciemniejszy zielony
                 markeredgecolor='white',   # Biała obwódka
                 markeredgewidth=2,
                 label='Aktywni użytkownicy',
                 zorder=3)                  # Rysuj na wierzchu

linia2 = ax.plot(miesiace, nowi, 
                 color='#3498db',           # Niebieski
                 marker='s', 
                 linewidth=3, 
                 markersize=10,
                 markerfacecolor='#2980b9',
                 markeredgecolor='white',
                 markeredgewidth=2,
                 label='Nowi użytkownicy',
                 zorder=3)

linia3 = ax.plot(miesiace, platny, 
                 color='#f39c12',           # Pomarańczowy
                 marker='^', 
                 linewidth=3, 
                 markersize=10,
                 markerfacecolor='#e67e22',
                 markeredgecolor='white',
                 markeredgewidth=2,
                 label='Płatni użytkownicy',
                 zorder=3)

# KROK 5: Dostosowanie osi
ax.spines['top'].set_visible(False)      # Ukryj górną ramkę
ax.spines['right'].set_visible(False)    # Ukryj prawą ramkę
ax.spines['left'].set_linewidth(2)       # Pogrub lewą ramkę
ax.spines['bottom'].set_linewidth(2)     # Pogrub dolną ramkę

# KROK 6: Siatka
ax.grid(True, alpha=0.3, linestyle='--', linewidth=1, color='gray', zorder=1)
ax.set_axisbelow(True)  # Siatka pod wykresem

# KROK 7: Tytuły i etykiety
ax.set_title('Wzrost bazy użytkowników aplikacji mobilnej "SuperApp"', 
             fontsize=18, fontweight='bold', pad=20, color='#2c3e50')
ax.set_xlabel('Miesiąc', fontsize=14, fontweight='bold', color='#2c3e50')
ax.set_ylabel('Liczba użytkowników (tys.)', fontsize=14, fontweight='bold', color='#2c3e50')

# KROK 8: Legenda z dostosowaniem
legend = ax.legend(loc='upper left', 
                  fontsize=12,
                  frameon=True,
                  fancybox=True,      # Zaokrąglone rogi
                  shadow=True,        # Cień
                  framealpha=0.95,    # Przezroczystość
                  edgecolor='#bdc3c7',
                  facecolor='white')

# KROK 9: Dodanie adnotacji
# Zaznaczamy najlepszy wynik
max_aktywni = max(aktywni)
max_idx = aktywni.index(max_aktywni)
ax.annotate(f'Rekordowy miesiąc!\n{max_aktywni}k użytkowników',
           xy=(max_idx, max_aktywni),           # Punkt do zaznaczenia
           xytext=(max_idx - 1, max_aktywni + 20), # Pozycja tekstu
           fontsize=11,
           fontweight='bold',
           color='#27ae60',
           bbox=dict(boxstyle='round,pad=0.5', facecolor='#d5f4e6', edgecolor='#27ae60', linewidth=2),
           arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3', 
                          color='#27ae60', lw=2))

# KROK 10: Dodanie tekstu informacyjnego
textstr = 'Źródło: Analytics Dashboard 2024\nOstatnia aktualizacja: Czerwiec 2024'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.3)
ax.text(0.02, 0.98, textstr, transform=ax.transAxes, fontsize=9,
       verticalalignment='top', bbox=props)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# KROK 11: Zapisywanie wykresu
# plt.savefig('wykres_uzytkownicy.png', dpi=300, bbox_inches='tight', facecolor='#f8f9fa')
# plt.savefig('wykres_uzytkownicy.pdf', bbox_inches='tight')  # Format PDF
# plt.savefig('wykres_uzytkownicy.svg', bbox_inches='tight')  # Format SVG (wektorowy)

plt.show()

print("\nWYKRES ZAPISANY!")
print("Możesz zapisać wykres w różnych formatach:")
print("  - PNG (rasterowy): dobry do prezentacji, stron www")
print("  - PDF (wektorowy): idealny do druku, publikacji naukowych")
print("  - SVG (wektorowy): dobry do edycji w programach graficznych")

# ĆWICZENIE:
# 1. Stwórz własny styl używając rcParams
# 2. Eksperymentuj z różnymi paletami kolorów
# 3. Dodaj więcej adnotacji do wykresu
# 4. Stwórz wykres w stylu "dark mode"
