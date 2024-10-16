
# Ejercicio 1

**a)** En este caso, la mejor opción es elegir un *modelo inflexible*. Esto se debe a que al tener una baja cantidad de *predictores* corremos un gran riesgo de *overfitting* si usamos un *modelo flexible*. Tampoco deberíamos preocuparnos demasiado por el error del modelo, ya que aunque por definición un modelo flexible se ajustaría mejor que un inflexible con la misma cantidad de datos, buscando relaciones más complejas entre los predictores y la respuesta, el gran tamaño de la muestra nos asegura una predicción al menos decente con un modelo inflexible, como por ejemplo una **regresión lineal**.

**b)** A pesar de que es un escenario bastante malo para nosotros, hay maneras de abordarlo. La peor forma definitivamente sería un modelo inflexible, ya que la gran cantidad de dimensiones (*predictores*) dificultaría mucho el ajuste a este tipo de modelos, cayendo en un muy probable overfit. Por el contrario, sabemos que un bajo tamaño de $n$ tampoco es un buen escenario para un modelo flexible, pero podemos usar un modelo que use alguna técnica de **regularización**, para priorizar ciertos predictores por sobre otros y deshacernos de la alta dimensionalidad, centrándonos en los predictores más relevantes y evitando el overfit.

**c)** Los métodos flexibles son, por naturaleza, los mejores para capturar soluciones no lineales, así que no hay muchas dudas en este caso. Un modelo inflexible sería muy malo en una situación como esta.

**d)** La mejor opción es un modelo inflexible, ya que es más probable que no intente ajustarse al ruido presente en los datos. Al usar un modelo flexible, que sabemos que se aferra mucho al dataset con el que trabajamos, buscando relaciones complejas y no lineales, la probabilidad de sobreajuste es muy alta, derivando en un rendimiento deficiente ante nuevos datos. Esta situación de puede ver reflejada en el siguiente gráfico (Izq: baja varianza, Der: alta varianza)


![[Pasted image 20241016112446.png]]

---

# Ejercicio 2

**a)** $n = 500$ y $p = 3$.
**b)** $n = 20$ y $p = 13$.
**c)** $n = 52$ y $p = 3$.

---

# Ejercicio 5

Ya fue mencionado en el ejercicio 1, pero en rasgos generales:

|                | Ventajas                                                                               | Desventajas                                                                                                                                                           |
| -------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Flexible**   | - Capacidad para capturar relaciones complejas<br>- Fácil adaptación a los datos<br>   | - Riesgo de overfit<br>- Necesidad de mayor cantidad de datos                                                                                                         |
| **Inflexible** | - Simplicidad del modelo<br>- Poco riesgo de overfit<br>- No se necesitan muchos datos | - Incapacidad para capturar relaciones complejas<br>- Mala adaptación a varianza en los datos<br>- Mal rendimiento con datos complejos o gran cantidad de predictores |

Generalmente, preferiríamos un enfoque flexible cuando tenemos una gran cantidad de datos y sabemos que las relaciones que existen no son lineales. Por contrario, elegiríamos un modelo inflexible cuando tenemos pocos predictores y relaciones lineales y mucho más simples.

---

# Ejercicio 6

| Característica                | Enfoques Paramétricos                                        | Enfoques No Paramétricos                                           |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------ |
| **Estructura**                | Asumen una forma específica para la relación.                | No asumen una forma específica, se adaptan a los datos.            |
| **Flexibilidad**              | Limitados a la forma asumida.                                | Más flexibles, pueden capturar relaciones complejas y no lineales. |
| **Requerimiento de Datos**    | Requieren menos datos para un ajuste efectivo.               | Necesitan muchos más datos para estimar patrones confiables.       |
| **Complejidad Computacional** | Más simples y rápidos de entrenar.                           | Pueden ser más complejos y costosos computacionalmente.            |
| **Riesgo de Sesgo**           | Pueden tener un alto sesgo si se elige mal la forma asumida. | Menor riesgo de sesgo, pero mayor riesgo de overfit.               |
| **Interpretabilidad**         | Más fáciles de interpretar.                                  | Menos interpretables debido a su complejidad.                      |

---

# Ejercicio 7

**a)** Las distancias euclidianas son:

1. 3
2. 2
3. 3.16228
4. 2.23607
5. 1.414214
6. 1.73205

**b)** Con $K = 1$, debemos elegir solo un vecino, el más cercano, el cual es el número 5. Como no tenemos otros vecinos con los que comparar resultados, el nuestra predicción es `Green`.

**c)** Con $K = 3$, debemos elegir los tres vecinos más cercanos, los cuales son las observaciones 5 (`Green`), 6 (`Red`) y 2 (`Red`), en ese orden. Como la respuesta más repetida es `Red`, esa es nuestra predicción.

**d)** Creo que $K$ debería ser pequeño, ya que mientras más chico es, KNN es más preciso en sus decisiones. Un $K$ demasiado grande tendería a un muy probable underfit, ya que no se comporta como el resto de modelos que vimos.