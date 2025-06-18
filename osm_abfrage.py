# OSM-Verarbeitung mit Overpass API via overpy (mit Debug-Ausgabe & Testlauf für 1 Station)

import overpy
import pandas as pd
import time
from shapely.geometry import Point
from IPython.display import display

# API-Client initialisieren
api = overpy.Overpass()

# Radius in Metern
radien = [100, 250, 500]

# Features, die gezählt werden sollen
feature_sets = {
    "park": '["leisure"="park"]',
    "residential": '["highway"="residential"]',
    "industrial": '["landuse"="industrial"]',
    "railway": '["railway"="rail"]',
    "water": '["natural"="water"]'
}

# Ergebnisliste
feature_matrix = []

# alle Stationen 
for idx, row in stationen.iterrows():
    lat = row["Station Latitude"]
    lon = row["Station Longitude"]
    station_id = row["Station ID"]
    result_row = {"Station ID": station_id}

    for radius in radien:
        for feature_name, tag_filter in feature_sets.items():
            query = f"""
            [out:json];
            (
              node{tag_filter}(around:{radius},{lat},{lon});
              way{tag_filter}(around:{radius},{lat},{lon});
              relation{tag_filter}(around:{radius},{lat},{lon});
            );
            out body;
            """
            try:
                result = api.query(query)
                count = len(result.nodes) + len(result.ways) + len(result.relations)
                colname = f"{feature_name}_{radius}m"
                result_row[colname] = count
                print(f"�� {idx+1} | {feature_name} @ {radius}m → {count}")
                time.sleep(1)  # API-freundlich
            except Exception as e:
                print(f"Fehler bei {feature_name} / {radius}m: {e}")
                result_row[f"{feature_name}_{radius}m"] = -1
                time.sleep(2)  # bei Fehler langsamer

    feature_matrix.append(result_row)

# In DataFrame umwandeln
df_features = pd.DataFrame(feature_matrix)

# Vorschau anzeigen
print("Feature-Matrix erstellt:", df_features.shape)
display(df_features.head())
