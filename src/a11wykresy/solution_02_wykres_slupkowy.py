"""
Rozwiązanie ćwiczeń do Przykładu 2: Wykres słupkowy
====================================================

ROZWIĄZANE ZADANIA:
1. Zmień wykres na poziomy (użyj plt.barh())
2. Dodaj drugi rok danych i stwórz wykres porównawczy
3. Posortuj języki według popularności malejąco

JAK URUCHOMIĆ:
python solution_02_wykres_slupkowy.py
"""

import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# ZADANIE 1: Wykres poziomy (plt.barh())
# =============================================================================

def zadanie_1_wykres_poziomy():
    """Wykres słupkowy poziomy"""

    # Dane
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

    # Przygotowanie danych
    jezyki = [rekord["jezyk"] for rekord in dane_jezykow]
    popularnosc = [rekord["popularnosc"] for rekord in dane_jezykow]

    # Tworzenie wykresu poziomego
    plt.figure(figsize=(10, 8))

    # plt.barh() tworzy wykres słupkowy POZIOMY
    # Pierwszy argument: pozycje na osi Y (nazwy języków)
    # Drugi argument: długości słupków (wartości popularności)
    slupki = plt.barh(jezyki, popularnosc,
                      color='skyblue',
                      edgecolor='navy',
                      linewidth=1.5)

    # Dodanie wartości na słupkach
    for i, (jezyk, wartosc) in enumerate(zip(jezyki, popularnosc)):
        # Dla wykresu poziomego: pierwsza współrzędna to X (wartość), druga to Y (pozycja)
        plt.text(wartosc + 1, i, f'{wartosc}%',
                 ha='left', va='center', fontsize=10, fontweight='bold')

    # Kolorowanie najlepszego wyniku
    max_index = popularnosc.index(max(popularnosc))
    slupki[max_index].set_color('gold')
    slupki[max_index].set_edgecolor('orange')

    # Opisy wykresu
    plt.title('Najpopularniejsze języki programowania w 2024 roku\n(Wykres poziomy)',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Popularność (%)', fontsize=12)
    plt.ylabel('Język programowania', fontsize=12)

    # Ustawienia
    plt.xlim(0, 80)  # Dla wykresu poziomego używamy xlim zamiast ylim
    plt.grid(axis='x', alpha=0.3, linestyle='--')  # Siatka dla osi X

    plt.tight_layout()
    plt.savefig('C:/home/gitHub/LogikaProgramowania/src/a11wykresy/zadanie1_poziomy.png', dpi=300, bbox_inches='tight')
    plt.show()


# =============================================================================
# ZADANIE 2: Wykres porównawczy (dwa lata danych)
# =============================================================================

def zadanie_2_wykres_porownawczy():
    """Wykres porównawczy dwóch lat"""

    # Dane dla dwóch lat
    dane_2023 = [
        {"jezyk": "Python", "popularnosc": 62.3},
        {"jezyk": "JavaScript", "popularnosc": 68.1},
        {"jezyk": "Java", "popularnosc": 48.2},
        {"jezyk": "C#", "popularnosc": 32.5},
        {"jezyk": "C++", "popularnosc": 30.1},
        {"jezyk": "TypeScript", "popularnosc": 20.3},
        {"jezyk": "PHP", "popularnosc": 25.8},
        {"jezyk": "Go", "popularnosc": 15.2}
    ]

    dane_2024 = [
        {"jezyk": "Python", "popularnosc": 68.5},
        {"jezyk": "JavaScript", "popularnosc": 65.3},
        {"jezyk": "Java", "popularnosc": 45.7},
        {"jezyk": "C#", "popularnosc": 34.2},
        {"jezyk": "C++", "popularnosc": 28.9},
        {"jezyk": "TypeScript", "popularnosc": 25.6},
        {"jezyk": "PHP", "popularnosc": 22.1},
        {"jezyk": "Go", "popularnosc": 18.4}
    ]

    # Przygotowanie danych
    jezyki = [rekord["jezyk"] for rekord in dane_2023]
    popularnosc_2023 = [rekord["popularnosc"] for rekord in dane_2023]
    popularnosc_2024 = [rekord["popularnosc"] for rekord in dane_2024]

    # Tworzenie wykresu
    plt.figure(figsize=(14, 8))

    # Pozycje słupków
    x = np.arange(len(jezyki))
    width = 0.35  # Szerokość słupka

    # Tworzenie dwóch zestawów słupków obok siebie
    slupki_2023 = plt.bar(x - width/2, popularnosc_2023, width,
                          label='2023', color='lightcoral',
                          edgecolor='darkred', linewidth=1.5)
    slupki_2024 = plt.bar(x + width/2, popularnosc_2024, width,
                          label='2024', color='skyblue',
                          edgecolor='navy', linewidth=1.5)

    # Dodanie wartości na słupkach
    for slupki in [slupki_2023, slupki_2024]:
        for slupek in slupki:
            wysokosc = slupek.get_height()
            plt.text(slupek.get_x() + slupek.get_width()/2., wysokosc + 0.5,
                    f'{wysokosc:.1f}%',
                    ha='center', va='bottom', fontsize=8)

    # Opisy wykresu
    plt.title('Porównanie popularności języków programowania: 2023 vs 2024',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Język programowania', fontsize=12)
    plt.ylabel('Popularność (%)', fontsize=12)

    # Ustawienia osi X
    plt.xticks(x, jezyki, rotation=45, ha='right')

    # Ustawienia
    plt.ylim(0, 80)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.legend(fontsize=12, loc='upper right')

    plt.tight_layout()
    plt.savefig('C:/home/gitHub/LogikaProgramowania/src/a11wykresy/zadanie2_porownawczy.png', dpi=300, bbox_inches='tight')
    plt.show()


# =============================================================================
# ZADANIE 3: Sortowanie według popularności malejąco
# =============================================================================

def zadanie_3_sortowanie_malejaco():
    """Wykres z językami posortowanymi według popularności malejąco"""

    # Dane
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

    # SORTOWANIE MALEJĄCO według popularności
    dane_posortowane = sorted(dane_jezykow, key=lambda x: x["popularnosc"], reverse=True)

    # Przygotowanie danych
    jezyki = [rekord["jezyk"] for rekord in dane_posortowane]
    popularnosc = [rekord["popularnosc"] for rekord in dane_posortowane]

    # Tworzenie wykresu
    plt.figure(figsize=(12, 7))

    # Gradient kolorów - od najciemniejszego do najjaśniejszego
    kolory = plt.cm.Blues(np.linspace(0.8, 0.3, len(jezyki)))

    slupki = plt.bar(jezyki, popularnosc,
                     color=kolory,
                     edgecolor='navy',
                     linewidth=1.5)

    # Dodanie wartości i pozycji rankingowej na słupkach
    for i, (jezyk, wartosc) in enumerate(zip(jezyki, popularnosc)):
        plt.text(i, wartosc + 1, f'#{i+1}\n{wartosc}%',
                 ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Specjalne podkreślenie TOP 3
    for i in range(min(3, len(slupki))):
        if i == 0:
            slupki[i].set_color('gold')
            slupki[i].set_edgecolor('orange')
        elif i == 1:
            slupki[i].set_color('silver')
            slupki[i].set_edgecolor('gray')
        elif i == 2:
            slupki[i].set_color('#CD7F32')  # Brązowy
            slupki[i].set_edgecolor('#8B4513')

    # Opisy wykresu
    plt.title('Ranking języków programowania 2024\n(posortowane według popularności)',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Język programowania', fontsize=12)
    plt.ylabel('Popularność (%)', fontsize=12)

    # Ustawienia
    plt.ylim(0, 80)
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.savefig('C:/home/gitHub/LogikaProgramowania/src/a11wykresy/zadanie3_sortowanie.png', dpi=300, bbox_inches='tight')
    plt.show()


# =============================================================================
# BONUS: Wszystkie trzy zadania w jednym - wykres poziomy z sortowaniem
# =============================================================================

def bonus_kompleksowe_rozwiazanie():
    """Wykres poziomy z dwoma latami danych i sortowaniem"""

    # Dane dla dwóch lat
    dane_2023 = [
        {"jezyk": "Python", "popularnosc": 62.3},
        {"jezyk": "JavaScript", "popularnosc": 68.1},
        {"jezyk": "Java", "popularnosc": 48.2},
        {"jezyk": "C#", "popularnosc": 32.5},
        {"jezyk": "C++", "popularnosc": 30.1},
        {"jezyk": "TypeScript", "popularnosc": 20.3},
        {"jezyk": "PHP", "popularnosc": 25.8},
        {"jezyk": "Go", "popularnosc": 15.2}
    ]

    dane_2024 = [
        {"jezyk": "Python", "popularnosc": 68.5},
        {"jezyk": "JavaScript", "popularnosc": 65.3},
        {"jezyk": "Java", "popularnosc": 45.7},
        {"jezyk": "C#", "popularnosc": 34.2},
        {"jezyk": "C++", "popularnosc": 28.9},
        {"jezyk": "TypeScript", "popularnosc": 25.6},
        {"jezyk": "PHP", "popularnosc": 22.1},
        {"jezyk": "Go", "popularnosc": 18.4}
    ]

    # Sortowanie według popularności 2024 (malejąco)
    dane_2024_sorted = sorted(dane_2024, key=lambda x: x["popularnosc"], reverse=True)

    # Tworzenie słownika dla szybkiego dostępu do danych 2023
    mapa_2023 = {d["jezyk"]: d["popularnosc"] for d in dane_2023}

    # Przygotowanie posortowanych danych
    jezyki = [rekord["jezyk"] for rekord in dane_2024_sorted]
    popularnosc_2023 = [mapa_2023[jezyk] for jezyk in jezyki]
    popularnosc_2024 = [rekord["popularnosc"] for rekord in dane_2024_sorted]

    # Tworzenie wykresu poziomego
    plt.figure(figsize=(12, 10))

    # Pozycje słupków
    y = np.arange(len(jezyki))
    height = 0.35  # Wysokość słupka

    # Tworzenie dwóch zestawów słupków poziomych
    slupki_2023 = plt.barh(y + height/2, popularnosc_2023, height,
                           label='2023', color='lightcoral',
                           edgecolor='darkred', linewidth=1.5, alpha=0.8)
    slupki_2024 = plt.barh(y - height/2, popularnosc_2024, height,
                           label='2024', color='skyblue',
                           edgecolor='navy', linewidth=1.5, alpha=0.8)

    # Dodanie wartości na słupkach
    for i, (val_2023, val_2024) in enumerate(zip(popularnosc_2023, popularnosc_2024)):
        # Wartości dla 2023
        plt.text(val_2023 + 1, i + height/2, f'{val_2023:.1f}%',
                 ha='left', va='center', fontsize=9)
        # Wartości dla 2024
        plt.text(val_2024 + 1, i - height/2, f'{val_2024:.1f}%',
                 ha='left', va='center', fontsize=9, fontweight='bold')
        # Pozycja w rankingu
        plt.text(-3, i, f'#{i+1}', ha='right', va='center',
                 fontsize=10, fontweight='bold', color='navy')

    # Opisy wykresu
    plt.title('Ranking i porównanie popularności języków programowania\n2023 vs 2024 (posortowane wg 2024)',
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Popularność (%)', fontsize=12)
    plt.ylabel('Język programowania', fontsize=12)

    # Ustawienia osi Y
    plt.yticks(y, jezyki)

    # Ustawienia
    plt.xlim(0, 80)
    plt.grid(axis='x', alpha=0.3, linestyle='--')
    plt.legend(fontsize=12, loc='lower right')

    # Dodanie linii referencyjnej
    plt.axvline(x=50, color='red', linestyle=':', linewidth=1, alpha=0.5, label='50% próg')

    plt.tight_layout()
    plt.savefig('C:/home/gitHub/LogikaProgramowania/src/a11wykresy/bonus_kompleksowy.png', dpi=300, bbox_inches='tight')
    plt.show()


# =============================================================================
# GŁÓWNA FUNKCJA - uruchamia wszystkie rozwiązania
# =============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("ROZWIĄZANIA ĆWICZEŃ - Wykresy słupkowe")
    print("=" * 70)

    print("\n[1/4] Zadanie 1: Wykres poziomy (plt.barh())")
    print("-" * 70)
    zadanie_1_wykres_poziomy()

    print("\n[2/4] Zadanie 2: Wykres porównawczy (dwa lata)")
    print("-" * 70)
    zadanie_2_wykres_porownawczy()

    print("\n[3/4] Zadanie 3: Sortowanie według popularności")
    print("-" * 70)
    zadanie_3_sortowanie_malejaco()

    print("\n[4/4] BONUS: Kompleksowe rozwiązanie (poziomy + porównawczy + sortowanie)")
    print("-" * 70)
    bonus_kompleksowe_rozwiazanie()

    print("\n" + "=" * 70)
    print("Wszystkie wykresy zostały wygenerowane i zapisane!")
    print("=" * 70)

