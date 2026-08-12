# Sistema de Detección de Anomalías - ITLA

## Información del Proyecto

- **Institución**: Instituto Tecnológico de las Américas (ITLA)
- **Centro**: Centro de Excelencia de Seguridad Informática
- **Título**: Propuesta Metodológica de un Sistema de Detección de Anomalías
- **Autores**: Steven Mendez, Keirys Familia, Yojhairy Zapata
- **Asesor**: Nelson Mieses
- **Algoritmo**: Isolation Forest (Machine Learning No Supervisado)

## Descripción

Script de simulación de referencia que valida conceptualmente la viabilidad matemática del aislamiento de anomalías sobre el vector de entrada:

```
Xi = [F1, F2, F3, F4, F5]
```

Procesamiento en ventanas temporales de 5 minutos.

## Variables

- **F1**: Frecuencia de autenticaciones
- **F2**: Ratio de fallas
- **F3**: Diversidad de IPs
- **F4**: Volumen de datos (MB)
- **F5**: Patrón horario anómalo

## Datos Sintéticos

- **Tráfico Legítimo**: 4,900 muestras
- **Anomalías Inyectadas**: 100 muestras (contaminación 2.0%)

### Escenarios de Ataque
1. Fuerza Bruta
2. Exfiltración
3. Escalada de Privilegios

## Requisitos

### Software
- **Python**: 3.8 o superior
- **pip**: Gestor de paquetes de Python

### Dependencias

| Paquete | Versión Mínima | Descripción |
|---------|---|---|
| numpy | 1.19.0 | Computación numérica |
| pandas | 1.1.0 | Análisis de datos |
| scikit-learn | 0.24.0 | Machine Learning |

### Instalación

1. **Clonar o descargar el repositorio:**
```bash
git clone <https://github.com/girl54897>
cd yoj
```

2. **Crear un entorno virtual (recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

O instalar manualmente:
```bash
pip install numpy>=1.19.0 pandas>=1.1.0 scikit-learn>=0.24.0
```

## Uso

```bash
python app_anexoC.py
```

## Pasos de Ejecución

El script ejecuta los siguientes pasos automáticamente:

### 1. Generación de Datos Sintéticos - Tráfico Normal
- **F1**: Frecuencia de autenticaciones (Distribución Poisson, λ=3)
- **F2**: Ratio de fallas (Distribución Beta, a=1, b=5)
- **F3**: Diversidad de IPs (Acceso desde 1-2 direcciones IP)
- **F4**: Volumen de datos (Distribución Lognormal, μ=1.5, σ=0.5)
- **F5**: Patrón horario (90% regular, 10% anomalía)
- **Cantidad**: 4,900 muestras

### 2. Generación de Escenarios de Ataque
- **F1**: Frecuencia extrema (40-100 intentos)
- **F2**: Ratio de fallas crítico (0.8-1.0)
- **F3**: Múltiples IPs (3-8 direcciones)
- **F4**: Volumen de datos extremo (500-2000 MB)
- **F5**: Evento asíncrono permanente
- **Cantidad**: 100 muestras (2% contaminación)

### 3. Consolidación de Datos
- Combina datos normales + datos de ataque
- Genera etiquetas de verdad (1: normal, -1: anomalía)

### 4. Normalización
- Aplica **MinMaxScaler** para escalar los datos a [0, 1]
- Mejora el desempeño del algoritmo

### 5. Entrenamiento del Modelo
- **Algoritmo**: Isolation Forest
- **Parámetros**:
  - `n_estimators`: 100 árboles
  - `contamination`: 0.02 (2% esperado)
  - `random_state`: 42 (reproducibilidad)

### 6. Predicciones
- El modelo predice qué muestras son anomalías
- Mapea predicciones a formato estándar (0: legítimo, 1: anomalía)

### 7. Evaluación
- Genera **Reporte de Clasificación** con:
  - Precisión (Precision)
  - Recall (Sensibilidad)
  - F1-Score
  - Soporte (número de muestras)
- Produce **Matriz de Confusión** para análisis detallado

## Salida

El script genera:
- Reporte de clasificación (Precisión, Recall, F1-Score)
- Matriz de confusión
- Evaluación del modelo Isolation Forest

## Métricas Utilizadas

- **True Positive (TP)**: Anomalías detectadas correctamente
- **False Positive (FP)**: Falsos positivos
- **True Negative (TN)**: Tráfico legítimo identificado correctamente
- **False Negative (FN)**: Anomalías no detectadas
