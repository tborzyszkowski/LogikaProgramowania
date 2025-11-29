"""
Przykład 10: Wykres pudełkowy (box plot) - analiza rozkładu danych
===================================================================

OPIS MERYTORYCZNY:
Analiza czasu odpowiedzi (response time) różnych mikrousług w systemie e-commerce
mierzonego w milisekundach. Dane pomogą zidentyfikować wąskie gardła systemu.

JAK URUCHOMIĆ:
1. pip install matplotlib numpy
2. python 10_boxplot.py

JAK MODYFIKOWAĆ:
- Zmień orientację na poziomą (vert=False)
- Dodaj więcej usług do analizy
- Zmień kolory i style boxów
- Użyj violin plot jako alternatywy (plt.violinplot)
"""

import matplotlib.pyplot as plt
import numpy as np

# DANE: Czasy odpowiedzi mikrousług (w milisekundach)
# Zbieramy 100 pomiarów dla każdej usługi

np.random.seed(42)

# Usługa 1: Authentication Service (szybka, stabilna)
auth_service = np.random.normal(loc=25, scale=5, size=100)

# Usługa 2: Product Catalog (średnia, stabilna)
catalog_service = np.random.normal(loc=45, scale=8, size=100)

# Usługa 3: Payment Gateway (wolniejsza, więcej outlierów)
payment_service = np.concatenate([
    np.random.normal(loc=80, scale=15, size=90),
    np.random.normal(loc=200, scale=30, size=10)  # 10% bardzo wolnych
])

# Usługa 4: Search Engine (szybka ale z outlierami)
search_service = np.concatenate([
    np.random.normal(loc=35, scale=7, size=95),
    np.random.normal(loc=150, scale=20, size=5)  # 5% outlierów
])

# Usługa 5: Recommendation Engine (najwolniejsza)
recommendation_service = np.random.normal(loc=120, scale=25, size=100)

# KROK 1: Przygotowanie danych
dane = [auth_service, catalog_service, payment_service, 
        search_service, recommendation_service]
nazwy_uslug = ['Authentication', 'Product\nCatalog', 'Payment\nGateway', 
               'Search\nEngine', 'Recommendation']

# KROK 2: Tworzenie wykresu
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# ===== BOXPLOT 1: Podstawowy =====
# plt.boxplot() tworzy wykres pudełkowy
# Parametry:
# - dane: lista list z wartościami
# - labels: nazwy kategorii
# - patch_artist: True = wypełnione kolorami, False = tylko kontury
# - notch: True = wcięcie pokazujące przedział ufności dla mediany

bp1 = ax1.boxplot(dane, 
                  labels=nazwy_uslug,
                  patch_artist=True,       # Wypełnione kolorem
                  notch=True,              # Wcięcie dla mediany
                  showmeans=True,          # Pokaż średnią
                  meanline=False,          # Średnia jako punkt (nie linia)
                  widths=0.6)              # Szerokość pudełek

# KROK 3: Kolorowanie pudełek
kolory = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12', '#9b59b6']

for patch, kolor in zip(bp1['boxes'], kolory):
    patch.set_facecolor(kolor)
    patch.set_alpha(0.7)

# Konfiguracja innych elementów
for whisker in bp1['whiskers']:
    whisker.set(linewidth=1.5, linestyle='-', color='#34495e')

for cap in bp1['caps']:
    cap.set(linewidth=1.5, color='#34495e')

for median in bp1['medians']:
    median.set(linewidth=2.5, color='#c0392b')

for mean in bp1['means']:
    mean.set(marker='D', markerfacecolor='yellow', 
            markeredgecolor='orange', markersize=8)

for flier in bp1['fliers']:
    flier.set(marker='o', markerfacecolor='red', 
             markersize=5, alpha=0.5)

# Opisy dla boxplot 1
ax1.set_title('Analiza czasu odpowiedzi mikrousług', 
             fontsize=14, fontweight='bold', pad=15)
ax1.set_ylabel('Czas odpowiedzi (ms)', fontsize=12)
ax1.grid(True, alpha=0.3, axis='y', linestyle='--')
ax1.set_ylim(0, 300)

# Dodanie legendy wyjaśniającej elementy boxplota
legend_elements = [
    plt.Line2D([0], [0], color='#c0392b', linewidth=2.5, label='Mediana'),
    plt.Line2D([0], [0], marker='D', color='w', markerfacecolor='yellow', 
              markeredgecolor='orange', markersize=8, label='Średnia'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', 
              markersize=5, alpha=0.5, label='Wartości odstające')
]
ax1.legend(handles=legend_elements, loc='upper left', fontsize=9)

