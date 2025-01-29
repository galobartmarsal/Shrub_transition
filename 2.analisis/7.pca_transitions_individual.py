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

print(catalunya_filtered.columns)

"""
trans = catalunya_filtered["transicion"].unique()
print(trans)

"""

df_transition = catalunya_filtered[catalunya_filtered["transicion"] == "meadow"] # per tal de fer el pca per cada transició, hem de canviar el nom de la transicio "shrub", "meadow",...

print(df_transition["transicion"])

variables = df_transition[["elevation" , "slope", "avg_annual_rad", "twi", "avg_ppanual_91_20", "avg_tanual_91_20", "precip_summer", "temp_winter", "dist_shrub_forest_87"]] # seleccionem variables

print(variables)

# estandaritzacio de dades

scaler = StandardScaler()
x_scaled = scaler.fit_transform(variables)

# Aplicar PCA

pca = PCA(n_components = 3)
variables_pca = pca.fit_transform(x_scaled)

# convertir a dataframe per graficar

df_pca = pd.DataFrame(variables_pca, columns=["PC1", "PC2", "PC3"])
df_pca_transition = df_transition["transicion"]


print(df_pca_transition.unique())
print(df_pca_transition.value_counts())


#explicació varianza

print("variança explicada per cada component", pca.explained_variance_ratio_)
print("variança total explicada", sum(pca.explained_variance_ratio_))

# loadings; pesos de cada variable en cada component

loadings = pd.DataFrame(pca.components_.T, 
                        index =["elevation", "slope", "twi", "dist_shrub_forest_87", 
                                "avg_annual_rad","avg_ppanual_91_20", "avg_tanual_91_20",
                                  "temp_winter", "precip_summer"],
                          columns=["PC1", "PC2", "PC3"])

print(loadings)


# visualització grafic

plt.figure(figsize=(8,6))
sns.scatterplot(data=df_pca, x="PC1", y="PC2")
plt.title("PCA shrub to meadow 87-22")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.show()

