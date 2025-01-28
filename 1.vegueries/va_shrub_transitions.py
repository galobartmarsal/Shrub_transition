import os

import matplotlib.pyplot as plt
import pandas as pd
import earthpy as et


# Importar base dades VA variables

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\va"))

fname_va = os.path.join("va_variables.csv")

va_variables = pd.read_csv(fname_va)

print(va_variables.columns)

# inspecció dels noms de columnes, canvi de noms i organizació de columnes

va_variables = va_variables.rename(columns={
    "fid":"fid_pixel",
    "aspect_points.gpkg_Aspect" : "aspect",
    "elevation_points.gpkg_DME_15X15" : "elevation",
    "Hillshade" : "hillshade",
    "slope_points.gpkg_Slope" : "slope",
    "twi_points.gpkg_TWI_VA" : "twi",
    "forest_transition_points.gpkg_va_mat87_bosc22_noburned" : "shrub_to_forest",
    "va_rad.gpkg_Cat_rad_anual_averg" : "avg_annual_rad",
    "va_shrub_transitions_points.gpkg_agricultured_shrub_8722" : "shrub_to_agricultural_land",
    "va_shrub_transitions_points.gpkg_va_matollar_87n22_noburned" : "remained_shrub",
    "va_shrub_transitions_points.gpkg_urbanised_shrub_8722" : "shrub_to_urbanised",
    "va_shrub_transitions_points.gpkg_shrub_to_other_classes_8722" : "shrub_to_otherclasses",
    "va_shrub_transitions_points.gpkg_shrub87andmeadow22_2" : "shrub_to_meadow",
    "va_shrub_transitions_points.gpkg_sparse_vegetation_22" : "shrub_to_sparse_veg",
    "va_shrub_transitions_points.gpkg_shrub_to_humid_areas_vegetation_8722" : "shrub_to_humid_veg",
    'va_shrub_transitions_variables_topo_clima_CLIMA_ATLES9120_PPTANUAL' : "avg_ppanual_91_20",
    'va_shrub_transitions_variables_topo_clima_CLIMA_ATLES9120_TMCANUAL' : "avg_tanual_91_20",
    "va_matollar_8722.gpkg_matollar_22_VA" : "remained_shrub_good",
    "va_burned.gpkg_arees_cremades_87_22_suma" : "burned_areas",
    'va_shrub_transitions_variables_topo_clima_burned_dist_dist_forest_87' : "dist_shrub_forest_87",
    'va_variables_estiu_hivern.gpkg_CLIMA_ATLES9120_PPTESTIU' : "precip_summer",
    "va_variables_estiu_hivern.gpkg_CLIMA_ATLES9120_TMCHIVERN" : "temp_winter"
    })

print(va_variables.columns)

va_variables_reindex = va_variables.reindex(["fid_pixel", "elevation", "slope", "hillshade", "aspect", 
                                             "avg_annual_rad", "twi", "avg_ppanual_91_20", "avg_tanual_91_20",
                                             "precip_summer", "temp_winter",
                                             "dist_shrub_forest_87",
                                             "remained_shrub", "remained_shrub_good",
                                             "shrub_to_forest",
                                             "shrub_to_agricultural_land",
                                             "shrub_to_urbanised",
                                             "shrub_to_meadow",
                                             "shrub_to_sparse_veg",
                                             "shrub_to_humid_veg",
                                             "shrub_to_otherclasses",
                                             "burned_areas",
                                             
                                             ], axis=1)


print(va_variables_reindex)

# inserció de la columna regió per saber de quina regió és cada pixel.

region = ["region"]

va_variables_reindex[region] = "va"

# eliminació de la columna repetida shrub

drop = va_variables_reindex.drop(columns=["remained_shrub"])

# canvi de nom de la columna shrub que hem deixat a la taula

drop_name = drop.rename(columns = {"remained_shrub_good" : "remained_shrub"})

va_shrub_transitions_topo_clima_variables_reindex = drop_name

print(va_shrub_transitions_topo_clima_variables_reindex)

va_shrub_transitions_topo_clima_variables_reindex.to_csv("va_shrub_transitions_topo_clima_variables_reindex.csv")

print("the end")