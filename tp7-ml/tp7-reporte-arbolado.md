## Preprocesamiento

Para esta fase del *challenge*, lo principal en el preprocesamiento fue el balanceo de las clases, ya que habían muchos mas casos desfavorables que favorables, por lo que se recortaron los primeros para igualar a los segundos. Luego, se eliminaron variables que no aportaban mucho, como "area_seccion", "seccion", "ultima_modificacion" y obviamente "id". No fue necesario normalizar datos.

## Testing

Luego de probar con diversas combinaciones de hiperparámetros en el proceso de entrenamiento, dimos con una precisión de entre 70% y 72%. 

Cabe recalcar que también se realizaron pruebas realizando Sobresampleo en lugar de recortar la cantidad de casos desfavorables en el preprocesamiento, donde los modelos resultaban ser muy precisos en el set de validación (en promedio, 88%) pero muy pobres en el test de Kaggle (aprox. 50%), por lo que fueron descartados.

## Resultados

Finalmente, en Kaggle obtuvimos un puntaje de **0.70652**, cumpliendo el objetivo.

## Descripción

El algoritmo realizado consiste, principalmente, de tres partes: preprocesamiento, entrenamiento y testeo. Ya hablamos de la primera y la última, por lo que se describirá el proceso de entrenamiento del modelo.

Teniendo nuestro dataframe balanceado, separado y únicamente con las columnas que nos interesan, ya podemos pasar al proceso de entrenamiento. 

Afortunadamente, gracias a las librerías de R (o de cualquier otro lenguaje) este proceso se puede hacer en unas pocas líneas de código, lo cual no quiere decir que es sencillo. La elección del modelo e hiperparámetros requieren un conocimiento profundo y una mala elección de estos puede desembocar en un modelo pobre, por lo que, informándonos y jugando con la librería, llegamos a la conclusión de que los hiperparámetros que mejores resultados daban son: 

- ntree (número de árboles en el Random Forest): Entre 3000 y 5000.
- mtry (número de features seleccionadas al azar en cada decisión): 2.

Cabe recalcar que hay muchos otros hiperparámetros con los que jugamos, pero no encontramos diferencias significativas al momento de testear los modelos, y al no saber al 100% como funcionaban, los omitimos.

---

Trabajo hecho con Giovanni Azurduy