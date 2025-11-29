# Matplotlib - Wprowadzenie do Wizualizacji Danych w Pythonie

## 📊 Spis Treści

1. [Wprowadzenie](#wprowadzenie)
2. [Instalacja i Konfiguracja](#instalacja-i-konfiguracja)
3. [Podstawowe Koncepcje](#podstawowe-koncepcje)
4. [Typy Wykresów](#typy-wykresów)
5. [Przykłady Praktyczne](#przykłady-praktyczne)
6. [Zaawansowane Techniki](#zaawansowane-techniki)
7. [Najlepsze Praktyki](#najlepsze-praktyki)
8. [Zadania do Ćwiczeń](#zadania-do-ćwiczeń)

---

## Wprowadzenie

**Matplotlib** to najpopularniejsza biblioteka do tworzenia wizualizacji danych w Pythonie. Została stworzona w 2003 roku przez Johna D. Huntera i od tego czasu stała się standardem w świecie analizy danych.

### Po co nam wizualizacja danych?

- 🧠 **Ułatwia zrozumienie**: Człowiek przetwarza obrazy 60,000 razy szybciej niż tekst
- 📈 **Odkrywa trendy**: Wzorce i zależności są łatwiejsze do zauważenia na wykresach
- 🎯 **Komunikacja**: Prezentacja wyników w sposób przystępny dla odbiorców
- 🔍 **Analiza**: Szybkie identyfikowanie anomalii i wartości odstających

### Kiedy używać Matplotlib?

✅ Tworzenie wykresów naukowych i publikacji  
✅ Analiza eksploracyjna danych (EDA)  
✅ Wizualizacja wyników eksperymentów  
✅ Dashboardy i raporty  
✅ Prototypowanie wizualizacji

---

## Instalacja i Konfiguracja

### Instalacja

```bash
# Podstawowa instalacja
pip install matplotlib

# Z dodatkowymi zależnościami
pip install matplotlib numpy
```

### Import w Pythonie

```python
import matplotlib.pyplot as plt  # Standardowa konwencja
import numpy as np               # Często używane razem
```

### Pierwsze uruchomienie

```python
import matplotlib.pyplot as plt

# Proste dane
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Rysowanie
plt.plot(x, y)
plt.show()  # Wyświetla wykres
```

---

## Podstawowe Koncepcje

### Architektura Matplotlib

Matplotlib ma hierarchiczną strukturę:

```
Figure (Płótno)
  └── Axes (Obszar wykresu) - może być wiele
      ├── Axis (Osie: X, Y)
      ├── Title (Tytuł)
      ├── Legend (Legenda)
      └── Plotted Data (Dane)
```

### Dwa sposoby tworzenia wykresów

#### 1. MATLAB-style (pyplot) - dla prostych wykresów

```python
plt.plot([1, 2, 3], [4, 5, 6])
plt.title('Prosty wykres')
plt.show()
```

#### 2. Obiektowy (OO-style) - dla większej kontroli

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
ax.set_title('Prosty wykres')
plt.show()
```

**Zalecenie**: Dla studentów na początku używamy stylu pyplot (prostszy), później przechodzimy na styl obiektowy (bardziej elastyczny).

### Podstawowe elementy wykresu

```python
plt.figure(figsize=(10, 6))        # Rozmiar wykresu
plt.plot(x, y)                     # Rysowanie danych
plt.title('Tytuł wykresu')         # Tytuł
plt.xlabel('Oś X')                 # Etykieta osi X
plt.ylabel('Oś Y')                 # Etykieta osi Y
plt.grid(True)                     # Siatka
plt.legend()                       # Legenda
plt.show()                         # Wyświetl
```

---

## Typy Wykresów

### 1. Wykres Liniowy (`plt.plot()`)

**Zastosowanie**: Pokazanie trendu w czasie, ciągłe zmiany

**Przykład**: `01_podstawowy_wykres_liniowy.py`

**Kluczowe parametry**:
- `marker`: styl punktów (`'o'`, `'s'`, `'^'`, `'D'`)
- `linestyle`: styl linii (`'-'`, `'--'`, `'-.'`, `':'`)
- `color`: kolor (`'red'`, `'#FF5733'`)
- `linewidth`: grubość linii

```python
plt.plot(x, y, marker='o', linestyle='-', color='blue', linewidth=2)
```

**Kiedy używać**:
- Dane czasowe (sprzedaż w czasie, temperatura)
- Trendy i zmiany
- Porównanie kilku serii danych

---

### 2. Wykres Słupkowy (`plt.bar()`)

**Zastosowanie**: Porównanie kategorii, dyskretne wartości

**Przykład**: `02_wykres_slupkowy.py`, `07_grupowany_slupkowy.py`

**Kluczowe parametry**:
- `width`: szerokość słupków
- `color`: kolor słupków
- `edgecolor`: kolor obramowania
- `alpha`: przezroczystość (0-1)

```python
plt.bar(kategorie, wartości, color='skyblue', edgecolor='navy')
```

**Odmiany**:
- `plt.bar()`: słupki pionowe
- `plt.barh()`: słupki poziome
- Grupowane: wiele serii obok siebie
- Skumulowane: słupki na sobie (parametr `bottom`)

**Kiedy używać**:
- Porównanie wartości między kategoriami
- Ranking, top listy
- Dane dyskretne

---

### 3. Wykres Punktowy (`plt.scatter()`)

**Zastosowanie**: Korelacje, relacje między zmiennymi

**Przykład**: `04_scatter_plot.py`

**Kluczowe parametry**:
- `s`: rozmiar punktów
- `c`: kolor (może być wartością dla gradientu)
- `alpha`: przezroczystość
- `cmap`: paleta kolorów dla gradientu

```python
plt.scatter(x, y, s=100, c=kolory, alpha=0.6, cmap='viridis')
```

**Kiedy używać**:
- Analiza korelacji między dwoma zmiennymi
- Identyfikacja klastrów i wzorców
- Wykrywanie wartości odstających

---

### 4. Wykres Kołowy (`plt.pie()`)

**Zastosowanie**: Udziały procentowe, części całości

**Przykład**: `05_wykres_kolowy.py`

**Kluczowe parametry**:
- `labels`: etykiety wycinków
- `autopct`: format procentów
- `explode`: wysunięcie wycinków
- `startangle`: kąt początkowy

```python
plt.pie(wartości, labels=etykiety, autopct='%1.1f%%', startangle=90)
```

**Kiedy używać**:
- Pokazanie udziałów w całości
- Maksymalnie 5-7 kategorii (więcej = nieczytelne)
- **UWAGA**: Często krytykowany, alternatywa: wykres słupkowy

---

### 5. Histogram (`plt.hist()`)

**Zastosowanie**: Rozkład częstości, dystrybucja danych

**Przykład**: `06_histogram.py`

**Kluczowe parametry**:
- `bins`: liczba przedziałów
- `density`: normalizacja do rozkładu prawdopodobieństwa
- `cumulative`: histogram skumulowany
- `histtype`: typ (`'bar'`, `'step'`, `'stepfilled'`)

```python
plt.hist(dane, bins=20, color='skyblue', edgecolor='black')
```

**Kiedy używać**:
- Analiza rozkładu danych
- Sprawdzenie normalności rozkładu
- Identyfikacja modów (szczytów)

---

### 6. Wykres Pudełkowy (`plt.boxplot()`)

**Zastosowanie**: Statystyki opisowe, porównanie rozkładów

**Przykład**: `10_boxplot.py`

**Elementy boxplota**:
```
    Outlier → o
              |
    Max   → ──┬──
              │
    Q3    → ┌─┴─┐
            │   │  ← IQR (Interquartile Range)
    Med.  → ├───┤  ← Mediana
            │   │
    Q1    → └─┬─┘
              │
    Min   → ──┴──
              |
    Outlier → o
```

**Kluczowe parametry**:
- `notch`: wcięcie dla mediany
- `showmeans`: pokazuj średnią
- `vert`: orientacja (True=pionowo, False=poziomo)

**Kiedy używać**:
- Porównanie rozkładów między grupami
- Identyfikacja wartości odstających
- Analiza statystyk (mediana, kwartyle)

---

### 7. Mapa Cieplna (`plt.imshow()`)

**Zastosowanie**: Wizualizacja macierzy, korelacji, zależności 2D

**Przykład**: `11_heatmap.py`

**Kluczowe parametry**:
- `cmap`: paleta kolorów
- `vmin`, `vmax`: zakres wartości
- `interpolation`: metoda interpolacji

```python
plt.imshow(macierz, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()  # Pasek legend kolorów
```

**Popularne palety (cmap)**:
- `'viridis'`: uniwersalna, dostępna dla daltonistów
- `'coolwarm'`: dla wartości dodatnich/ujemnych
- `'YlOrRd'`: żółty-pomarańczowy-czerwony (ciepła)

**Kiedy używać**:
- Macierze korelacji
- Dane 2D (temperatura na mapie, gęstość)
- Porównanie wielu zmiennych

---

## Przykłady Praktyczne

### Przykład 1: Podstawowy Wykres Liniowy
**Plik**: `01_podstawowy_wykres_liniowy.py`

**Scenariusz**: Sprzedaż lodów w lodziarni przez rok

**Kluczowe elementy**:
- Sezonowość danych (lato vs zima)
- Dodawanie znaczników (markers)
- Formatowanie tytułów i etykiet
- Siatka dla lepszej czytelności

**Czego się nauczysz**:
- Podstawowa struktura wykresu
- `plt.plot()` z parametrami
- Rotacja etykiet `plt.xticks(rotation=45)`
- `plt.tight_layout()` dla lepszego układu

---

### Przykład 2: Wykres Słupkowy
**Plik**: `02_wykres_slupkowy.py`

**Scenariusz**: Popularność języków programowania

**Kluczowe elementy**:
- Kolorowanie słupków
- Dodawanie wartości nad słupkami (`plt.text()`)
- Wyróżnianie najlepszego wyniku (zmiana koloru)
- Siatka tylko dla osi Y

**Czego się nauczysz**:
- `plt.bar()` i jego parametry
- Iteracja po słupkach dla dostosowania
- Dodawanie adnotacji tekstowych
- Kontrola zakresów osi (`plt.ylim()`)

---

### Przykład 3: Wiele Linii
**Plik**: `03_wiele_linii.py`

**Scenariusz**: Porównanie cen akcji PKN Orlen, PZU, PGE

**Kluczowe elementy**:
- Wiele serii danych na jednym wykresie
- Różne style linii i markerów
- Linie referencyjne (średnia)
- Legenda z opisem

**Czego się nauczysz**:
- Dodawanie wielu linii
- Kody kolorów hex (`#1f77b4`)
- `plt.axhline()` dla linii poziomych
- Praca z legendą

---

### Przykład 4: Scatter Plot
**Plik**: `04_scatter_plot.py`

**Scenariusz**: Analiza ROI kampanii marketingowych (budżet vs przychody)

**Kluczowe elementy**:
- Grupowanie danych według kategorii
- Różne kolory dla różnych grup
- Linia trendu (prosta regresja)
- Analiza korelacji

**Czego się nauczysz**:
- `plt.scatter()` z różnymi grupami
- Obliczanie i wizualizacja trendu
- Interpretacja korelacji
- Filtrowanie list pythonowych

---

### Przykład 5: Wykres Kołowy
**Plik**: `05_wykres_kolowy.py`

**Scenariusz**: Udziały platform streamingowych (Netflix, HBO Max, Disney+)

**Kluczowe elementy**:
- Niestandardowe kolory (kolory brandów)
- Wysunięcie wycinków (`explode`)
- Format procentów
- Legenda poza wykresem

**Czego się nauczysz**:
- `plt.pie()` z wszystkimi parametrami
- `autopct` dla formatowania
- `plt.axis('equal')` dla idealnego koła
- Pozycjonowanie legendy

---

### Przykład 6: Histogram
**Plik**: `06_histogram.py`

**Scenariusz**: Rozkład wynagrodzeń w branży IT (Junior, Mid, Senior, Lead)

**Kluczowe elementy**:
- Generowanie realistycznych danych
- Histogramy nałożone (overlaid)
- Linie statystyk (średnia, mediana)
- Obliczenia statystyczne

**Czego się nauczysz**:
- `plt.hist()` z różnymi opcjami
- Subploty dla porównań
- `plt.axvline()` dla linii pionowych
- Moduł `statistics`

---

### Przykład 7: Grupowany Słupkowy
**Plik**: `07_grupowany_slupkowy.py`

**Scenariusz**: Sprzedaż smartfonów, laptopów, tabletów w kwartałach

**Kluczowe elementy**:
- Grupowanie słupków obok siebie
- NumPy dla pozycjonowania
- Wartości nad każdym słupkiem
- Analiza wzrostu

**Czego się nauczysz**:
- Używanie `numpy.arange()`
- Przesunięcie słupków (offset)
- Funkcje pomocnicze dla adnotacji
- Formatowanie liczb (`f-string`)

---

### Przykład 8: Subplots
**Plik**: `08_subplots.py`

**Scenariusz**: Kompleksowa analiza klimatu Warszawy (temperatura, opady, wilgotność, wiatr)

**Kluczowe elementy**:
- Siatka 2x2 wykresów
- Różne typy w różnych panelach
- Wspólny tytuł
- Colorbar dla scatter

**Czego się nauczysz**:
- `plt.subplots(nrows, ncols)`
- Indeksowanie axes `axes[row, col]`
- `plt.colorbar()` dla paska kolorów
- `fig.suptitle()` dla głównego tytułu

---

### Przykład 9: Style Wykresów
**Plik**: `09_style_wykresy.py`

**Scenariusz**: Wzrost użytkowników aplikacji mobilnej w różnych stylach

**Kluczowe elementy**:
- Porównanie predefiniowanych stylów
- Pełne dostosowanie wykresu
- Ukrywanie ramek (`spines`)
- Adnotacje z strzałkami

**Czego się nauczysz**:
- `plt.style.available` i `plt.style.context()`
- Dostosowywanie spines
- `plt.annotate()` dla strzałek
- Zapisywanie wykresów (`plt.savefig()`)

---

### Przykład 10: Boxplot
**Plik**: `10_boxplot.py`

**Scenariusz**: Analiza czasu odpowiedzi mikrousług e-commerce

**Kluczowe elementy**:
- Porównanie wielu grup
- Identyfikacja outlierów
- Linia SLA (Service Level Agreement)
- Interpretacja statystyk

**Czego się nauczysz**:
- `plt.boxplot()` z opcjami
- Czytanie elementów boxplota
- Percentyle i kwartyle
- Wykrywanie problemów wydajności

---

### Przykład 11: Heatmapa
**Plik**: `11_heatmap.py`

**Scenariusz**: Postępy fitness i macierz korelacji aktywności

**Kluczowe elementy**:
- Macierze 2D
- Wartości w komórkach
- Palety kolorów
- Korelacja między zmiennymi

**Czego się nauczysz**:
- `plt.imshow()` dla macierzy
- `numpy.corrcoef()` dla korelacji
- Dodawanie tekstu do komórek
- Interpretacja map cieplnych

---

## Zaawansowane Techniki

### Dostosowywanie Kolorów

```python
# Nazwy kolorów
plt.plot(x, y, color='red')

# Kody hex
plt.plot(x, y, color='#FF5733')

# RGB tuple (0-1)
plt.plot(x, y, color=(0.1, 0.2, 0.5))

# Gradienty (dla scatter, imshow)
plt.scatter(x, y, c=wartości, cmap='viridis')
```

### Formatowanie Tekstu

```python
plt.title('Tytuł', fontsize=16, fontweight='bold', 
          color='navy', family='serif')

plt.xlabel('Oś X', fontsize=12, style='italic')
```

### Zapisywanie Wykresów

```python
# PNG (rasterowy)
plt.savefig('wykres.png', dpi=300, bbox_inches='tight')

# PDF (wektorowy) - idealny do publikacji
plt.savefig('wykres.pdf', bbox_inches='tight')

# SVG (wektorowy) - do edycji graficznej
plt.savefig('wykres.svg', bbox_inches='tight')
```

### Adnotacje i Strzałki

```python
plt.annotate('Ważny punkt',
            xy=(x_punkt, y_punkt),        # Punkt do zaznaczenia
            xytext=(x_tekst, y_tekst),    # Pozycja tekstu
            arrowprops=dict(arrowstyle='->', color='red', lw=2),
            fontsize=12,
            bbox=dict(boxstyle='round', facecolor='yellow'))
```

### Osie Wtórne

```python
fig, ax1 = plt.subplots()

# Pierwsza oś Y (lewa)
ax1.plot(x, y1, 'b-')
ax1.set_ylabel('Y1', color='b')

# Druga oś Y (prawa)
ax2 = ax1.twinx()
ax2.plot(x, y2, 'r-')
ax2.set_ylabel('Y2', color='r')
```

---

## Najlepsze Praktyki

### ✅ DO:

1. **Zawsze dodawaj tytuł i etykiety osi**
   ```python
   plt.title('Co pokazuje wykres')
   plt.xlabel('Nazwa zmiennej X')
   plt.ylabel('Nazwa zmiennej Y z jednostką')
   ```

2. **Używaj siatki dla lepszej czytelności**
   ```python
   plt.grid(True, alpha=0.3)  # alpha dla przezroczystości
   ```

3. **Dobieraj odpowiedni typ wykresu**
   - Trend → wykres liniowy
   - Porównanie kategorii → słupkowy
   - Rozkład → histogram
   - Korelacja → scatter

4. **Używaj kolorów świadomie**
   - Maksymalnie 5-7 kolorów na wykresie
   - Dobieraj kontrastowe kolory
   - Pamiętaj o daltonistach (użyj palet dostępnych, np. 'viridis')

5. **Formatuj wielkości**
   ```python
   plt.figure(figsize=(10, 6))  # Proporcje 5:3 często optymalne
   ```

### ❌ NIE:

1. **Nie przeciążaj wykresu**
   - Maksymalnie 5 linii na wykresie liniowym
   - Nie dodawaj zbędnych elementów dekoracyjnych

2. **Nie używaj wykresów 3D bez potrzeby**
   - Często utrudniają odczyt
   - 2D zazwyczaj lepszy

3. **Nie manipuluj skalą osi**
   - Zawsze zaczynaj od 0 dla wykresów słupkowych
   - Nie ukrywaj różnic przez nieodpowiednią skalę

4. **Nie używaj pie chart dla >7 kategorii**
   - Alternatywa: wykres słupkowy

5. **Nie zapominaj o legendzie dla wielu serii**
   ```python
   plt.legend(loc='best')  # Automatyczne dopasowanie pozycji
   ```

---

## Przydatne Skróty i Komendy

### Najczęściej używane parametry `plt.plot()`

```python
plt.plot(x, y,
    color='blue',           # lub 'b', '#1f77b4'
    linestyle='-',          # '-' '-- ' '-.' ':'
    linewidth=2,            # grubość linii
    marker='o',             # 'o' 's' '^' 'D' '*'
    markersize=8,           # rozmiar znacznika
    label='Seria 1',        # dla legendy
    alpha=0.7)              # przezroczystość 0-1
```

### Pamiętaj o `plt.show()`

```python
# Na końcu programu, aby wyświetlić wykres
plt.show()
```

W Jupyter Notebook możesz też użyć:
```python
%matplotlib inline  # Na początku notebooka
```

---

## Rozwiązywanie Problemów

### Problem: Wykres się nie pokazuje
**Rozwiązanie**: Dodaj `plt.show()` na końcu

### Problem: Etykiety się nakładają
**Rozwiązanie**: 
```python
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
```

### Problem: Wykres jest za mały
**Rozwiązanie**:
```python
plt.figure(figsize=(12, 8))  # Zwiększ rozmiar
```

### Problem: Legenda zakrywa dane
**Rozwiązanie**:
```python
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Poza wykresem
```

### Problem: Kolory są niewyraźne
**Rozwiązanie**:
```python
# Użyj bardziej kontrastowych kolorów
kolory = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12']
```

---

## Zadania do Ćwiczeń

### Zadanie 1: Własne Dane - Podstawy
Stwórz wykres liniowy pokazujący temperaturę przez 7 dni tygodnia.
- Dodaj tytuł "Temperatura w moim mieście"
- Oznacz dni tygodnia na osi X
- Dodaj siatkę
- Zapisz wykres do pliku PNG

### Zadanie 2: Porównanie Kategorii
Stwórz wykres słupkowy pokazujący liczbę godzin nauki różnych przedmiotów w tygodniu.
- Co najmniej 5 przedmiotów
- Posortuj słupki według wartości
- Pokoloruj słupek z największą liczbą godzin na inny kolor

### Zadanie 3: Scatter Plot z Korelacją
Wygeneruj losowe dane symulujące zależność między czasem nauki a oceną.
- Użyj `random` lub `numpy` do generowania danych
- Dodaj linię trendu
- Opisz czy korelacja jest dodatnia czy ujemna

### Zadanie 4: Subplots - Kompleksowa Analiza
Stwórz 4 wykresy (2x2) pokazujące:
1. Wykres liniowy (temperatura)
2. Wykres słupkowy (sprzedaż)
3. Histogram (rozkład ocen)
4. Scatter (wysokość vs waga)

### Zadanie 5: Styl i Estetyka
Weź dowolny poprzedni wykres i:
- Zmień styl na 'seaborn' lub 'ggplot'
- Dostosuj kolory zgodnie z własną paletą
- Dodaj adnotację ze strzałką do najważniejszego punktu
- Dodaj watermark (tekst w rogu)

### Zadanie 6: Dane Rzeczywiste
Znajdź dane CSV online (np. dane COVID, pogodowe, giełdowe) i:
- Wczytaj dane używając `pandas` lub ręcznie
- Stwórz co najmniej 3 różne typy wykresów
- Wyciągnij wnioski z wizualizacji

---

## Dodatkowe Zasoby

### Oficjalna Dokumentacja
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Gallery of Examples](https://matplotlib.org/stable/gallery/index.html)

### Interaktywne Tutoriale
- [Real Python - Matplotlib Guide](https://realpython.com/python-matplotlib-guide/)
- [DataCamp - Matplotlib Tutorial](https://www.datacamp.com/tutorial/matplotlib-tutorial-python)

### Inspiracja i Przykłady
- [Python Graph Gallery](https://www.python-graph-gallery.com/)
- [Matplotlib Cheat Sheets](https://github.com/matplotlib/cheatsheets)

### Biblioteki Pokrewne
- **Seaborn**: Wyższy poziom abstrakcji, piękniejsze wykresy
- **Plotly**: Interaktywne wykresy
- **Pandas plotting**: Wbudowane w pandas
- **Bokeh**: Interaktywne wizualizacje webowe

---

## Podsumowanie

### Kluczowe Punkty

1. **Matplotlib to fundament** wizualizacji w Pythonie
2. **Wybór typu wykresu** zależy od rodzaju danych i przekazu
3. **Prostota jest kluczowa** - nie przeciążaj wykresów
4. **Zawsze opisuj** - tytuł, etykiety, legenda
5. **Eksperymentuj** - najlepiej uczysz się przez praktykę

### Następne Kroki

Po opanowaniu Matplotlib warto poznać:
- 📊 **Seaborn** - dla piękniejszych wykresów statystycznych
- 🗺️ **Plotly** - dla wykresów interaktywnych
- 📈 **Pandas** - dla szybkiej wizualizacji DataFrame'ów
- 🎨 **Altair** - dla deklaratywnej wizualizacji

---

## Kontakt i Wsparcie

Jeśli masz pytania podczas zajęć:
1. Przeanalizuj przykłady kodu
2. Sprawdź komunikaty błędów (error messages)
3. Użyj `help(plt.funkcja)` w Pythonie
4. Zapytaj prowadzącego

**Powodzenia w nauce wizualizacji danych! 🚀📊**

---

*Materiały przygotowane dla studentów kierunków nieinformatycznych - Python jako pierwszy język programowania*

*Wersja: 1.0 | Data: 2024*
