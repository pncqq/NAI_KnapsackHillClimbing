# 🎒 NAI_KnapsackHillClimbing

Rozwiązanie problemu plecakowego z wykorzystaniem algorytmu **Hill Climbing**.

Celem projektu jest znalezienie najlepszego zestawu przedmiotów do spakowania do plecaka o ograniczonej pojemności, poprzez lokalne przeszukiwanie rozwiązań i iteracyjne ulepszanie wyniku.

## 📦 Zawartość repozytorium

- `main.py` – implementacja algorytmu Hill Climbing
- `.idea/` – pliki środowiska (PyCharm)

## 🧠 Opis algorytmu

Algorytm **Hill Climbing** rozpoczyna od losowego rozwiązania i przeszukuje jego najbliższe sąsiedztwo w poszukiwaniu lepszego wyniku. Proces ten trwa do momentu, gdy nie można znaleźć lepszego rozwiązania w sąsiedztwie (tzw. lokalne optimum).

W kontekście problemu plecakowego:
- Reprezentacja rozwiązania: zestaw przedmiotów (0/1)
- Funkcja celu: suma wartości przedmiotów (przy ograniczeniu wagi)

## ⚙️ Technologie

- Python 3.x

## ▶️ Jak uruchomić

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/pncqq/NAI_KnapsackHillClimbing.git
   cd NAI_KnapsackHillClimbing
   ```

2. Uruchom program:
   ```bash
   python main.py
   ```

> 📌 Parametry problemu i danych wejściowych są zahardcodowane w pliku `main.py`. Można je łatwo zmodyfikować, np. zmienić liczbę przedmiotów, ich wagi i wartości, lub pojemność plecaka.

## 👨‍💻 Autor

**Filip Michalski**  
Projekt stworzony w ramach kursu NAI (Narzędzia AI).  
Przykład użycia metaheurystyki do rozwiązywania problemów optymalizacyjnych.
