
import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import earthpy as et
import seaborn as sns
from scipy.stats import norm 

# En aquest codi el que es fa es generar els gràfics en decils de les variables. 
# En decils vol dir que, el total de punts de matollar del 87 s'ha dividit en 10 decils, i de cada decil es mira quina quantitat de punts de matollar del 87 a passat a cada transició.
# Hi ha un gràfic de decils per cada variable.

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\catalunya"))

fname_cat = os.path.join("catalunya_filtered.csv")

catalunya = pd.read_csv(fname_cat)

print(catalunya.columns)
"""
# dividim en decils la variable elevació per tal de veure quins % de transicions hi ha en cada decil

ruido_min = -0.00001
ruido_max = 0.00001

catalunya["dist_shrub_forest_87"] = catalunya["dist_shrub_forest_87"] + np.random.uniform(ruido_min, ruido_max, size=len(catalunya))
catalunya["dist_shrub_forest_87"] = pd.qcut(catalunya["dist_shrub_forest_87"], q=10, labels=False)


#catalunya["dist_shrub_forest_87"] = pd.qcut(catalunya["dist_shrub_forest_87"], q=10, labels=False)

resultados_temp = [] 

for decil in range(10):
    grupo = catalunya[catalunya["dist_shrub_forest_87"] == decil]
    total_grupo = len(grupo)
    
    trans_bosque = grupo['shrub_to_forest'].sum() / total_grupo * 100
    trans_prado = grupo['shrub_to_meadow'].sum() / total_grupo * 100
    trans_matorral = grupo['remained_shrub'].sum() / total_grupo * 100
    trans_cultivo = grupo['shrub_to_agricultural_land'].sum() / total_grupo * 100
    trans_urbano = grupo['shrub_to_urbanised'].sum() / total_grupo * 100
    trans_otras = grupo['shrub_to_otherclasses'].sum() / total_grupo * 100
    trans_esparsa_veg = grupo['shrub_to_sparse_veg'].sum() / total_grupo * 100
    trans_humi_veg = grupo['shrub_to_humid_veg'].sum() / total_grupo * 100
    
    resultados_temp.append({
        'Decil': decil,
        'Trans_Bosque (%)': trans_bosque,
        'Trans_Prado (%)': trans_prado,
        'Trans_Matorral (%)': trans_matorral,
        'Trans_Cultivo (%)': trans_cultivo,
        'Trans_Urbano (%)': trans_urbano,
        'Trans_Otras (%)': trans_otras,
        "Trans_Esparsa (%)" : trans_esparsa_veg,
        "Trans_humida (%)" : trans_humi_veg
    })

df_resultados_temp = pd.DataFrame(resultados_temp)

print(df_resultados_temp)

#df_resultados_temp.to_csv("df_resultados_temp.csv")

#grafic

df_melt = pd.melt(df_resultados_temp, id_vars='Decil', 
                  value_vars=['Trans_Bosque (%)', 'Trans_Prado (%)', 'Trans_Matorral (%)', 
                              'Trans_Cultivo (%)', 'Trans_Urbano (%)', 'Trans_Otras (%)', "Trans_Esparsa (%)", "Trans_humida (%)"], 
                  var_name='Transicion', value_name='Porcentaje')

deciles = df_resultados_temp['Decil']
trans_bosque = df_resultados_temp['Trans_Bosque (%)']
trans_prado = df_resultados_temp['Trans_Prado (%)']
trans_matorral = df_resultados_temp['Trans_Matorral (%)']
trans_cultivo = df_resultados_temp['Trans_Cultivo (%)']
trans_urbano = df_resultados_temp['Trans_Urbano (%)']
trans_otras = df_resultados_temp['Trans_Otras (%)']
trans_esparsa = df_resultados_temp['Trans_Esparsa (%)']
trans_humid = df_resultados_temp['Trans_humida (%)']


# 2. GRÀFIC COM L'ANTERIOR, PERÒ EN COMPTES DE BARRES APILADES, ÉS INDIVIDUAL DE CADA TRANSICIÓ

fig, axs = plt.subplots(nrows=4, ncols=2, figsize=(8, 8))
axs = axs.flatten()

transiciones = [
    (trans_matorral, 'Shrub', 'grey'),
    (trans_bosque, 'Forest', 'green'),
    (trans_cultivo, 'Agricultural', 'orange'),
    (trans_urbano, 'Urbanised', 'brown'),
    (trans_prado, 'Meadow', 'red'),
    (trans_otras, 'Other', 'blue'),
    (trans_esparsa, 'Trans esparsa', 'pink'),
    (trans_humid, 'Trans humid', 'purple'),]


for ax, (data, label, color) in zip(axs, transiciones):
    ax.bar(deciles, data, color=color)
    ax.set_title(label, fontsize = 8)
    ax.set_xticks(deciles)

fig.suptitle('dist_shrub_forest_87', fontsize=12)

fig.text(0.5, 0.04, 'Decil', ha='center', fontsize=10)  # Título para el eje X
fig.text(0.04, 0.5, 'Percentage of transitions', va='center', rotation='vertical', fontsize=10)  # Título para el eje Y


plt.tight_layout(rect=[0.05, 0.05, 1, 0.95])
plt.show()

"""
# grafic decils amb intervals

