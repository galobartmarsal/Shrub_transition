import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from mpl_toolkits.mplot3d import Axes3D

import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

from scipy.stats import norm 
from scipy.stats import zscore

# elaboració d'un PCA amb el matollar del 87, per poder començar a interpretar aquest matollar respecte variables topogràfiques

# 1. Importem el CSV on hi ha les nostres dades

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\catalunya"))

fname_cat = os.path.join("catalunya_filtered.csv")

catalunya_filtered = pd.read_csv(fname_cat)

# 2. Seleccionem només les columnes de variables topogràfiques i climatiques

variables = catalunya_filtered[["elevation", "slope", "twi", "dist_shrub_forest_87", 
                                "avg_annual_rad","avg_ppanual_91_20", "avg_tanual_91_20",
                                  "temp_winter", "precip_summer"]]


print(variables)

# 3. Normalitzem les dades (escalar les variables)

"""El PCA busca maximizar la varianza para encontrar las direcciones (componentes principales) 
en las que los datos tienen mayor variabilidad. Las variables con valores más grandes o 
con unidades más grandes tendrán automáticamente mayor varianza, 
lo que influirá en la forma en que se calculan los componentes principales. 
Por ejemplo, si una variable está en metros y otra en grados, los valores de la primera (elevación) 
serán mucho más grandes que los de la segunda (pendiente), y el PCA podría dar mayor 
importancia a la elevación simplemente porque sus valores son mayores, 
no necesariamente porque sea más relevante. 

La estandarización consiste en convertir las variables en una escala común 
eliminando las diferencias de media y varianza. Lo más común es escalar 
cada variable para que tenga media 0 y desviación estándar 1. 
Esto garantiza que todas las variables contribuyan de manera equitativa al análisis, 
independientemente de sus escalas originales."""

scaler = StandardScaler()
variables_scaled = scaler.fit_transform(variables)

# 4. Aplicacio de PCA

pca = PCA(n_components = 9) # definició de PCA i elecció de components
X_pca = pca.fit_transform(variables_scaled) # transformar dades originals en components principals

df_pca = pd.DataFrame(data=X_pca, columns=['PC_1', 'PC_2', "PC_3", "PC_4", "PC_5", "PC_6", "PC_7", "PC_8", "PC_9"])  # transformar-ho en un dataframe per una millor visualització
 
df_pca['transicion'] = catalunya_filtered['transicion'] 

df_pca = pd.concat([df_pca, catalunya_filtered[['remained_shrub', 'shrub_to_forest', 'shrub_to_agricultural_land',
                                                'shrub_to_urbanised', 'shrub_to_meadow', 'shrub_to_sparse_veg',
                                                'shrub_to_humid_veg', 'shrub_to_otherclasses']]], axis=1)

# 4.1. Visualització de la variança explicada 

print("Varianza explicada por cada componente principal:", pca.explained_variance_ratio_)
print("Varianza total explicada:", np.sum(pca.explained_variance_ratio_))

loadings = pca.components_
print(loadings)

componentes = pd.DataFrame(pca.components_, columns=["elevation", "slope", "twi", "dist_shrub_forest_87", 
                                "avg_annual_rad","avg_ppanual_91_20", "avg_tanual_91_20",
                                  "temp_winter", "precip_summer"])

print(componentes)



# 4.2. Gràfic PCA de punts

plt.figure(figsize=(10, 8))

sns.scatterplot(x=df_pca['PC_1'], y=df_pca['PC_2'], hue=df_pca['transicion'], 
            palette="Set1", s=20)

plt.title('PCA of shrub transitions', fontsize=16)
plt.xlabel(f'Componente Principal 1 ({pca.explained_variance_ratio_[0]*100:.2f}% varianza explicada)')
plt.ylabel(f'Componente Principal 2 ({pca.explained_variance_ratio_[1]*100:.2f}% varianza explicada)')
plt.legend(title='Shrub')
plt.show()

print(f'Varianza explicada por cada componente: {pca.explained_variance_ratio_}')

"""
# Visualització de la variança explicada per cada component principal

print("Varianza explicada por cada componente principal:", pca.explained_variance_ratio_)
print("Varianza total explicada:", np.sum(pca.explained_variance_ratio_))

loadings = pca.components_
print(loadings)

componentes = pd.DataFrame(pca.components_, columns=["elevation", "slope", "twi", "dist_shrub_forest_87", 
                                "avg_annual_rad","avg_ppanual_91_20", "avg_tanual_91_20",
                                  "temp_winter", "precip_summer"])

print(componentes)

componentes.to_csv("componentes.csv", index= False)
"""
"""
# grafic de l'explicació de variança de les components principals

var_explicada = pca.explained_variance_ratio_

plt.figure(figsize=(8, 6))
plt.plot(range(1, len(var_explicada) + 1), var_explicada.cumsum(), marker='o', linestyle='--')
plt.title('Varianza acumulada explicada por los componentes principales')
plt.xlabel('Número de componentes principales')
plt.ylabel('Varianza explicada acumulada')
plt.grid(True)
plt.show()

"""









