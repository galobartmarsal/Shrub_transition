import os

import matplotlib.pyplot as plt
import pandas as pd
import earthpy as et


# Importar base dades GI variables

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\gi"))

# en aquesta primera part de codi ajuntem les diferents capes de punts que he creat de girona, en una sola i la tractem per, posteriorment, obtenir el csv per ajuntar GI a tot Catalunya

fname_gi = os.path.join("gi_union.csv")

gi_variables = pd.read_csv(fname_gi)

gi_points_1 = gi_variables.dropna(subset=["Hillshade"])

gi_points_2 = gi_points_1.dropna(subset=["fid_2"])

print(gi_points_2.columns)

gi_clean = gi_points_2.drop(columns= ["fid_2", "cat", "cat_"])

print(gi_clean)

# segona part en que tractem l'anterior taula, per poder ajuntar-la amb la resta de csv i obtenir tot Catalunya

# inspecció dels noms de columnes, canvi de noms i organizació de columnes

gi_variables = gi_clean.rename(columns={
    "fid":"fid_pixel",
    "Aspect" : "aspect",
    "Elevation" : "elevation",
    "Hillshade" : "hillshade",
    "Slope" : "slope",
    "TWI" : "twi",
    "shrub87_forest22" : "shrub_to_forest",
    'avg_annual_rad' : "avg_annual_rad",
    'shrub87_agricultural22' : "shrub_to_agricultural_land",
    'shrub87_shrub22' : "remained_shrub",
    'shrub87_urbanised22' : "shrub_to_urbanised",
    'shrub87_otherclasses22' : "shrub_to_otherclasses",
    'shrub87_meadow22' : "shrub_to_meadow",
    'shrub87_sparseveg22' : "shrub_to_sparse_veg",
    'shrub87_humidveg22' : "shrub_to_humid_veg",
    'gi_clima.gpkg_CLIMA_ATLES9120_PPTANUAL' : "avg_ppanual_91_20",
    'gi_clima.gpkg_CLIMA_ATLES9120_TMCANUAL' : "avg_tanual_91_20",
    'gi_matollar_8722.gpkg_matollar_22_GI' : "remained_shrub_good",
    "gi_burned.gpkg_arees_cremades_87_22_suma" : "burned_areas",
    "dist_to_forest_87_2" : "dist_shrub_forest_87"
 
    })

print(gi_variables)


gi_variables_reindex = gi_variables.reindex(["fid_pixel", "elevation", "slope", "hillshade", "aspect", 
                                             "avg_annual_rad", "twi", "avg_ppanual_91_20", "avg_tanual_91_20",
                                             "remained_shrub", "remained_shrub_good",
                                             "shrub_to_forest",
                                             "shrub_to_agricultural_land",
                                             "shrub_to_urbanised",
                                             "shrub_to_meadow",
                                             "shrub_to_sparse_veg",
                                             "shrub_to_humid_veg",
                                             "shrub_to_otherclasses",
                                             "burned_areas",
                                             "dist_shrub_forest_87"
                                             ], axis=1)

print(gi_variables_reindex)

# inserció de la columna regió per saber de quina regió és cada pixel.

region = ["region"]

gi_variables_reindex[region] = "gi"

# eliminació de la columna repetida shrub

drop = gi_variables_reindex.drop(columns=["remained_shrub"])

# canvi de nom de la columna shrub que hem deixat a la taula

drop_name = drop.rename(columns = {"remained_shrub_good" : "remained_shrub"})

gi_shrub_transitions_topo_clima_variables_reindex = drop_name

print(gi_shrub_transitions_topo_clima_variables_reindex)

gi_shrub_transitions_topo_clima_variables_reindex.to_csv("gi_shrub_transitions_topo_clima_variables_reindex.csv")

print("the end")