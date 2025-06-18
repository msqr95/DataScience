# 1. Gibt es fehlende Werte?
print(" Fehlende Werte pro Spalte:")
print(df_tag.isnull().sum())

# 2. Sind alle Datumseinträge im Jahr 2024?
df_tag["Datum"] = pd.to_datetime(df_tag["Datum"], errors="coerce")
außerhalb = df_tag[~df_tag["Datum"].dt.year.isin([2024])]
print("\n Einträge außerhalb 2024:", len(außerhalb))

# 3. Gibt es doppelte Kombinationen aus Station + Datum?
duplikate = df_tag.duplicated(subset=["Station ID", "Datum"])
print("Doppelte Einträge:", duplikate.sum())

# 4. Gibt es Tagesmittel mit negativen Werten oder unrealistischen Ausreißern?
print("\n Negative Tagesmittel:", (df_tag["Tagesmittel"] < 0).sum())
print("Extrem hohe Werte (Tagesmittel > 500):", (df_tag["Tagesmittel"] > 500).sum())
