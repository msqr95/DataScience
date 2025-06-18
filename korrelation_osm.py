## Korrelationsanalyse der OSM-Merkmale
import matplotlib.pyplot as plt
import seaborn as sns

# Korrelationsmatrix berechnen
corr_matrix = X_scaled_df.corr()

# Visualisierung
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True, linewidths=0.5)
plt.title("Korrelationsmatrix der standardisierten OSM-Feature")
plt.tight_layout()
plt.show()
