# Lineare Regression + Einflussvisualisierung

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Keine Filterung mehr notwendig – df_merged enthält bereits nur PM2.5
df_model = df_merged.copy()

# 2. Feature-Auswahl: nur numerische OSM-Features mit Radiusbezug
feature_cols = [col for col in df_model.columns if any(suffix in col for suffix in ["_100m", "_250m", "_500m"]) and pd.api.types.is_numeric_dtype(df_model[col])]

# 3. Ziel- und Eingabematrix
y = df_model["Tagesmittel"]
X = df_model[feature_cols].copy()
X = X.apply(pd.to_numeric, errors="coerce").fillna(0)

# 4. Standardisierung
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled_df = pd.DataFrame(X_scaled, columns=feature_cols)

# 5. Training/Test-Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled_df, y, test_size=0.2, random_state=42)

# 6. Modelltraining
model = LinearRegression()
model.fit(X_train, y_train)

# 7. Vorhersage & Bewertung
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)

print(f"R²: {r2:.3f}")
print(f"RMSE: {rmse:.2f}")

# 8. Einflussvisualisierung
coeffs = pd.Series(model.coef_, index=X_train.columns)
coeffs_sorted = coeffs.sort_values()

plt.figure(figsize=(10, 6))
coeffs_sorted.plot(kind="barh")
plt.title("Einfluss der OSM-Features auf PM2.5 (Lineares Modell, standardisiert)")
plt.xlabel("Standardisierter Regressionskoeffizient")
plt.axvline(x=0, linestyle="--", alpha=0.3, color="black")
plt.grid(axis='x', linestyle=":", alpha=0.5)
plt.tight_layout()
plt.show()
