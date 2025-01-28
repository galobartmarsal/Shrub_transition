import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import earthpy as et
import seaborn as sns
from scipy.stats import norm 
from scipy.stats import spearmanr
from scipy.stats import f_oneway

os.chdir(os.path.join(r"C:\Users\galob\OneDrive\Documents\MARÇAL\1. DOCTORAT\1. PROJECTE\1r any\CORINE & MHC\Manual Habitats Catalunya\MSC\Matollar\MATOLLAR_15X15_REDO\catalunya"))

fname_cat = os.path.join("catalunya_filtered.csv")

catalunya = pd.read_csv(fname_cat)

print(catalunya.columns)
    
  
# comptatge de pixels per transicio

shrub = catalunya[catalunya["transicion"] == "shrub"]

print(shrub)


# boxplot de cada variable, per cada transició

plt.figure(figsize=(10, 6))
sns.boxplot(x='transicion', y='temp_winter', data=catalunya, showfliers=False)  # showfliers=False showfliers=False para ocultar outliers
plt.title('Boxplot temp_winter (without outliers)')
plt.xticks(rotation=45)  # Rotar etiquetas si son llargues
plt.show()





