"""
Przykład 8: Subplots - wiele wykresów w jednym oknie
=====================================================

OPIS MERYTORYCZNY:
Kompleksowa analiza danych klimatycznych dla Warszawy w 2024 roku:
temperatura, opady, wilgotność powietrza i prędkość wiatru.

JAK URUCHOMIĆ:
1. pip install matplotlib numpy
2. python 08_subplots.py

JAK MODYFIKOWAĆ:
- Zmień układ subplotów (np. 4 wiersze, 1 kolumna)
- Dodaj więcej wykresów
- Użyj różnych typów wykresów w różnych panelach
- Eksperymentuj z plt.subplot2grid() dla nieregularnych układów
"""

import matplotlib.pyplot as plt
import numpy as np
import random

# DANE: Dane klimatyczne dla każdego miesiąca
random.seed(42)
miesiace = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze', 
            'Lip', 'Sie', 'Wrz', 'Paź', 'Lis', 'Gru']

dane_klimatyczne = [
    {"miesiac": "Sty", "temp_srednia": -2.5, "opady": 28, "wilgotnosc": 85, "wiatr": 15},
    {"miesiac": "Lut", "temp_srednia": -0.8, "opady": 24, "wilgotnosc": 82, "wiatr": 16},
    {"miesiac": "Mar", "temp_srednia": 4.2, "opady": 32, "wilgotnosc": 75, "wiatr": 14},
    {"miesiac": "Kwi", "temp_srednia": 10.5, "opady": 38, "wilgotnosc": 68, "wiatr": 13},
    {"miesiac": "Maj", "temp_srednia": 16.3, "opady": 52, "wilgotnosc": 65, "wiatr": 11},
    {"miesiac": "Cze", "temp_srednia": 19.8, "opady": 68, "wilgotnosc": 68, "wiatr": 10},
    {"miesiac": "Lip", "temp_srednia": 22.1, "opady": 75, "wilgotnosc": 70, "wiatr": 9},
    {"miesiac": "Sie", "temp_srednia": 21.5, "opady": 62, "wilgotnosc": 71, "wiatr": 9},
    {"miesiac": "Wrz", "temp_srednia": 16.2, "opady": 45, "wilgotnosc": 75, "wiatr": 11},
    {"miesiac": "Paź", "temp_srednia": 10.1, "opady": 38, "wilgotnosc": 80, "wiatr": 12},
    {"miesiac": "Lis", "temp_srednia": 4.8, "opady": 35, "wilgotnosc": 86, "wiatr": 14},
    {"miesiac": "Gru", "temp_srednia": 0.5, "opady": 30, "wilgotnosc": 88, "wiatr": 15}
]

# Przygotowanie danych
temperatura = [d["temp_srednia"] for d in dane_klimatyczne]
opady = [d["opady"] for d in dane_klimatyczne]
wilgotnosc = [d["wilgotnosc"] for d in dane_klimatyczne]
wiatr = [d["wiatr"] for d in dane_klimatyczne]

# KROK 1: Tworzenie figury z subplotami
# plt.subplots(nrows, ncols) tworzy siatkę wykresów
# nrows=2, ncols=2 tworzy siatkę 2x2 (4 wykresy)
# figsize określa całkowity rozmiar okna
# fig - obiekt całej figury
# axes - tablica obiektów osi (wykresów)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 12))

# UWAGA: axes to tablica 2D: axes[wiersz][kolumna]
# axes[0][0] - lewy górny
# axes[0][1] - prawy górny
# axes[1][0] - lewy dolny
# axes[1][1] - prawy dolny

# ===== SUBPLOT 1: Temperatura (lewy górny) =====
ax1 = axes[0, 0]  # Można też: axes[0][0]

# Rysujemy wykres liniowy z wypełnieniem
ax1.plot(miesiace, temperatura, 
         color='#e74c3c', 
         linewidth=2.5, 
         marker='o', 
         markersize=8,
         label='Temperatura średnia')

# Wypełnienie pod wykresem
ax1.fill_between(miesiace, temperatura, 
                 alpha=0.3, 
                 color='#e74c3c')

# Linia odniesienia dla 0°C
ax1.axhline(y=0, color='blue', linestyle='--', linewidth=1, alpha=0.5, label='0°C')

