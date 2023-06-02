import random


# Przedmiot zawiera wage i wartosc
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


# Generowanie losowych przedmiotów
def generate_items(weights, values):
    items = []
    for i in range(len(weights)):
        items.append(Item(weights[i], values[i]))
    return items


# Czy rozwiązanie jest poprawne (czy miesci sie w plecaku)
# Zwraca wartość rozwiązania
def calculate_fitness(solution, items, max_weight):
    total_weight = 0
    total_value = 0
    for i in range(len(solution)):
        if solution[i] == 1:  # jesli w slocie jest przedmiot
            total_weight += items[i].weight  # sumujemy wage plecaka
            total_value += items[i].value  # sumujemy wartosc plecaka
            if total_weight > max_weight:  # jesli przekroczymy wage, zwracamy 0
                return 0
    return total_value


# Generacja pierwszego rozwiązania
def generate_initial_solution(num_items):
    return [random.randint(0, 1) for _ in range(num_items)]


# Generuje sasiedztwo dla rozwiazania
def get_neighborhood(solution):
    neighborhood = []
    for i in range(len(solution)):
        neighbor = solution.copy()
        neighbor[i] = 1 - neighbor[i]  # Odwracanie bitu
        neighborhood.append(neighbor)
    return neighborhood


def local_search(items, max_weight, min_knapsack_value):
    iterations = 0
    best_fitness = 0

    while best_fitness < min_knapsack_value:

        best_solution = generate_initial_solution(len(items))  # initial solution
        while best_fitness == 0:
            best_solution = generate_initial_solution(len(items))  # cant be zero
            best_fitness = calculate_fitness(best_solution, items, max_weight)

        neighborhood = get_neighborhood(best_solution)
        # Przechodzimy przez wszystkich sasiadow
        for neighbor in neighborhood:
            fitness = calculate_fitness(neighbor, items, max_weight)  # Obliczamy
            if fitness > best_fitness:
                best_solution = neighbor
                best_fitness = fitness
        iterations += 1
    return best_solution, best_fitness


# Parametry
num_items = 20
max_value = 15
max_weight = 75
max_iterations = 1000
min_knapsack_value = 250


weights = [3, 1, 6, 10, 1, 4, 9, 1, 7, 2, 6, 1, 6, 2, 2, 4, 8, 1, 7, 3, 6, 2, 9, 5, 3, 3, 4, 7, 3, 5, 30, 50]
values = [7, 4, 9, 18, 9, 15, 4, 2, 6, 13, 18, 12, 12, 16, 19, 19, 10, 16, 14, 3, 14, 4, 15, 7, 5, 10, 10, 13, 19, 9, 8,
          5]

items = generate_items(weights, values)
best_solution, best_fitness = local_search(items, max_weight, min_knapsack_value)
print(f'Najlepsze rozwiązanie: {best_solution}\n'
      f'Wartość plecaka: {best_fitness}')
