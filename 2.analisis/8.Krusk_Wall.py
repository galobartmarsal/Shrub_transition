import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from scipy.stats import kruskal

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\catalunya"))

fname_cat = os.path.join("catalunya_filtered.csv")

catalunya_filtered = pd.read_csv(fname_cat)

data = catalunya_filtered

print(data.columns)

#avaluació correlacio entre transicions i variables - elevation


shrub_shrub = data[data["transicion"] == "shrub"]["elevation"]
shrub_forest = data[data["transicion"] == "forest"]["elevation"]
shrub_agriculture = data[data["transicion"] == "agriculture"]["elevation"]
shrub_urban = data[data["transicion"] == "urban"]["elevation"]
shrub_meadow = data[data["transicion"] == "meadow"]["elevation"]
shrub_sparse = data[data["transicion"] == "sparse"]["elevation"]
shrub_humid = data[data["transicion"] == "humid"]["elevation"]
shrub_other = data[data["transicion"] == "other"]["elevation"]

stat, p = kruskal(shrub_shrub, shrub_forest, shrub_agriculture, shrub_urban, shrub_meadow,
                  shrub_sparse, shrub_humid, shrub_other)

print("Estadistic H:" , stat, "p-value", p)

if p < 0.05:
    print("Hay diferencias significativas entre los grupos.")

else:
    print("No hay diferencias significativas entre los grupos.")


