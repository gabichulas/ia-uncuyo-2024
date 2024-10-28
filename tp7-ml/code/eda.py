import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"tp7-ml\data\arbolado-mendoza-dataset-train.csv")

# Distribucion inclinacion peligrosa:

var = "inclinacion_peligrosa"

plt.figure(figsize=(10,6))
sns.histplot(df[var], kde=True)
plt.savefig(r"tp7-ml\images\distribucion_inc_peligrosa.png")

# Distribucion secciones mas peligrosas

df_filtered = df[df[var]==1]

plt.figure(figsize=(10,6))
sns.histplot(df_filtered['seccion'], kde=True)
plt.savefig(r"tp7-ml\images\distribucion_secciones_peligrosas.png")

# Distribucion especies mas peligrosas

plt.figure(figsize=(10,6))
sns.histplot(df_filtered['especie'], kde=True)
plt.savefig(r"tp7-ml\images\distribucion_especies_peligrosas.png")


