# 1. Zielvariable direkt extrahieren
y = df_merged["Tagesmittel"]

# 2. Erklärende Variablen: alle OSM-Features (enden auf _100m, _250m, _500m)
feature_cols = [col for col in df_merged.columns if any(r in col for r in ["_100m", "_250m", "_500m"])]
X = df_merged[feature_cols]

# 3. Übersicht
print("Features:", feature_cols)
print("X-Shape:", X.shape, "| y-Shape:", y.shape)
