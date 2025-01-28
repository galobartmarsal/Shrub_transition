import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cambiar al directorio de trabajo
os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\catalunya"))

# Cargar los datos
fname_cat = os.path.join("catalunya_filtered.csv")
catalunya = pd.read_csv(fname_cat)

print(catalunya.columns)

# Dividir en deciles y obtener los rangos
catalunya["temp_winter_bins"], bin_edges = pd.qcut(
    catalunya["temp_winter"], q=10, retbins=True, labels=False
)

# Crear etiquetas de los rangos de los deciles
decil_ranges = pd.DataFrame({
    "Decil": range(10),
    "Etiqueta": [
        f"{bin_edges[i]:.2f} - {bin_edges[i+1]:.2f}" 
        for i in range(len(bin_edges) - 1)
    ]
})

# Calcular los porcentajes de transiciones para cada decil
resultados_temp = []

for decil in range(10):
    grupo = catalunya[catalunya["temp_winter_bins"] == decil]
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
        "Trans_Humida (%)": trans_humid_veg
    })

df_resultados_temp = pd.DataFrame(resultados_temp)

print(df_resultados_temp)

# Graficar con los rangos de los deciles en el eje X
deciles = df_resultados_temp['Decil']
trans_bosque = df_resultados_temp['Trans_Bosque (%)']
trans_prado = df_resultados_temp['Trans_Prado (%)']
trans_matorral = df_resultados_temp['Trans_Matorral (%)']
trans_cultivo = df_resultados_temp['Trans_Cultivo (%)']
trans_urbano = df_resultados_temp['Trans_Urbano (%)']
trans_otras = df_resultados_temp['Trans_Otras (%)']
trans_esparsa = df_resultados_temp['Trans_Esparsa (%)']
trans_humid = df_resultados_temp['Trans_Humida (%)']

fig, axs = plt.subplots(nrows=4, ncols=2, figsize=(12, 10))
axs = axs.flatten()

transiciones = [
    (trans_matorral, 'Shrub', 'grey'),
    (trans_bosque, 'Forest', 'green'),
    (trans_cultivo, 'Agricultural', 'orange'),
    (trans_urbano, 'Urbanised', 'brown'),
    (trans_prado, 'Meadow', 'red'),
    (trans_otras, 'Other', 'blue'),
    (trans_esparsa, 'Sparse veg.', 'pink'),
    (trans_humid, 'Humid veg.', 'purple'),
]

# Usar las etiquetas de los rangos para el eje X
etiquetas_rangos = decil_ranges["Etiqueta"]

for ax, (data, label, color) in zip(axs, transiciones):
    ax.bar(deciles, data, color=color)
    ax.set_title(label, fontsize=8)
    ax.set_xticks(deciles)
    ax.set_xticklabels(etiquetas_rangos, rotation=45, ha='right', fontsize=6)

fig.suptitle('temp_winter', fontsize=10)

fig.text(0.5, 0.04, 'Decil (Interval)', ha='center', fontsize=10)  # Título para el eje X
fig.text(0.04, 0.5, 'Transition percentage', va='center', rotation='vertical', fontsize=10)  # Título para el eje Y

plt.tight_layout(rect=[0.05, 0.05, 1, 0.95])
plt.show()
