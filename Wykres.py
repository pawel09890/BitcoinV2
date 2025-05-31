import matplotlib.pyplot as plt
import pandas as pd

# Wczytanie rzeczywistych kursów
df_actual = pd.read_csv("Wyniki1.csv")
# Wczytanie  kursó estymacji
df_estimated = pd.read_csv("Estymacje.csv")

# Pobranie ostatnich 30 notowań
df_actual_last_30 = df_actual.tail(30)
df_estimated_last_30 = df_estimated.tail(10)

# Tworzenie wykresów
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Wykres rzeczywistego kursu
axes[0].plot(df_actual["Data i czas"], df_actual["Cena (USD)"], label="Rzeczywisty kurs", color="blue")
axes[0].set_title("Rzeczywisty kurs Bitcoina")
axes[0].set_xlabel("Data i czas")
axes[0].set_ylabel("Cena (USD)")
axes[0].legend()
axes[0].tick_params(axis='x', rotation=45)

# Wykres estymowanego kursu
axes[1].plot(df_estimated["Data i czas"], df_estimated["Przewidywana wartość"], label="Estymowany kurs", color="red")
axes[1].set_title("Estymowany kurs Bitcoina")
axes[1].set_xlabel("Data i czas")
axes[1].set_ylabel("Cena (USD)")
axes[1].legend()
axes[1].tick_params(axis='x', rotation=45)

# Wykres ostatnich 30 notowan i estymowanego kursu
axes[2].plot(df_actual_last_30["Data i czas"], df_actual_last_30["Cena (USD)"], label="Ostatnie 30 notowań", color="blue")
axes[2].plot(df_estimated_last_30["Data i czas"], df_estimated_last_30["Przewidywana wartość"], label="Estymowany kurs (ostatnie 30)", color="red")
axes[2].set_title("Ostatnie 30 notowań i estymowany kurs")
axes[2].set_xlabel("Data i czas")
axes[2].set_ylabel("Cena (USD)")
axes[2].legend()
axes[2].tick_params(axis='x', rotation=45)

plt.tight_layout()
#plt.show()