# ===== BOXPLOT 2: Poziomy z dodatkowymi informacjami =====
bp2 = ax2.boxplot(dane, 
                  labels=nazwy_uslug,
                  vert=False,              # Poziomy
                  patch_artist=True,
                  notch=True,
                  showmeans=True,
                  meanline=False,
                  widths=0.6)

# Kolorowanie
for patch, kolor in zip(bp2['boxes'], kolory):
    patch.set_facecolor(kolor)
    patch.set_alpha(0.7)

for whisker in bp2['whiskers']:
    whisker.set(linewidth=1.5, linestyle='-', color='#34495e')

for cap in bp2['caps']:
    cap.set(linewidth=1.5, color='#34495e')

for median in bp2['medians']:
    median.set(linewidth=2.5, color='#c0392b')

for mean in bp2['means']:
    mean.set(marker='D', markerfacecolor='yellow', 
            markeredgecolor='orange', markersize=8)

for flier in bp2['fliers']:
    flier.set(marker='o', markerfacecolor='red', 
             markersize=5, alpha=0.5)

# Opisy dla boxplot 2
ax2.set_title('Porównanie poziome (z SLA)', 
             fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel('Czas odpowiedzi (ms)', fontsize=12)
ax2.grid(True, alpha=0.3, axis='x', linestyle='--')
ax2.set_xlim(0, 300)

# Dodanie linii SLA (Service Level Agreement) - max 100ms
ax2.axvline(x=100, color='green', linestyle='--', linewidth=2, 
           alpha=0.7, label='SLA: 100ms')
ax2.legend(loc='upper right', fontsize=10)

fig.suptitle('Monitoring wydajności systemu e-commerce', 
            fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# SZCZEGÓŁOWA ANALIZA STATYSTYCZNA
print("\n" + "="*80)
print("RAPORT WYDAJNOŚCI MIKROUSŁUG")
print("="*80)

import statistics

uslugi_dane = [
    ("Authentication Service", auth_service),
    ("Product Catalog", catalog_service),
    ("Payment Gateway", payment_service),
    ("Search Engine", search_service),
    ("Recommendation Engine", recommendation_service)
]

for nazwa, dane_uslugi in uslugi_dane:
    print(f"\n{nazwa}:")
    print(f"  Średnia:          {np.mean(dane_uslugi):7.2f} ms")
    print(f"  Mediana:          {np.median(dane_uslugi):7.2f} ms")
    print(f"  Odchylenie std:   {np.std(dane_uslugi):7.2f} ms")
    print(f"  Min:              {np.min(dane_uslugi):7.2f} ms")
    print(f"  Max:              {np.max(dane_uslugi):7.2f} ms")
    
    # Kwartyle
    q1 = np.percentile(dane_uslugi, 25)
    q3 = np.percentile(dane_uslugi, 75)
    iqr = q3 - q1
    print(f"  Q1 (25%):         {q1:7.2f} ms")
    print(f"  Q3 (75%):         {q3:7.2f} ms")
    print(f"  IQR:              {iqr:7.2f} ms")
    
    # Sprawdzenie SLA (max 100ms)
    przekroczenia = sum(1 for x in dane_uslugi if x > 100)
    procent = (przekroczenia / len(dane_uslugi)) * 100
    print(f"  Przekroczenia SLA: {przekroczenia}/100 ({procent:.1f}%)")
    
    if procent > 5:
        print(f"  ⚠️  UWAGA: Usługa przekracza SLA w >5% przypadków!")

print("\n" + "="*80)
print("INTERPRETACJA BOXPLOT:")
print("="*80)
print("""
Elementy wykresu pudełkowego:
  • Prostokąt (pudełko): zawiera 50% środkowych danych (Q1 do Q3)
  • Linia w pudełku (czerwona): mediana (50. percentyl)
  • Diament (żółty): średnia arytmetyczna
  • Wąsy (linie): rozciągają się do 1.5 * IQR od pudełka
  • Punkty poza wąsami (czerwone): wartości odstające (outliery)
  • Wcięcie (notch): przedział ufności dla mediany (95%)

Jeśli wcięcia dwóch pudełek się nie pokrywają, mediany są 
istotnie statystycznie różne (p < 0.05).
""")

# ĆWICZENIE:
# 1. Dodaj szóstą usługę (np. Email Service)
# 2. Stwórz violin plot jako alternatywę
# 3. Dodaj test statystyczny porównujący usługi
# 4. Stwórz alert dla usług przekraczających SLA
