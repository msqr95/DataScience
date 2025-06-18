# Stationen vorbereiten

# Eindeutige Kombinationen aus ID + Koordinaten extrahieren
stationen = df_tag[["Station ID", "Station Shortname", "Station Longitude", "Station Latitude"]].drop_duplicates()

# Index zurücksetzen
stationen.reset_index(drop=True, inplace=True)
    
# Vorschau
print("Anzahl eindeutiger Berliner Stationen:", len(stationen))
display(stationen.head(25))
