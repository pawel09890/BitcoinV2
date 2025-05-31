import numpy as np
import csv
from datetime import datetime, timezone, timedelta
from deap import base, creator, tools, algorithms
from Wykres import plt

# Wczytanie danych historycznych
def load_historical_data(filename="Wyniki1.csv"):
    """Wczytuje kursy Bitcoina z pliku CSV i zwraca tablicę NumPy."""
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Pominięcie nagłówka
        return np.array([float(row[1]) for row in reader])

historical_data = load_historical_data()
# Zwiększam zakres cenowy o +-10000usd
min_price, max_price = min(historical_data) - 10000, max(historical_data) + 10000

# Funkcja oceny osobnika
def evaluate(individual, last_10_prices):
    """Ocena osobnika na podstawie przewidywanej zmiany ceny."""
    predicted_value = last_10_prices[-1] + np.mean(np.diff(individual))
    moving_average = np.mean(last_10_prices[-24:]) #srednia kroczaca
#  propozycja
    # Ważone prognozowanie: 70% predykcja + 30% średnia krocząca
    weighted_prediction = (predicted_value * 0.3) + (moving_average * 0.2) + (historical_data[-1] * 0.5)
# propozycja
    return max(min_price, min(weighted_prediction, max_price)),
#
#  return max(min_price, min(predicted_value, max_price)),

# Konfiguracja algorytmu genetycznego
creator.create("FitnessMin", base.Fitness, weights=(-1.0,)) #najlepsze dopasowanie
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", np.random.uniform, min_price, max_price)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, 10)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxBlend, alpha=0.3)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=2.0, indpb=0.4)
toolbox.register("select", tools.selRoulette)

# Główna funkcja uruchamiająca algorytm
def genetic_algorithm(n_generations=500, historical_data=None, output_file="Estymacje.csv"):
    """Uruchamia algorytm genetyczny i generuje prognozy na kolejne 10 godzin."""
    last_10_prices = historical_data[-1000:]
    toolbox.register("evaluate", lambda ind: evaluate(ind, last_10_prices))
    predictions = []

    for i in range(10):
        population = toolbox.population(n=200)
        algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.4, ngen=n_generations, stats=None, halloffame=None, verbose=False)

        best_ind = tools.selBest(population, 1)[0]
        next_value = evaluate(best_ind, last_10_prices)[0]
        last_10_prices = np.append(last_10_prices[1:], next_value) #nowy lisa ostatnich 10 z dodanym wyliczeniem

        timestamp = datetime.now(timezone.utc) + timedelta(hours=i + 1)
        predictions.append((timestamp.strftime("%Y-%m-%d %H:%M:%S"), round(next_value, 10)))

        print(f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')}: Przewidywana wartość = {round(next_value, 10)}")

    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Data i czas", "Przewidywana wartość"])
        writer.writerows(predictions)

    print(f"Wyniki zapisano do {output_file}. Program zakończył działanie.")
    #Rysowanie wykresy dopiro po zaktualizowaniu estymacji
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    genetic_algorithm(historical_data=historical_data)
