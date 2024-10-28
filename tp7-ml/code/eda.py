import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"tp7-ml\data\arbolado-mendoza-dataset-train.csv")

# Punto 2
# Distribucion inclinacion peligrosa:

var = "inclinacion_peligrosa"

plt.figure(figsize=(10,6))
sns.histplot(df[var], kde=True)
plt.savefig(r"tp7-ml\images\distribucion_inc_peligrosa.png")
plt.close()

# Distribucion secciones mas peligrosas

df_filtered = df[df[var]==1]

plt.figure(figsize=(10,6))
sns.histplot(df_filtered['seccion'], kde=True)
plt.savefig(r"tp7-ml\images\distribucion_secciones_peligrosas.png")
plt.close()

# Distribucion especies mas peligrosas

plt.figure(figsize=(10,6))
sns.histplot(df_filtered['especie'], kde=True)
plt.savefig(r"tp7-ml\images\distribucion_especies_peligrosas.png")
plt.close()

# Punto 3
# Histogramas circunferencia tronco

bins = [5, 10, 15, 20, 30, 40]

for bin in bins:
    plt.figure(figsize=(10,6))
    sns.histplot(df["circ_tronco_cm"],bins=bin , kde=True)
    plt.savefig(r"tp7-ml\images\distribucion_circ_tronco_cm"+f"_{bin}bins"+".png")
    plt.close()

# Histogramas segun inclinacion peligrosa

for bin in bins:
    plt.figure(figsize=(10,6))
    sns.histplot(df[df[var]==0]["circ_tronco_cm"],bins=bin , kde=True)
    plt.savefig(r"tp7-ml\images\hist_groupedby_inc\0\distribucion_circ_tronco_cm"+f"_{bin}bins"+"_not_dangerous.png")
    plt.close()

for bin in bins:
    plt.figure(figsize=(10,6))
    sns.histplot(df[df[var]==1]["circ_tronco_cm"],bins=bin , kde=True)
    plt.savefig(r"tp7-ml\images\hist_groupedby_inc\1\distribucion_circ_tronco_cm"+f"_{bin}bins"+"_dangerous.png")
    plt.close()