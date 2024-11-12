import pandas as pd
import numpy as np

# Función para calcular la entropía
def entropy(data, class_name):
    values = data[class_name].value_counts(normalize=True)
    return -np.sum(values * np.log2(values))

# Función para calcular la ganancia de información de un atributo
def information_gain(data, feature, class_name):
    # Entropía total del conjunto
    total_entropy = entropy(data, class_name)

    # Entropía después de la división por la característica
    feature_values = data[feature].value_counts()
    weighted_entropy = 0
    for value in feature_values.index:
        subset = data[data[feature] == value]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset, class_name)
    
    return total_entropy - weighted_entropy

# Función para seleccionar el mejor atributo basado en la ganancia de información
def best_split(data, class_name):
    best_feature = None
    best_gain = -1
    for feature in data.columns[:-1]:  # Exceptuamos la columna de clase
        gain = information_gain(data, feature, class_name)
        if gain > best_gain:
            best_gain = gain
            best_feature = feature
    return best_feature

# Función para construir el árbol de decisión
def build_tree(data, attribs, default, class_name):
    # Si todos los ejemplos tienen la misma clase, devolvemos un nodo hoja con esa clase
    if len(data[class_name].unique()) == 1:
        return {data[class_name].iloc[0]: {}}
    
    # Si no hay más atributos para dividir, devolvemos la clase mayoritaria
    if len(attribs) == 0:
        return {default: {}}
    
    # Elegir el mejor atributo basado en la ganancia de información
    best_feature = best_split(data, class_name)
    
    # Si no se puede dividir más, devolvemos la clase mayoritaria
    if best_feature is None:
        return {default: {}}
    
    # Crear el nodo para el mejor atributo
    tree = {best_feature: {}}  
    
    # Dividir los datos en subconjuntos según los valores del mejor atributo
    for value in data[best_feature].unique():
        subset = data[data[best_feature] == value].drop(columns=[best_feature])
        subtree = build_tree(subset, attribs.drop([best_feature]), default, class_name)
        tree[best_feature][value] = subtree 
    
    return tree

# Cargar el dataset
data = pd.read_csv(r'tp7-ml\data\tennis.csv')
data.columns = data.columns.str.strip()
attribs = data.columns.drop("play")
default = data['play'].mode()[0]

# Llamar a la función de aprendizaje del árbol de decisión
tree = build_tree(data, attribs, default, "play")

# Mostrar el árbol de decisión generado
print("Decision Tree:")
print(tree)
