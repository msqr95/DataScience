# Merge über die Station ID
df_merged = pd.merge(df_tag, df_features, on="Station ID", how="left")

# Vorschau anzeigen
print("Merge erfolgreich:", df_merged.shape)
df_merged.head()