# dividim en decils la variable elevació per tal de veure quins % de transicions hi ha en cada decil

ruido_min = -0.00001
ruido_max = 0.00001
catalunya["dist_shrub_forest_87"] = catalunya["dist_shrub_forest_87"] + np.random.uniform(ruido_min, ruido_max, size=len(catalunya))
catalunya["dist_shrub_forest_87"], bins = pd.qcut(catalunya["dist_shrub_forest_87"], q=10, labels=False, retbins=True)

# Crear DataFrame con rangos de deciles
decil_ranges = pd.DataFrame({
    "Decil": range(10),
    "Min": bins[:-1],
    "Max": bins[1:],
    "Etiqueta": [f"{round(bins[i], 2)} - {round(bins[i+1], 2)}" for i in range(len(bins) - 1)]
})

# Calcular resultados para cada decil
resultados_temp = []
for decil in range(10):
    grupo = catalunya[catalunya["dist_shrub_forest_87"] == decil]
    total_grupo = len(grupo)

    trans_bosque = grupo['shrub_to_forest'].sum() / total_grupo * 100
    trans_prado = grupo['shrub_to_meadow'].sum() / total_grupo * 100
    trans_matorral = grupo['remained_shrub'].sum() / total_grupo * 100
    trans_cultivo = grupo['shrub_to_agricultural_land'].sum() / total_grupo * 100
    trans_urbano = grupo['shrub_to_urbanised'].sum() / total_grupo * 100
    trans_otras = grupo['shrub_to_otherclasses'].sum() / total_grupo * 100
    trans_esparsa_veg = grupo['shrub_to_sparse_veg'].sum() / total_grupo * 100
    trans_humid_veg = grupo['shrub_to_humid_veg'].sum() / total_grupo * 100

    resultados_temp.append({
        'Decil': decil,
        'Trans_Bosque (%)': trans_bosque,
        'Trans_Prado (%)': trans_prado,
        'Trans_Matorral (%)': trans_matorral,
        'Trans_Cultivo (%)': trans_cultivo,
        'Trans_Urbano (%)': trans_urbano,
        'Trans_Otras (%)': trans_otras,
        "Trans_Esparsa (%)": trans_esparsa_veg,
        "Trans_humida (%)": trans_humid_veg
    })

df_resultados_temp = pd.DataFrame(resultados_temp)

# Graficar transiciones
fig, axs = plt.subplots(nrows=4, ncols=2, figsize=(12, 10))  # Tamaño más grande
axs = axs.flatten()

transiciones = [
    (df_resultados_temp['Trans_Matorral (%)'], 'Shrub', 'grey'),
    (df_resultados_temp['Trans_Bosque (%)'], 'Forest', 'green'),
    (df_resultados_temp['Trans_Cultivo (%)'], 'Agricultural', 'orange'),
    (df_resultados_temp['Trans_Urbano (%)'], 'Urbanised', 'brown'),
    (df_resultados_temp['Trans_Prado (%)'], 'Meadow', 'red'),
    (df_resultados_temp['Trans_Otras (%)'], 'Other', 'blue'),
    (df_resultados_temp['Trans_Esparsa (%)'], 'Trans esparsa', 'pink'),
    (df_resultados_temp['Trans_humida (%)'], 'Trans humid', 'purple')
]

etiquetas_rangos = decil_ranges["Etiqueta"]

for ax, (data, label, color) in zip(axs, transiciones):
    ax.bar(df_resultados_temp['Decil'], data, color=color)
    ax.set_title(label, fontsize=8)
    ax.set_xticks(df_resultados_temp['Decil'])
    ax.set_xticklabels(etiquetas_rangos, rotation=45, ha='right', fontsize=6)

fig.suptitle('dist_shrub_forest_87', fontsize=10)
fig.text(0.5, 0.04, 'Decil (Rangos)', ha='center', fontsize=10)
fig.text(0.04, 0.5, 'Percentage of transitions', va='center', rotation='vertical', fontsize=10)

plt.tight_layout(rect=[0.05, 0.05, 1, 0.95])
plt.show()