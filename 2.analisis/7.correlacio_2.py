import os
 
import numpy as np
import seaborn as sns
import pandas as pd
from scipy.stats import shapiro, normaltest, probplot
import matplotlib.pyplot as plt
from plotnine import ggplot, aes, geom_histogram, geom_qq, ggtitle, theme_minimal
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

from scipy.stats import norm 
from scipy.stats import zscore

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\catalunya"))

fname_cat = os.path.join("catalunya_filtered.csv")

catalunya = pd.read_csv(fname_cat)

print(catalunya.head())

variables_explicatives = catalunya[["slope", "elevation", "twi", "temp_winter", "precip_summer",
                     "avg_annual_rad", "avg_ppanual_91_20", "avg_tanual_91_20", "dist_shrub_forest_87"]]


"""
# com que hi ha una mostra molt gran (> 8.000.000 pixels), podem fer un resampling de la mostra
sample_size = 10000

sample = variables_explicatives.sample(n=sample_size, random_state=42)
"""

sample = variables_explicatives

normality_results = {}

for column in variables_explicatives.columns:  # Excluyendo la columna identificadora
 # Test de normalidad usando D'Agostino y Pearson If the data contains repeated values we recommend using the D'Agostino-Pearson test.
    stat, p_value = normaltest(sample[column])
    normality_results[column] = {'stat': stat, 'p_value': p_value}

    # Visualización: Histogramas y gráficos QQ
    plt.figure(figsize=(12, 5))

    # QQ Plot
    plt.subplot(1, 2, 2)
    probplot(sample[column], dist="norm", plot=plt)
    plt.title(f"QQ Plot of {column}")

    plt.tight_layout()
    plt.show()

# Mostrar resultados del test de normalidad
print("\nResultados del test de normalidad:")
for column, result in normality_results.items():
    print(f"Variable: {column}, Statistic: {result['stat']:.4f}, P-value: {result['p_value']:.4g}")
    if result['p_value'] < 0.05:
        print(f" -> La variable {column} NO sigue una distribución normal (p < 0.05)")
    else:
        print(f" -> La variable {column} sigue una distribución normal (p >= 0.05)")

# Paso 2: Correlación entre variables predictivas
# Calculamos las matrices de correlación con Spearman y Kendall
spearman_corr = sample.corr(method="spearman")  # Excluir identificador
kendall_corr = sample.corr(method="kendall")

print(kendall_corr)

# Visualizamos las matrices de correlación con mapas de calor
plt.figure(figsize=(10, 8))
sns.heatmap(spearman_corr, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Matriz de correlación (Spearman) entre variables predictivas")
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(kendall_corr, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("Matriz de correlación (Kendall) entre variables predictivas")
plt.show()


# Paso 3: Calcular el VIF para detectar colinealidad
# Excluimos la columna identificadora para calcular el VIF
X = sample.values  # Variables predictivas sin el identificador
vif_data = pd.DataFrame()
vif_data["Variable"] = sample.columns
vif_data["VIF"] = [variance_inflation_factor(X, i) for i in range(X.shape[1])]

print("\nValores del VIF (Variance Inflation Factor):")
print(vif_data)

variables_explicatives = catalunya[["slope", "elevation", "twi", "precip_summer", "temp_winter",
                       "dist_shrub_forest_87"]]

sample_size = 10000

sample = variables_explicatives.sample(n=sample_size, random_state=42)

X = sample # Variables predictivas sin el identificador
vif_data = pd.DataFrame()
vif_data["Variable"] = sample.columns
vif_data["VIF"] = [variance_inflation_factor(X, i) for i in range(X.shape[1])]

print("\nValores del VIF (Variance Inflation Factor):")
print(vif_data)
