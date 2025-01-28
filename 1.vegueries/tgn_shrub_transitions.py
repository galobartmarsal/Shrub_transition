import os

import matplotlib.pyplot as plt
import pandas as pd
import earthpy as et


# Importar base dades TGN variables

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\tgn"))

fname_tgn = os.path.join("tgn_variables.csv")

tgn_variables = pd.read_csv(fname_tgn)

print(tgn_variables.columns)

# inspecció dels noms de columnes, canvi de noms i organizació de columnes

tgn_variables = tgn_variables.rename(columns={
    "fid":"fid_pixel",
    "Aspect" : "aspect",
    "Elevation" : "elevation",
    "Hillshade" : "hillshade",
    "Slope" : "slope",
    "TWI" : "twi",
    "forest_transition" : "shrub_to_forest",
    "tgn_shrub87_variables_points_2.gpkg_Cat_rad_anual_averg" : "avg_annual_rad",
    "tgn_shrub_transitions_points.gpkg_agricultured_shrub_8722" : "shrub_to_agricultural_land",
    "tgn_shrub_transitions_points.gpkg_tgn_matollar_87n22_noburned" : "remained_shrub",
    "tgn_shrub_transitions_points.gpkg_urbanised_shrub_8722" : "shrub_to_urbanised",
    "tgn_shrub_transitions_points.gpkg_shrub_to_other_classes_8722" : "shrub_to_otherclasses",
    "tgn_shrub_transitions_points.gpkg_shrub87andmeadow22_2" : "shrub_to_meadow",
    "tgn_shrub_transitions_points.gpkg_sparse_vegetation_22" : "shrub_to_sparse_veg",
    "tgn_shrub_transitions_points.gpkg_shrub_to_humid_areas_vegetation_8722" : "shrub_to_humid_veg",
    'tgn_shrub_transitions_variables_topo_clima_CLIMA_ATLES9120_PPTANUAL' : "avg_ppanual_91_20",
    'tgn_shrub_transitions_variables_topo_clima_CLIMA_ATLES9120_TMCANUAL' : "avg_tanual_91_20",
    "tgn_matollar_8722.gpkg_matollar_22_TG" : "remained_shrub_good",
    "tgn_burned.gpkg_arees_cremades_87_22_suma" : "burned_areas",
    'tgn_shrub_transitions_variables_topo_clima_burned_dist — vector_673464f6c33f32_dist_to_forest_87' : "dist_shrub_forest_87",
    'tgn_variables_estiu_hivern.gpkg_CLIMA_ATLES9120_PPTESTIU' : "precip_summer",
    "tgn_variables_estiu_hivern.gpkg_CLIMA_ATLES9120_TMCHIVERN" : "temp_winter"

    })

print(tgn_variables.columns)

tgn_variables_reindex = tgn_variables.reindex(["fid_pixel", "elevation", "slope", "hillshade", "aspect", 
                                             "avg_annual_rad", "twi", "avg_ppanual_91_20", "avg_tanual_91_20",
                                             "precip_summer" , "temp_winter",
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


print(tgn_variables_reindex.columns)

# inserció de la columna regió per saber de quina regió és cada pixel.

region = ["region"]

tgn_variables_reindex[region] = "tgn"

# eliminació de la columna repetida shrub

drop = tgn_variables_reindex.drop(columns=["remained_shrub"])

# canvi de nom de la columna shrub que hem deixat a la taula

drop_name = drop.rename(columns = {"remained_shrub_good" : "remained_shrub"})

tgn_shrub_transitions_topo_clima_variables_reindex = drop_name

print(tgn_shrub_transitions_topo_clima_variables_reindex)

tgn_shrub_transitions_topo_clima_variables_reindex.to_csv("tgn_shrub_transitions_topo_clima_variables_reindex.csv")

print("the end")
