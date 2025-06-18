# Nur Einträge mit Datum im Jahr 2024 behalten
df_tag = df_tag[df_tag["Datum"].dt.year == 2024].copy()
