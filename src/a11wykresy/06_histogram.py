"""
Przykład 6: Histogram
======================

OPIS MERYTORYCZNY:
Dane przedstawiają rozkład wynagrodzeń (brutto w tys. PLN miesięcznie)
w branży IT w Polsce na podstawie ankiety 500 programistów.

JAK URUCHOMIĆ:
1. pip install matplotlib
2. python 06_histogram.py

JAK MODYFIKOWAĆ:
- Zmień liczbę przedziałów (parametr 'bins')
- Użyj różnych kolorów
- Dodaj krzywą rozkładu normalnego
- Zmień typ histogramu (parametr 'histtype': 'bar', 'step', 'stepfilled')
"""

import matplotlib.pyplot as plt
import random

# DANE: Wynagrodzenia w branży IT
# Generujemy realistyczne dane używając różnych rozkładów dla różnych poziomów

dane_wynagrodzen = []

# Junior developerzy (20% próby): 5-10 tys. PLN
random.seed(42)  # Dla powtarzalności wyników
for _ in range(100):
    dane_wynagrodzen.append({
        "wynagrodzenie": random.uniform(5.0, 10.0),
        "poziom": "junior"
    })

# Mid developerzy (45% próby): 10-18 tys. PLN
for _ in range(225):
    dane_wynagrodzen.append({
        "wynagrodzenie": random.uniform(10.0, 18.0),
        "poziom": "mid"
    })

# Senior developerzy (30% próby): 16-28 tys. PLN
for _ in range(150):
    dane_wynagrodzen.append({
        "wynagrodzenie": random.uniform(16.0, 28.0),
        "poziom": "senior"
    })

# Lead/Architect (5% próby): 25-40 tys. PLN
for _ in range(25):
    dane_wynagrodzen.append({
        "wynagrodzenie": random.uniform(25.0, 40.0),
        "poziom": "lead"
    })

# KROK 1: Przygotowanie danych
wszystkie_wynagrodzenia = [d["wynagrodzenie"] for d in dane_wynagrodzen]

# KROK 2: Obliczenie statystyk
import statistics
srednia = statistics.mean(wszystkie_wynagrodzenia)
mediana = statistics.median(wszystkie_wynagrodzenia)
odchylenie = statistics.stdev(wszystkie_wynagrodzenia)

# KROK 3: Tworzenie wykresu
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# ===== HISTOGRAM 1: Podstawowy =====
# plt.hist() tworzy histogram
# Parametry:
# - dane: lista wartości
# - bins: liczba przedziałów (lub lista granic przedziałów)
# - color: kolor słupków
# - edgecolor: kolor obramowania
# - alpha: przezroczystość

n, bins, patches = ax1.hist(wszystkie_wynagrodzenia, 
                             bins=20,              # 20 przedziałów
                             color='skyblue', 
                             edgecolor='navy',
                             alpha=0.7,
                             label='Wynagrodzenia')

# KROK 4: Dodanie linii statystyk
# Linia średniej
ax1.axvline(srednia, color='red', linestyle='--', linewidth=2, 
            label=f'Średnia: {srednia:.2f} tys. PLN')

# Linia mediany
ax1.axvline(mediana, color='green', linestyle='--', linewidth=2,
            label=f'Mediana: {mediana:.2f} tys. PLN')

# KROK 5: Opisy dla pierwszego histogramu
ax1.set_title('Rozkład wynagrodzeń w branży IT (2024)', 
              fontsize=14, fontweight='bold')
ax1.set_xlabel('Wynagrodzenie miesięczne brutto (tys. PLN)', fontsize=11)
ax1.set_ylabel('Liczba osób', fontsize=11)
ax1.legend(fontsize=10)
ax1.grid(True, alpha=0.3, axis='y')

# ===== HISTOGRAM 2: Porównawczy (według poziomów) =====
# Przygotowanie danych według poziomów
junior_wyn = [d["wynagrodzenie"] for d in dane_wynagrodzen if d["poziom"] == "junior"]
mid_wyn = [d["wynagrodzenie"] for d in dane_wynagrodzen if d["poziom"] == "mid"]
senior_wyn = [d["wynagrodzenie"] for d in dane_wynagrodzen if d["poziom"] == "senior"]
lead_wyn = [d["wynagrodzenie"] for d in dane_wynagrodzen if d["poziom"] == "lead"]

# Rysowanie nałożonych histogramów
ax2.hist(junior_wyn, bins=15, alpha=0.5, color='lightblue', 
         edgecolor='blue', label='Junior')
ax2.hist(mid_wyn, bins=15, alpha=0.5, color='lightgreen', 
         edgecolor='green', label='Mid')
ax2.hist(senior_wyn, bins=15, alpha=0.5, color='orange', 
         edgecolor='darkorange', label='Senior')
ax2.hist(lead_wyn, bins=15, alpha=0.5, color='purple', 
         edgecolor='darkviolet', label='Lead/Architect')

# Opisy dla drugiego histogramu
ax2.set_title('Rozkład wynagrodzeń według poziomów doświadczenia', 
              fontsize=14, fontweight='bold')
ax2.set_xlabel('Wynagrodzenie miesięczne brutto (tys. PLN)', fontsize=11)
ax2.set_ylabel('Liczba osób', fontsize=11)
ax2.legend(fontsize=10)
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

# SZCZEGÓŁOWA ANALIZA
print("\n" + "="*60)
print("ANALIZA WYNAGRODZEŃ W BRANŻY IT")
print("="*60)
print(f"\nLiczba respondentów: {len(wszystkie_wynagrodzenia)}")
print(f"\nStatystyki ogólne:")
print(f"  Średnia:           {srednia:.2f} tys. PLN")
print(f"  Mediana:           {mediana:.2f} tys. PLN")
print(f"  Odchylenie std:    {odchylenie:.2f} tys. PLN")
print(f"  Minimum:           {min(wszystkie_wynagrodzenia):.2f} tys. PLN")
print(f"  Maksimum:          {max(wszystkie_wynagrodzenia):.2f} tys. PLN")

print(f"\nStatystyki według poziomów:")
for nazwa, dane in [("Junior", junior_wyn), ("Mid", mid_wyn), 
                     ("Senior", senior_wyn), ("Lead", lead_wyn)]:
    if dane:
        print(f"\n  {nazwa}:")
        print(f"    Liczba:   {len(dane)}")
        print(f"    Średnia:  {statistics.mean(dane):.2f} tys. PLN")
        print(f"    Mediana:  {statistics.median(dane):.2f} tys. PLN")
        print(f"    Zakres:   {min(dane):.2f} - {max(dane):.2f} tys. PLN")

# ĆWICZENIE:
# 1. Dodaj histogram skumulowany (cumulative=True)
# 2. Stwórz histogram pokazujący tylko wynagrodzenia powyżej mediany
# 3. Oblicz i zaznacz kwartyle (25%, 50%, 75%)
