# 1. Bibliotheken importieren
import pandas as pd #https://pandas.pydata.org/docs/whatsnew/v2.3.0.html
import matplotlib.pyplot as plt #https://matplotlib.org/stable/users/prev_whats_new/whats_new_3.10.0.html

# 2. Datei laden und nur berliner Stationen filtern
df = pd.read_csv("pm2_2024-01-01_2025-01-01_all_attributes.csv")
df = df[df["Station City"] == "Berlin"]

# 3. Spalten anzeigen
print(" Spaltenübersicht:")
print(df.columns.tolist())

# 4. Vorschau auf die ersten Zeilen
print("\n Erste 5 Zeilen:")
print(df.head())

# 5. Übersicht über Datentypen und fehlende Werte
print("\n Struktur der Daten:")
print(df.info())
