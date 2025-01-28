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

# dividim en decils la variable elevació per tal de veure quins % de transicions hi ha en cada decil

catalunya["slope"] = pd.qcut(catalunya["slope"], q=10, labels=False)

resultados_temp = [] 

for decil in range(10):
    grupo = catalunya[catalunya["slope"] == decil]
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
trans_esparsa =df_resultados_temp["Trans_Esparsa (%)"]
trans_humida =df_resultados_temp["Trans_humida (%)"]

# 1. GRÀFIC BARRES APILADES: PERCENTATGE DE CADA TRANSICIÓ QUE HA FET EL MATOLLAR DEL 87, DIVIDIT EN 10 DECILS I PER VARIABLE

plt.figure(figsize=(10, 6))
plt.bar(deciles, trans_matorral, label='Shrub', color='grey')
plt.bar(deciles, trans_bosque, bottom=trans_matorral, label='Forest', color='green')
plt.bar(deciles, trans_cultivo, bottom=trans_matorral + trans_bosque, label='Agricultural land', color='orange')
plt.bar(deciles, trans_urbano, bottom=trans_matorral + trans_bosque + trans_cultivo, label='Urbanised land', color='brown')
plt.bar(deciles, trans_prado, bottom=trans_matorral + trans_bosque + trans_cultivo + trans_urbano, label='Meadow', color='red')
plt.bar(deciles, trans_otras, bottom=trans_matorral + trans_bosque + trans_cultivo + trans_urbano + trans_prado, label='Other', color='blue')
plt.bar(deciles, trans_esparsa, bottom=trans_matorral + trans_bosque + trans_cultivo + trans_urbano + trans_prado + trans_otras, label='Sparse veg.', color='pink')
plt.bar(deciles, trans_humida, bottom=trans_matorral + trans_bosque + trans_cultivo + trans_urbano + trans_prado + trans_otras + trans_esparsa, label='Humid veg.', color='purple')


plt.title("slope")
plt.xlabel('Decil')
plt.ylabel('Transition percentage')
plt.xticks(deciles)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Shrub 1987 transition to:')

plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.show()






