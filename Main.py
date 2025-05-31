from PobieranieAPI import get_historical_prices
from Estymacja import genetic_algorithm, load_historical_data
from Wykres import plt



ACTUAL_PRICES_FILE = "Wyniki1.csv"
OUTPUT_ESTIMATIONS_FILE = "Estymacje.csv"

if __name__ == "__main__":
    print("Rozpoczynam pobieranie danych z API...")

    # Pobranie danych i zapis do pliku
    get_historical_prices()


    print("Rozpoczynam estymację przyszłych wartości...")

    # Wczytanie historycznych danych i uruchomienie algorytmu genetycznego
    historical_data = load_historical_data(ACTUAL_PRICES_FILE)
    genetic_algorithm(historical_data=historical_data, output_file=OUTPUT_ESTIMATIONS_FILE)

    print(f"\n✅ Wyniki estymacji zapisano do pliku {OUTPUT_ESTIMATIONS_FILE}")
    #plt.show()


