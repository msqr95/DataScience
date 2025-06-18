# 1. Nur Berliner Stationen auswählen
df_berlin = df[df["Station City"] == "Berlin"].copy()

# 2. Nur PM2.5-Komponente behalten
df_berlin = df_berlin[df_berlin["Component Name"] == "PM2"]

# 3. Zeitspalte in echtes Datetime-Format umwandeln
df_berlin["Start Datetime"] = pd.to_datetime(df_berlin["Start Datetime"])

# 4. Neues Tagesdatum extrahieren (ohne Uhrzeit)
df_berlin["Datum"] = df_berlin["Start Datetime"].dt.date

# 5. Tagesmittel pro Station und Tag berechnen
df_tag = (
    df_berlin.groupby(
        ["Station ID", "Station Shortname", "Station Longitude", "Station Latitude", "Datum"]
    )["Value"]
    .mean(numeric_only=True)
    .reset_index()
)

# 6. Umbenennung für Klarheit
df_tag.rename(columns={"Value": "Tagesmittel"}, inplace=True)

# 7. Vorschau
print(df_tag.head())
