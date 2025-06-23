# Random Forest Regressor (Vergleichsmodell)

from sklearn.ensemble import RandomForestRegressor #https://scikit-learn.org/stable/whats_new/v1.7.html
import seaborn as sns #https://seaborn.pydata.org/whatsnew/v0.13.2.html

# 1. Modellinitialisierung und Training
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 2. Vorhersage & Bewertung
y_pred_rf = rf.predict(X_test)
r2_rf = r2_score(y_test, y_pred_rf)
rmse_rf = mean_squared_error(y_test, y_pred_rf, squared=False)

print(f" Random Forest R²: {r2_rf:.3f}")
print(f" Random Forest RMSE: {rmse_rf:.2f}")

# 3. Feature Importance Plot
importances = pd.Series(rf.feature_importances_, index=X_train.columns)
importances_sorted = importances.sort_values()

plt.figure(figsize=(10, 6))
importances_sorted.plot(kind="barh", color="forestgreen")
plt.title("Wichtigkeit der OSM-Features (Random Forest)")
plt.xlabel("Feature Importance")
plt.grid(True, axis='x', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
