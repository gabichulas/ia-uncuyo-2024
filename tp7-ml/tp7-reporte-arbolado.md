## Preprocesamiento

Para esta fase del *challenge*, lo principal en el preprocesamiento fue el balanceo de las clases, ya que habían muchos mas casos desfavorables que favorables, por lo que se recortaron los primeros para igualar a los segundos. Luego, se eliminaron variables que no aportaban mucho, como "area_seccion", "seccion", "ultima_modificacion" y obviamente "id". No fue necesario normalizar datos.

## Testing

Luego de probar con diversas combinaciones de hiperparámetros en el proceso de entrenamiento, dimos con una precisión de entre 70% y 72%. 

Cabe recalcar que también se realizaron pruebas realizando Sobresampleo en lugar de recortar la cantidad de casos desfavorables en el preprocesamiento, donde los modelos resultaban ser muy precisos en el set de validación (en promedio, 88%) pero muy pobres en el test de Kaggle (aprox. 50%), por lo que fueron descartados.

## Resultados

Finalmente, en Kaggle obtuvimos un puntaje de **0.70652**, cumpliendo el objetivo.

---

Trabajo hecho con Giovanni Azurduy