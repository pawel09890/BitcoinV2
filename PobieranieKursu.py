import numpy as np
import csv



# 🔹 Funkcja wczytująca dane historyczne z pliku CSV
def load_historical_data(filename="Wyniki1.csv"):
    """
    Wczytuje kursy Bitcoina z pliku CSV i zwraca tablicę NumPy.

    Zwraca:
    - np.array: Tablica wartości cen Bitcoina.
    """
    data = []
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Pominięcie nagłówka
        for row in reader:
            data.append(float(row[1]))  # Pobranie wartości cenowych
    return np.array(data)


# 🔹 Pobranie historycznych wartości cen
historical_data = load_historical_data()


# 🔹 Uruchomienie algorytmu
if __name__ == "__main__":
    load_historical_data(filename="Wyniki1.csv")