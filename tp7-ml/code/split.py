import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('tp7-ml/data/arbolado-mza-dataset.csv')

train_df, validation_df = train_test_split(df, test_size=0.2, random_state=2606)

validation_df.to_csv('tp7-ml/data/arbolado-mendoza-dataset-validation.csv', index=False)
train_df.to_csv('tp7-ml/data/arbolado-mendoza-dataset-train.csv', index=False)