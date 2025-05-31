import csv

def create_fixed_filename():
    """Zawsze tworzy lub nadpisuje plik Estymacje.csv."""
    return "Estymacje.csv"

# Tworzenie nadpisywanego pliku wynikowego
ESTIMATIONS_FILE = create_fixed_filename()

with open(ESTIMATIONS_FILE, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Data i czas", "Przewidywana cena (USD)"])

HISTORICAL_DATA_FILE = "Wyniki1.csv"

def save_data_to_csv(data, filename=HISTORICAL_DATA_FILE):
    """Zapisuje pobrane kursy do pliku Wyniki.csv."""
    if not data:
        print("Brak danych do zapisania.")
        return

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Data i czas", "Cena (USD)"])
            writer.writerows(data)

        print(f"Dane poprawnie zapisano do {filename} ({len(data)} rekordów)")

    except Exception as e:
        print(f"Błąd zapisu do pliku CSV: {e}")
