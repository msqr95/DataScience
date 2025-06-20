# Bibliotheken
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Festlegen der Spaltennamen entsprechend deines DataFrames
date_col = "Start Datetime"
comp_col = "Component Name"
mean_col = "Value"
station_col = "Station ID"

# Daten für PM2 filtern und vorbereiten
df_pm2 = df[df[comp_col] == "PM2"].copy()
df_pm2[date_col] = pd.to_datetime(df_pm2[date_col])
df_pm2["Monat"] = df_pm2[date_col].dt.month

# Histogramm der Tagesmittelwerte (PM2)
plt.figure(figsize=(10, 6))
sns.histplot(df_pm2[mean_col], bins=30, kde=True, color="steelblue")
plt.title("Histogramm der PM2.5-Messwerte, Berlin (2024)")
plt.xlabel("PM2.5-Wert")
plt.ylabel("Häufigkeit")
plt.grid(True)
plt.tight_layout()
plt.show()

# Boxplot nach Monat
plt.figure(figsize=(12, 6))
sns.boxplot(x="Monat", y=mean_col, data=df_pm2, palette="Blues")
plt.title("PM2.5-Messwerte nach Monat, Berlin (2024)")
plt.xlabel("Monat")
plt.ylabel("PM2.5-Wert")
plt.grid(True)
plt.tight_layout()
plt.show()

# Zeitreihe einer Beispielstation
example_station = df_pm2[station_col].iloc[0]
df_example = df_pm2[df_pm2[station_col] == example_station].sort_values(by=date_col)

plt.figure(figsize=(14, 5))
plt.plot(df_example[date_col], df_example[mean_col], marker='o', linestyle='-', linewidth=1)
plt.title(f"Zeitreihe der PM2.5-Werte – Station {example_station} (2024)")
plt.xlabel("Datum")
plt.ylabel("PM2.5-Wert")
plt.grid(True)
plt.tight_layout()
plt.show()
