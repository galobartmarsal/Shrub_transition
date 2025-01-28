import os

import matplotlib.pyplot as plt
import pandas as pd
import earthpy as et


# Importar base dades LL variables

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\vegueries\ll"))

fname_ll = os.path.join("ll_variables.csv")

ll_variables = pd.read_csv(fname_ll)

print(ll_variables.columns)

# inspecció dels noms de columnes, canvi de noms i organizació de columnes

ll_variables = ll_variables.rename(columns={
    "fid":"fid_pixel",
    "Aspect" : "aspect",
    "Elevation" : "elevation",
    "Hillshade" : "hillshade",
    "Slope" : "slope",
    "TWI" : "twi",
    "forest_transition" : "shrub_to_forest",
    "rad_ll_Cat_rad_anual_averg" : "avg_annual_rad",
    "ll_shurb_transitions_points.gpkg_agricultured_shrub_8722" : "shrub_to_agricultural_land",
    "ll_shurb_transitions_points.gpkg_ll_matollar_87n22_noburned" : "remained_shrub",
    "ll_shurb_transitions_points.gpkg_urbanised_shrub_8722" : "shrub_to_urbanised",
    "ll_shurb_transitions_points.gpkg_shrub_to_other_classes_8722" : "shrub_to_otherclasses",
    "ll_shurb_transitions_points.gpkg_shrub87andmeadow22_2" : "shrub_to_meadow",
    "ll_shurb_transitions_points.gpkg_sparse_vegetation_22" : "shrub_to_sparse_veg",
    "ll_shurb_transitions_points.gpkg_shrub_to_humid_areas_vegetation_8722" : "shrub_to_humid_veg",
    'll_shrub_transitions_variables_topo_clima_CLIMA_ATLES9120_PPTANUAL' : "avg_ppanual_91_20",
    'll_shrub_transitions_variables_topo_clima_CLIMA_ATLES9120_TMCANUAL' : "avg_tanual_91_20",
    'll_matollar_8722.gpkg_matollar_22_LL' : "remained_shrub_good",
    "ll_burned.gpkg_arees_cremades_87_22_suma" : "burned_areas",
    'll_shrub_transitions_variables_topo_clima_burned_distance — vector_673473d1e70116_dist_to_forest_87' : "dist_shrub_forest_87",
    'll_variables_estiu_hivern.gpkg_CLIMA_ATLES9120_PPTESTIU' : "precip_summer",
    'll_variables_estiu_hivern.gpkg_CLIMA_ATLES9120_TMCHIVERN' : "temp_winter"
    
    })

print(ll_variables.columns)

ll_variables_reindex = ll_variables.reindex(["fid_pixel", "elevation", "slope", "hillshade", "aspect", 
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


print(ll_variables_reindex.columns)

# inserció de la columna regió per saber de quina regió és cada pixel.

region = ["region"]

ll_variables_reindex[region] = "ll"

# eliminació de la columna repetida shrub

drop = ll_variables_reindex.drop(columns=["remained_shrub"])

# canvi de nom de la columna shrub que hem deixat a la taula

drop_name = drop.rename(columns = {"remained_shrub_good" : "remained_shrub"})

ll_shrub_transitions_topo_clima_variables_reindex = drop_name

print(ll_shrub_transitions_topo_clima_variables_reindex)

ll_shrub_transitions_topo_clima_variables_reindex.to_csv("ll_shrub_transitions_topo_clima_variables_reindex.csv")

print("the end")