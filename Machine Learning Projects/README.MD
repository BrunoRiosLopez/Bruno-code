# Machine Learning Projects

---
## Anti Money Laundering

### Resumen del Proyecto: Detección de Blanqueo de Dinero (AMLNet)

#### 📌 Objetivo
Desarrollar un modelo de **Machine Learning** capaz de identificar automáticamente transacciones financieras sospechosas de blanqueo de dinero en un entorno altamente desbalanceado.

---

#### 📊 Datos Clave
* **Volumen:** ~1.090.000 transacciones sintéticas.
* **Desbalance:** Solo el **0.13%** de las operaciones son sospechosas (~1.411 casos).
* **Foco:** Análisis del comportamiento de las cuentas de origen y destino a partir del histórico de transacciones.

---

#### 🛠️ Metodología
1. **Limpieza:** Eliminación de variables no representativas o que causaban *data leakage*.
2. **Ingeniería de Características:** Generación de métricas acumuladas por cuenta (frecuencias, saldos e importes máximos/promedio).
3. **División:** Selección temporal (80% entrenamiento, 20% prueba).
4. **Métrica Clave:** **PR-AUC** (Área bajo la curva Precision-Recall) para evaluar correctamente el desbalance de clases.

---

#### 🏆 Resultados y Conclusión
* **Modelo Ganador:** **XGBoost** alcanzó el mejor rendimiento con un **PR-AUC de 0.9314**, superando con creces a modelos tradicionales como Regresión Logística, SVM o Árboles de Decisión.
* **Variable Principal:** La desviación estándar y el importe máximo transaccionado por la cuenta de origen resultaron ser los indicadores con mayor poder predictivo.
