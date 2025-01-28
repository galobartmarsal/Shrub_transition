import os

import matplotlib.pyplot as plt
import pandas as pd
import earthpy as et


# Importar base dades AP variables

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\ap"))

fname_ap = os.path.join("ap_variables.csv")

ap_variables = pd.read_csv(fname_ap)

print(ap_variables.columns)

# inspecció dels noms de columnes, canvi de noms i organizació de columnes

ap_variables = ap_variables.rename(columns={
    "fid":"fid_pixel",
    "aspect" : "aspect",
    "elevation" : "elevation",
    "Hillshade" : "hillshade",
    "slope" : "slope",
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
    "ap_shrub_transitions_variables_topo_clima_CLIMA_ATLES9120_PPTANUAL" : "avg_ppanual_91_20",
    "ap_shrub_transitions_variables_topo_clima_CLIMA_ATLES9120_TMCANUAL" : "avg_tanual_91_20",
    'ap_matollar_8722_gpkg_matollar_22_AP' : "remained_shrub_good",
    'ap_burned_gpkg_arees_cremades_87_22_suma' : "burned_areas",
    'distance_to_forest_87' : "dist_shrub_forest_87",
    'ap_variables.gpkg_CLIMA_ATLES9120_PPTESTIU' : "precip_summer",
    'ap_variables.gpkg_CLIMA_ATLES9120_TMCHIVERN' : "temp_winter"

    })

print(ap_variables.columns)

ap_variables_reindex = ap_variables.reindex(["fid_pixel", "elevation", "slope", "hillshade", "aspect", 
                                             "avg_annual_rad", "twi", "avg_ppanual_91_20", "avg_tanual_91_20",
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
                                             "remained_shrub_good"
                                            
                                             ], axis=1)


print(ap_variables_reindex.columns)

# inserció de la columna regió per saber de quina regió és cada pixel.

region = ["region"]

ap_variables_reindex[region] = "ap"

# eliminació de la columna repetida shrub

drop = ap_variables_reindex.drop(columns=["remained_shrub"])

# canvi de nom de la columna shrub que hem deixat a la taula

drop_name = drop.rename(columns = {"remained_shrub_good" : "remained_shrub"})

ap_shrub_transitions_topo_clima_variables_reindex = drop_name

print(ap_shrub_transitions_topo_clima_variables_reindex.columns)

ap_shrub_transitions_topo_clima_variables_reindex.to_csv("ap_shrub_transitions_topo_clima_variables_reindex.csv")

print("end")






