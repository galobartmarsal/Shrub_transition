import os

import matplotlib.pyplot as plt
import pandas as pd
import earthpy as et


# Importar base dades CC variables

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\cc"))

fname_cc = os.path.join("cc_variables.csv")

cc_variables = pd.read_csv(fname_cc)

print(cc_variables.columns)

# inspecció dels noms de columnes, canvi de noms i organizació de columnes

cc_variables = cc_variables.rename(columns={
    "fid":"fid_pixel",
    "Aspect" : "aspect",
    "Elevation" : "elevation",
    "Hillshade" : "hillshade",
    "Slope" : "slope",
    "TWI" : "twi",
    'shrub87_forest22' : "shrub_to_forest",
    'avg_annual_rad' : "avg_annual_rad",
    'shrub87_agricultural22' : "shrub_to_agricultural_land",
    'shrub87_shrub22' : "remained_shrub",
    'shrub87_urbanised22' : "shrub_to_urbanised",
    'shrub87_otherclasses22' : "shrub_to_otherclasses",
    'shrub87_meadow22' : "shrub_to_meadow",
    'shrub87_sparseveg22' : "shrub_to_sparse_veg",
    'shrub87_humidveg22' : "shrub_to_humid_veg",
    'cc_clima.gpkg_CLIMA_ATLES9120_PPTANUAL' : "avg_ppanual_91_20",
    'cc_clima.gpkg_CLIMA_ATLES9120_TMCANUAL' : "avg_tanual_91_20",
    'cc_matollar_8722.gpkg_matollar_22_CC' : "remained_shrub_good",
    "cc_burned.gpkg_arees_cremades_87_22_suma" : "burned_areas",
    "dist_to_forest_87_2" : "dist_shrub_forest_87",
    'cc_variables_estiu_hivern.gpkg_CLIMA_ATLES9120_PPTESTIU' : "precip_summer",
    'cc_variables_estiu_hivern.gpkg_CLIMA_ATLES9120_TMCHIVERN' : "temp_winter"
    })

print(cc_variables.columns)

cc_variables_reindex = cc_variables.reindex(["fid_pixel", "elevation", "slope", "hillshade", "aspect", 
                                             "avg_annual_rad", "twi", "avg_ppanual_91_20", "avg_tanual_91_20",
                                             "precip_summer", "temp_winter",
                                             "remained_shrub", "remained_shrub_good",
                                             "dist_shrub_forest_87",
                                             "shrub_to_forest",
                                             "shrub_to_agricultural_land",
                                             "shrub_to_urbanised",
                                             "shrub_to_meadow",
                                             "shrub_to_sparse_veg",
                                             "shrub_to_humid_veg",
                                             "shrub_to_otherclasses",
                                             "burned_areas",
                                             
                                             ], axis=1)


print(cc_variables_reindex)

# inserció de la columna regió per saber de quina regió és cada pixel.

region = ["region"]

cc_variables_reindex[region] = "cc"

# eliminació de la columna repetida shrub

drop = cc_variables_reindex.drop(columns=["remained_shrub"])

# canvi de nom de la columna shrub que hem deixat a la taula

drop_name = drop.rename(columns = {"remained_shrub_good" : "remained_shrub"})

cc_shrub_transitions_topo_clima_variables_reindex = drop_name

print(cc_shrub_transitions_topo_clima_variables_reindex.columns)

cc_shrub_transitions_topo_clima_variables_reindex.to_csv("cc_shrub_transitions_topo_clima_variables_reindex.csv")

print("end")
