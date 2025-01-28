import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import earthpy as et
import seaborn as sns
from scipy.stats import norm 

# En aquest codi el que es fa és ajuntar totes les vegueries processades anteriorment, en una única taula per obtenir Catalunya.

# 1. Importem cada csv elaborat amb QGIS de les diferents vegueries, per tal d'ajuntar-les en un unic CSV per tenir tot Catalunya.
# 1.1 importar ap 

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\ap"))

fname_ap = os.path.join("ap_shrub_transitions_topo_clima_variables_reindex.csv")

ap = pd.read_csv(fname_ap)

# 1.2 importar bcn

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\bcn"))

fname_bcn = os.path.join("bcn_shrub_transitions_topo_clima_variables_reindex.csv")

bcn = pd.read_csv(fname_bcn)

# 1.3 importar cc

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\cc"))

fname_cc = os.path.join("cc_shrub_transitions_topo_clima_variables_reindex.csv")

cc = pd.read_csv(fname_cc)

# 1.4 importar gi

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\gi"))

fname_gi = os.path.join("gi_shrub_transitions_topo_clima_variables_reindex.csv")

gi = pd.read_csv(fname_gi)

# 1.5 importar ll

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\ll"))

fname_ll = os.path.join("ll_shrub_transitions_topo_clima_variables_reindex.csv")

ll = pd.read_csv(fname_ll)

# 1.6 importar pe

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\pe"))

fname_pe = os.path.join("pe_shrub_transitions_topo_clima_variables_reindex.csv")

pe = pd.read_csv(fname_pe)

# 1.7 importar te

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\te"))

fname_te = os.path.join("te_shrub_transitions_topo_clima_variables_reindex.csv")

te = pd.read_csv(fname_te)

# 1.8 importar tgn

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\tgn"))

fname_tgn = os.path.join("tgn_shrub_transitions_topo_clima_variables_reindex.csv")

tgn = pd.read_csv(fname_tgn)

# 1.9 importar va

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\va"))

fname_va = os.path.join("va_shrub_transitions_topo_clima_variables_reindex.csv")

va = pd.read_csv(fname_va)

print(ap.columns)
print(bcn.columns)
print(cc.columns)
print(gi.columns)
print(ll.columns)
print(pe.columns)
print(te.columns)
print(tgn.columns) 
print(va.columns)


# 2. Ajuntem tots els CSV de les diferents vegueries

vegueries = [ap,bcn,cc,gi,ll,pe,te,tgn,va] # llista dels diferents dataframes

catalunya = pd.concat(vegueries, ignore_index=True) # unim els dataframes.

catalunya["ID"] = catalunya.index + 1 # creem una nova columna que fara d'identificador de cada pixel (tot i que els CSV ja en tenien, es repetien numeros). "+1" pq comenci des de 1 i no des de 0

catalunya =catalunya.drop("Unnamed: 0", axis=1) # eliminació d'una columna que hi havia i que no servia de res

print(catalunya.columns)

# 2.1 reorganització de columnes

catalunya = catalunya.reindex(["ID", "fid_pixel", "elevation", "slope", "hillshade", "aspect", 
                                             "avg_annual_rad", "twi", "avg_ppanual_91_20" , "avg_tanual_91_20",
                                             "precip_summer", "temp_winter",
                                             "dist_shrub_forest_87",
                                             "remained_shrub",
                                             "shrub_to_forest",
                                             "shrub_to_agricultural_land",
                                             "shrub_to_urbanised",
                                             "shrub_to_meadow",
                                             "shrub_to_sparse_veg",
                                             "shrub_to_humid_veg",
                                             "shrub_to_otherclasses",
                                             "burned_areas",
                                             "region"
                                             ], axis=1)
                                             

print(catalunya)

catalunya.to_csv("catalunya.csv", index=False) # guardar el csv de tot Catalunya, cru, sense tractar.

# 3. Primera neteja de les dades del CSV de tot Catalunya

# 3.1. canviem els valors negatius de la columna elevation a 0. ja que aquests són valors a nivell del mar o sota el mar
catalunya["elevation"] = catalunya["elevation"].apply(lambda x: 0 if x < 0 else x) 

# 3.2. eliminacio d'aquesta variable, ja que no aporta res
catalunya = catalunya.drop("hillshade", axis=1) 

# 3.3. aquesta funció crea una condicio boleana que selecciona només les files, on els valors de twi són 0 o positius.
catalunya_1 = catalunya[catalunya["twi"] >= 0] 

# 3.4. eliminació de files on hi ha cel·les buides (NaNa), a partir de la funció .dropna()
catalunya_filtered_1 = catalunya_1.dropna() 

# 3.5. filtrem i ens quedem només les files on no hi ha hagut arees creamedes entre el 1987 i 2022. D'aquesta manera sabem que la classe final del 2022 és exclusiva de matollar 1987
catalunya_filtered = catalunya_filtered_1.query("burned_areas !=1")

print(catalunya_filtered)

# 4. Creem una funció per què ens retorni el nom de cada transició (aquesta funcio fa que allà on hi hagi un 1 en cada columna de transició, li dongui el nom de la transició)

def categorize_transition(row):           
    if row['remained_shrub'] == 1:
        return 'shrub'
    elif row['shrub_to_forest'] == 1:
        return 'forest'
    elif row['shrub_to_agricultural_land'] == 1:
        return 'agriculture'
    elif row['shrub_to_urbanised'] == 1:
        return 'urban'
    elif row['shrub_to_meadow'] == 1:
        return 'meadow'
    elif row['shrub_to_sparse_veg'] == 1:
        return 'sparse'
    elif row['shrub_to_humid_veg'] == 1:
        return 'humid'
    elif row['shrub_to_otherclasses'] == 1:
        return 'other'
    else:
        return 'Ninguna'  
    

# 4.1. creació de columna nova amb el nom de cada transicio de cada pixel

catalunya_filtered['transicion'] = catalunya_filtered.apply(categorize_transition, axis=1) 

catalunya_filtered = catalunya_filtered.drop("burned_areas", axis=1) # eliminació de la columna burned areas, ja que no fa servei

print(catalunya_filtered)

catalunya_filtered = catalunya_filtered[catalunya_filtered["transicion"] != "Ninguna"] # les caselles que queden amb Ninguna, són pixels que no han patit cap transició (o al menys no ho sabem), ja que la capa de MUSC22 del CREAF no conte dades en aquests llocs (hi ha zones que no estan descrites, veure exemple amb els pixels que tenen Ninguna)

# 5. taula final de tot catalunya amb tots els pixels i cada variable

catalunya_filtered.to_csv("catalunya_filtered.csv", index=False) # aquesta és la primera taula netejada i per fer servir.

cat_trans = catalunya_filtered[["fid_pixel","transicion","region"]] # també he elaborat una taula on s'indica només cada pixel, quin canvi de classe ha fet i a quina regió pertany

cat_trans.to_csv("cat_trans.csv", index=False) # taula on nomes indica la transició i la regió de cada pixel

print("end")



    