ax1.set_title('Temperatura średnia', fontsize=14, fontweight='bold', pad=10)
ax1.set_ylabel('Temperatura (°C)', fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper left', fontsize=9)

# ===== SUBPLOT 2: Opady (prawy górny) =====
ax2 = axes[0, 1]

# Wykres słupkowy
bars = ax2.bar(miesiace, opady, 
               color='#3498db', 
               edgecolor='navy',
               linewidth=1.5,
               alpha=0.7)

# Kolorujemy na czerwono miesiące z opadami > 60mm
for i, (bar, opad) in enumerate(zip(bars, opady)):
    if opad > 60:
        bar.set_color('#e74c3c')
        bar.set_edgecolor('darkred')

ax2.set_title('Suma opadów', fontsize=14, fontweight='bold', pad=10)
ax2.set_ylabel('Opady (mm)', fontsize=11)
ax2.grid(True, alpha=0.3, axis='y')

# Dodajemy linię średniej
srednia_opadow = sum(opady) / len(opady)
ax2.axhline(y=srednia_opadow, color='green', linestyle='--', 
            linewidth=2, label=f'Średnia: {srednia_opadow:.1f}mm')
ax2.legend(fontsize=9)

# ===== SUBPLOT 3: Wilgotność (lewy dolny) =====
ax3 = axes[1, 0]

# Wykres obszarowy (area chart)
ax3.fill_between(miesiace, wilgotnosc, 
                 color='#9b59b6', 
                 alpha=0.6)
ax3.plot(miesiace, wilgotnosc, 
         color='#8e44ad', 
         linewidth=2, 
         marker='s',
         markersize=6)

ax3.set_title('Wilgotność względna', fontsize=14, fontweight='bold', pad=10)
ax3.set_ylabel('Wilgotność (%)', fontsize=11)
ax3.set_ylim(60, 95)
ax3.grid(True, alpha=0.3)

# ===== SUBPLOT 4: Prędkość wiatru (prawy dolny) =====
ax4 = axes[1, 1]

# Wykres punktowy z różnymi rozmiarami
# Rozmiar punktu proporcjonalny do prędkości wiatru
rozmiary = [w**2 * 3 for w in wiatr]  # Kwadrat prędkości * 3

scatter = ax4.scatter(miesiace, wiatr, 
                      s=rozmiary,
                      c=wiatr,  # Kolor zależy od prędkości
                      cmap='YlOrRd',  # Paleta kolorów: żółty-pomarańczowy-czerwony
                      alpha=0.6,
                      edgecolors='black',
                      linewidths=1.5)

# Dodajemy kolorbar (pasek legend kolorów)
cbar = plt.colorbar(scatter, ax=ax4)
cbar.set_label('Prędkość (km/h)', fontsize=10)

# Linia łącząca punkty
ax4.plot(miesiace, wiatr, 
         color='gray', 
         linestyle='--', 
         linewidth=1, 
         alpha=0.5)

ax4.set_title('Średnia prędkość wiatru', fontsize=14, fontweight='bold', pad=10)
ax4.set_ylabel('Prędkość (km/h)', fontsize=11)
ax4.grid(True, alpha=0.3)

# ===== OGÓLNE USTAWIENIA =====
# Wspólny tytuł dla wszystkich wykresów
fig.suptitle('Analiza danych klimatycznych - Warszawa 2024', 
             fontsize=18, fontweight='bold', y=0.995)

# Obracamy etykiety osi X we wszystkich wykresach
for ax in axes.flat:
    ax.tick_params(axis='x', rotation=45)
    ax.set_xlabel('Miesiąc', fontsize=11)

# Automatyczne dopasowanie odstępów
plt.tight_layout()
plt.show()

# DODATKOWA ANALIZA
print("\n" + "="*70)
print("RAPORT KLIMATYCZNY - WARSZAWA 2024")
print("="*70)

print(f"\nTemperatura:")
print(f"  Średnia roczna:      {sum(temperatura)/len(temperatura):6.1f}°C")
print(f"  Najcieplejszy miesiąc: {miesiace[temperatura.index(max(temperatura))]} ({max(temperatura):.1f}°C)")
print(f"  Najzimniejszy miesiąc: {miesiace[temperatura.index(min(temperatura))]} ({min(temperatura):.1f}°C)")

print(f"\nOpady:")
print(f"  Suma roczna:         {sum(opady):6} mm")
print(f"  Średnia miesięczna:  {sum(opady)/len(opady):6.1f} mm")
print(f"  Najwięcej opadów:    {miesiace[opady.index(max(opady))]} ({max(opady)} mm)")

print(f"\nWilgotność:")
print(f"  Średnia roczna:      {sum(wilgotnosc)/len(wilgotnosc):6.1f}%")

print(f"\nWiatr:")
print(f"  Średnia prędkość:    {sum(wiatr)/len(wiatr):6.1f} km/h")
print(f"  Najbardziej wietrzny: {miesiace[wiatr.index(max(wiatr))]} ({max(wiatr)} km/h)")

# ĆWICZENIE:
# 1. Zmień układ na 1 wiersz i 4 kolumny
# 2. Dodaj piąty wykres pokazujący korelację temperatura-opady
# 3. Użyj różnych colormap dla scatter plot
