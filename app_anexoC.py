# Sistema de Detección de Anomalías - Simulación con Isolation Forest
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, confusion_matrix

print("Iniciando simulación...")

# Configuración
np.random.seed(42)
num_normales = 4900
num_anomalias = 100

# Tráfico normal
normal_f1 = np.random.poisson(lam=3, size=num_normales)
normal_f2 = np.random.beta(a=1, b=5, size=num_normales)
normal_f3 = np.random.choice([1, 2], p=[0.95, 0.05], size=num_normales)
normal_f4 = np.random.lognormal(mean=1.5, sigma=0.5, size=num_normales)
normal_f5 = np.random.choice([0, 1], p=[0.90, 0.10], size=num_normales)

X_normal = np.column_stack((normal_f1, normal_f2, normal_f3, normal_f4, normal_f5))

# Escenarios de ataque
ataque_f1 = np.random.randint(40, 100, size=num_anomalias)
ataque_f2 = np.random.uniform(0.8, 1.0, size=num_anomalias)
ataque_f3 = np.random.randint(3, 8, size=num_anomalias)
ataque_f4 = np.random.uniform(500, 2000, size=num_anomalias)
ataque_f5 = np.ones(num_anomalias)

X_ataque = np.column_stack((ataque_f1, ataque_f2, ataque_f3, ataque_f4, ataque_f5))

# Datos consolidados
X_raw = np.vstack((X_normal, X_ataque))
y_true = np.array([1] * num_normales + [-1] * num_anomalias)

# Normalización
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X_raw)

# Isolation Forest
clf = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
clf.fit(X_scaled)

# Predicciones
y_pred = clf.predict(X_scaled)

# Mapeo de etiquetas (0: normal, 1: anomalía)
y_true_mapped = np.where(y_true == -1, 1, 0)
y_pred_mapped = np.where(y_pred == -1, 1, 0)

print("\n--- REPORTE DE CLASIFICACIÓN ---")
print(classification_report(y_true_mapped, y_pred_mapped, target_names=["Legítimo", "Anomalía"]))

print("\nMatriz de Confusión:")
print(confusion_matrix(y_true_mapped, y_pred_mapped))
print("\nSimulación completada.")
