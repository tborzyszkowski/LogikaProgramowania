"""
Przykład 4: Wykres punktowy (scatter plot)
==========================================

OPIS MERYTORYCZNY:
Dane przedstawiają korelację między wydatkami na reklamę (w tys. PLN)
a przychodami ze sprzedaży (w tys. PLN) dla 50 różnych kampanii marketingowych
prowadzonych przez firmę e-commerce.

JAK URUCHOMIĆ:
1. pip install matplotlib
2. python 04_scatter_plot.py

JAK MODYFIKOWAĆ:
- Zmień rozmiary punktów (parametr 's')
- Zmień przezroczystość (parametr 'alpha')
- Użyj różnych kolorów dla różnych grup danych
- Dodaj więcej wymiarów używając koloru i rozmiaru punktów jednocześnie
"""

import matplotlib.pyplot as plt

# DANE: Wydatki na reklamę vs przychody
# Każda kampania ma: budżet reklamowy, przychód i typ kampanii
dane_kampanii = [
    {"budzet": 5.2, "przychod": 28.5, "typ": "social_media"},
    {"budzet": 8.1, "przychod": 42.3, "typ": "social_media"},
    {"budzet": 3.5, "przychod": 18.2, "typ": "social_media"},
    {"budzet": 12.4, "przychod": 65.8, "typ": "social_media"},
    {"budzet": 6.8, "przychod": 35.1, "typ": "social_media"},
    {"budzet": 15.2, "przychod": 78.4, "typ": "social_media"},
    {"budzet": 9.3, "przychod": 48.9, "typ": "social_media"},
    {"budzet": 4.7, "przychod": 25.6, "typ": "social_media"},
    {"budzet": 11.5, "przychod": 59.2, "typ": "social_media"},
    {"budzet": 7.9, "przychod": 41.7, "typ": "social_media"},
    
    {"budzet": 18.5, "przychod": 82.3, "typ": "google_ads"},
    {"budzet": 22.3, "przychod": 98.7, "typ": "google_ads"},
    {"budzet": 14.8, "przychod": 68.5, "typ": "google_ads"},
    {"budzet": 25.6, "przychod": 112.4, "typ": "google_ads"},
    {"budzet": 19.2, "przychod": 87.6, "typ": "google_ads"},
    {"budzet": 16.7, "przychod": 75.3, "typ": "google_ads"},
    {"budzet": 28.4, "przychod": 125.8, "typ": "google_ads"},
    {"budzet": 21.5, "przychod": 95.2, "typ": "google_ads"},
    {"budzet": 17.9, "przychod": 79.8, "typ": "google_ads"},
    {"budzet": 24.1, "przychod": 106.5, "typ": "google_ads"},
    
    {"budzet": 32.5, "przychod": 115.6, "typ": "tv"},
    {"budzet": 45.8, "przychod": 158.2, "typ": "tv"},
    {"budzet": 38.2, "przychod": 132.7, "typ": "tv"},
    {"budzet": 52.6, "przychod": 178.9, "typ": "tv"},
    {"budzet": 41.3, "przychod": 142.5, "typ": "tv"},
    {"budzet": 35.7, "przychod": 125.8, "typ": "tv"},
    {"budzet": 48.9, "przychod": 168.4, "typ": "tv"},
    {"budzet": 43.2, "przychod": 149.7, "typ": "tv"},
    {"budzet": 37.5, "przychod": 128.9, "typ": "tv"},
    {"budzet": 50.1, "przychod": 172.3, "typ": "tv"},
]

# KROK 1: Grupowanie danych według typu kampanii
social_media = [d for d in dane_kampanii if d["typ"] == "social_media"]
google_ads = [d for d in dane_kampanii if d["typ"] == "google_ads"]
tv = [d for d in dane_kampanii if d["typ"] == "tv"]

# KROK 2: Przygotowanie list współrzędnych dla każdej grupy
sm_budzet = [d["budzet"] for d in social_media]
sm_przychod = [d["przychod"] for d in social_media]

ga_budzet = [d["budzet"] for d in google_ads]
ga_przychod = [d["przychod"] for d in google_ads]

tv_budzet = [d["budzet"] for d in tv]
tv_przychod = [d["przychod"] for d in tv]

# KROK 3: Tworzenie wykresu
plt.figure(figsize=(12, 8))

# KROK 4: Rysowanie punktów dla każdej grupy
# plt.scatter() tworzy wykres punktowy
# s - rozmiar punktów
# alpha - przezroczystość (0-1)
# edgecolors - kolor obramowania punktów
# linewidths - grubość obramowania

plt.scatter(sm_budzet, sm_przychod, 
            s=100,                  # Rozmiar punktów
            alpha=0.6,              # Przezroczystość
            color='#3498db',        # Niebieski
            edgecolors='navy',      # Ciemnoniebieski obrys
            linewidths=1.5,
            label='Social Media')

plt.scatter(ga_budzet, ga_przychod, 
            s=100, 
            alpha=0.6, 
            color='#e74c3c',        # Czerwony
            edgecolors='darkred',
            linewidths=1.5,
            label='Google Ads')

plt.scatter(tv_budzet, tv_przychod, 
            s=100, 
            alpha=0.6, 
            color='#2ecc71',        # Zielony
            edgecolors='darkgreen',
            linewidths=1.5,
            label='Reklama TV')

# KROK 5: Dodanie linii trendu (regresja liniowa - uproszczona)
# Obliczamy średni współczynnik przychodu/budżet dla wszystkich danych
wszystkie_budzety = [d["budzet"] for d in dane_kampanii]
wszystkie_przychody = [d["przychod"] for d in dane_kampanii]

# Prosta regresja: y = ax + b
# Znajdź najlepsze dopasowanie linii
import statistics
sredni_stosunek = statistics.mean([p/b for p, b in zip(wszystkie_przychody, wszystkie_budzety)])

# Rysujemy linię trendu
x_trend = [0, max(wszystkie_budzety)]
y_trend = [0, max(wszystkie_budzety) * sredni_stosunek]
plt.plot(x_trend, y_trend, 
         color='gray', 
         linestyle='--', 
         linewidth=2, 
         alpha=0.5,
         label=f'Trend (ROI: {sredni_stosunek:.1f}x)')

# KROK 6: Opisy
plt.title('Analiza ROI kampanii marketingowych - Budżet vs Przychody', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Budżet reklamowy (tys. PLN)', fontsize=13)
plt.ylabel('Przychody ze sprzedaży (tys. PLN)', fontsize=13)

# KROK 7: Legenda i siatka
plt.legend(loc='upper left', fontsize=11, framealpha=0.9)
plt.grid(True, alpha=0.3, linestyle='--')

# Ustawiamy zakres osi zaczynając od 0
plt.xlim(0, max(wszystkie_budzety) * 1.1)
plt.ylim(0, max(wszystkie_przychody) * 1.1)

plt.tight_layout()
plt.show()

# ANALIZA DANYCH
print("\n=== ANALIZA EFEKTYWNOŚCI KAMPANII ===")
for typ, dane in [("Social Media", social_media), ("Google Ads", google_ads), ("TV", tv)]:
    roi_srednie = statistics.mean([d["przychod"]/d["budzet"] for d in dane])
    print(f"{typ}: średni ROI = {roi_srednie:.2f}x (za każdą złotówkę {roi_srednie:.2f} zł przychodu)")

# ĆWICZENIE:
# 1. Dodaj czwarty typ kampanii (np. influencer marketing)
# 2. Zmień rozmiar punktów proporcjonalnie do ROI
# 3. Dodaj adnotacje (plt.annotate()) dla najlepszych kampanii
