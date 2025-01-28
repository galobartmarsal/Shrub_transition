import os

import matplotlib.pyplot as plt
import pandas as pd
import earthpy as et


# Importar base dades BCN variables

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\bcn"))

fname_bcn = os.path.join("bcn_variables.csv")

bcn_variables = pd.read_csv(fname_bcn)

print(bcn_variables.columns)

# inspecció dels noms de columnes, canvi de noms i organizació de columnes

bcn_variables = bcn_variables.rename(columns={
    "fid":"fid_pixel",
    "Aspect" : "aspect",
    "Elevation" : "elevation",
    "Hillshade" : "hillshade",
    "Slope" : "slope",
    "TWI" : "twi",
    "shrub87_forest22" : "shrub_to_forest",
    "avg_annual_rad" : "avg_annual_rad",
    "shrub87_agricultural22" : "shrub_to_agricultural_land",
    "shrub87_shrub22" : "remained_shrub",
    "shrub87_urbanised22" : "shrub_to_urbanised",
    "shrub87_otherclasses22" : "shrub_to_otherclasses",
    "shrub87_meadow22" : "shrub_to_meadow",
    "shrub87_sparseveg22" : "shrub_to_sparse_veg",
    "shrub87_humidveg22" : "shrub_to_humid_veg",
    'bcn_clima.gpkg_CLIMA_ATLES9120_PPTANUAL' : "avg_ppanual_91_20",
    'bcn_clima.gpkg_CLIMA_ATLES9120_TMCANUAL' : "avg_tanual_91_20",
    'bcn_matollar_8722.gpkg_matollar_22_BCN' : "remained_shrub_good",
    "bcn_burned.gpkg_arees_cremades_87_22_suma" : "burned_areas",
    'distance_to_forest_87' : "distance_remove",
    'Merged_distance_to_forest_87' : "dist_shrub_forest_87",
    'bcn_variables_estiu_hivern.gpkg_CLIMA_ATLES9120_PPTESTIU' : "precip_summer",
    'bcn_variables_estiu_hivern.gpkg_CLIMA_ATLES9120_TMCHIVERN' : "temp_winter"

    })

print(bcn_variables.columns)

bcn_variables_reindex = bcn_variables.reindex(["fid_pixel", "elevation", "slope", "hillshade", "aspect", 
                                             "avg_annual_rad", "twi", "avg_ppanual_91_20", "avg_tanual_91_20",
                                             "precip_summer" , "temp_winter",
                                             "remained_shrub", "remained_shrub_good",
                                             "shrub_to_forest",
                                             "shrub_to_agricultural_land",
                                             "shrub_to_urbanised",
                                             "shrub_to_meadow",
                                             "shrub_to_sparse_veg",
                                             "shrub_to_humid_veg",
                                             "shrub_to_otherclasses",
                                             "burned_areas",
                                             "distance_remove",
                                             "dist_shrub_forest_87"
                                             ], axis=1)


print(bcn_variables_reindex.columns)

# inserció de la columna regió per saber de quina regió és cada pixel.

region = ["region"]

bcn_variables_reindex[region] = "bcn"

# eliminació de la columna repetida shrub

drop = bcn_variables_reindex.drop(columns=["remained_shrub", "distance_remove"])

# canvi de nom de la columna shrub que hem deixat a la taula

drop_name = drop.rename(columns = {"remained_shrub_good" : "remained_shrub"})

bcn_shrub_transitions_topo_clima_variables_reindex = drop_name

print(bcn_shrub_transitions_topo_clima_variables_reindex)

bcn_shrub_transitions_topo_clima_variables_reindex.to_csv("bcn_shrub_transitions_topo_clima_variables_reindex.csv")

print("end")
