# Introducción

Se nos plantea que, dados dos tipos de entornos (que serán descritos más adelante), debemos encontrar el camino más corto entre un agente y un objetivo. Para esto utilizaremos diversos tipos de algoritmos, como *BFS*, *DFS*, *A Star* y hasta un agente completamente aleatorio. Estos entornos están generados de forma aleatoria y puede no haber ninguna solución.

-------------------------------------------------------------------

# Marco teórico


### Entornos

Como se mencionó previamente, tenemos dos tipos de entornos posibles:

- **Entorno 1**: Todos los movimientos tienen el mismo costo, 1. ^9d16dg
- **Entorno 2**: Los movimientos tienen un costo asociado. Moverse hacia la izquierda tiene costo 1, hacia abajo costo 2, etc. ^9d16df

Estos son grillas cuadradas (8x8, 16x16) que tienen una cantidad de obstáculos determinada por `hprob`, un número entre 0 y 1 que indica la proporción de obstáculos respecto a la cantidad total de casillas. 

La salida y el objetivo suelen ser la primer y última casilla respectivamente, pero también pueden ser ubicadas de forma aleatoria. 

### Agente

Nuestro agente siempre va a ser el mismo. Este tiene siempre la misma cantidad de vidas: 100. Las vidas son completamente independientes del costo asociado por movimiento del [Entorno 2](#^9d16df). Este puede o no encontrar un camino hacia el objetivo.

El agente va a comportarse según ciertos algoritmos, a excepción de un tipo que tiene un comportamiento totalmente aleatorio, sin ningún tipo de percepción de su alrededor.

### Algoritmos

Los algoritmos a usar son:

- BFS (Breadth First Search)
- DFS (Depth First Search)
- DLS (Depth Limited Search)
- UCS (Uniform Cost Search)
- A*

Para hacer más conciso el informe, solo se mencionará que la heurística utilizada para A* es la **Distancia Manhattan**, dada por:


$\displaystyle d_{Manhattan}(p, q) = |\Delta x| + |\Delta y| = |x_2 - x_1| + |y_2 - y_1|$


---


# Diseño experimental


Para recopilar datos suficientes y poder visualizarlos de forma gráfica, se realizaron, por cada algoritmo, 30 iteraciones. Los entornos, numerados del 0 al 29, siempre son los mismos. Esto para garantizar la uniformidad y consistencia de los resultados.

La información guardada fue: 

- Número del entorno.
- Casillas exploradas en total.
- Costo para [Entorno 1](#^9d16dg).
- Costo para [Entorno 2](#^9d16df).
- Tiempo empleado.
- ¿Solución encontrada?


---


# Análisis y discusión de resultados


Para el análisis de los datos, se realizaron gráficos de caja, para visualizar de forma adecuada la dispersión de los resultados.


![[tp4-busquedas-informadas/images/boxplot_cost_e1_por_algorithm_name.png]]

Como podemos observar, para el primer entorno, los resultados no están tan dispersos, a excepción del agente aleatorio. Debemos tener en cuenta que, al ser aleatorio y tener muy poca probabilidad de llegar al objetivo, los costos van a tender a cero, lo que significa que no se llegó al destino. También podemos observar una gran dispersión, con intentos llegando a casi 80 movimientos.

![[tp4-busquedas-informadas/images/boxplot_cost_e2_por_algorithm_name.png]]

Para el segundo tipo de entorno, podemos ver que solo *ucs2* cambió. Esto se debe a que el resto de algoritmos no se rigen por los costos asociados en este tipo de entorno. Si esto fuera así, muy probablemente este sería uno de los que mejores resultados arrojaría.


![[tp4-busquedas-informadas/images/boxplot_time_por_algorithm_name.png]]


Para finalizar, tenemos un *boxplot* que nos muestra la diferencia entre los tiempos de ejecución de estos algoritmos. Podemos observar que, a excepción de *rand*, que claramente no es nada consistente, los últimos algoritmos tienden a tardar más. Esto no es necesariamente malo, ya que solo habla de su complejidad temporal, y los resultados nos muestran que, a pesar de ser de los que más tardan, A* es uno de los mejores.


---


# Conclusión

En este informe hemos explorado diversos algoritmos de búsqueda en dos tipos de entornos, cada uno con características y restricciones particulares. Los resultados obtenidos nos permiten hacer algunas observaciones clave.

Primero, en el **Entorno 1**, donde todos los movimientos tienen el mismo costo, los algoritmos de búsqueda informada, como A*, muestran un desempeño superior en términos de consistencia y efectividad para encontrar soluciones, mientras que el comportamiento aleatorio fue el menos eficiente. La **Distancia Manhattan** utilizada como heurística para A* demostró ser adecuada para minimizar los movimientos en este entorno.

En el **Entorno 2**, donde los movimientos tienen un costo variable, el algoritmo UCS (Uniform Cost Search) fue el único que cambió su comportamiento, mostrando un ajuste significativo debido a la consideración de los costos de los movimientos. Esto evidencia que los algoritmos que no toman en cuenta estos costos pueden no ser los más eficientes en este tipo de entorno, lo que sugiere que UCS podría ser el más adecuado para entornos donde los costos de movimiento varían.

Finalmente, en cuanto al tiempo de ejecución, algoritmos más complejos como A* tienden a tardar más, pero su precisión y capacidad para encontrar soluciones óptimas justifican el tiempo adicional en la mayoría de los casos. El análisis temporal muestra que hay un balance claro entre tiempo y efectividad, siendo A* una de las mejores opciones en términos de resultados, a pesar de su mayor complejidad temporal.

En resumen, la elección del algoritmo depende tanto del entorno como de la prioridad entre eficiencia en tiempo o costo de movimientos. Algoritmos como A* y UCS muestran ser los más robustos y adaptables a diversas condiciones, mientras que el comportamiento aleatorio, aunque interesante para ciertos estudios, no ofrece resultados consistentes ni eficientes en la mayoría de los casos.
