# Introducción

Debemos resolver el famoso problema de las $N$-reinas. Para esto, usaremos los siguientes algoritmos:

- Hill Climbing
- Simulated Annealing
- Algoritmos Genéticos

Los escenarios iniciales son generados de forma aleatoria y puede no encontrarse una solución.

---

# Marco teórico

Algo importante a tener en cuenta, es la *heurística* a utilizar (simbolizada de ahora en más como $H(e)$). Esta función contabiliza la cantidad de reinas amenazadas en un tablero.

**Descripción de los algoritmos puestos a prueba**:

1. **Hill Climbing**:
    
    - Es un método de búsqueda local que intenta mejorar iterativamente la solución actual seleccionando estados vecinos con mejor puntaje según una función objetivo.
    - En el caso de las $N$-reinas, la función $H(e)$ cuenta la cantidad de pares de reinas que se amenazan. El objetivo es minimizar $H(e)$ hasta llegar a cero.
    
2. **Simulated Annealing**:
    
    - Es una variante del Hill Climbing que permite aceptar soluciones peores con una probabilidad decreciente, simulando un proceso de enfriamiento. Esto ayuda a escapar de mínimos locales.
    - Para las $N$-reinas, el enfriamiento gradual permite que el algoritmo explore soluciones más diversas antes de enfocarse en las mejores.
    
3. **Algoritmo Genético**:
    
    - Inspirado en la evolución biológica, este método utiliza una población de soluciones, aplicando operadores de selección, cruza y mutación para evolucionar hacia mejores soluciones.
    - En este caso, cada individuo representa una posible disposición de las reinas, y se evalúa la aptitud de cada uno según la función $H(e)$.
    - Para estos experimentos, se utilizaron dos variantes de estos. `genetic` se queda con el 15% de los mejores candidatos de su iteración, generando el 85% restante de manera aleatoria. Al contrario, `genetic2` no realiza ninguna operación similar, quedándose con todos los candidatos resultantes de la selección, cruza y mutación realizadas.


---

# Diseño experimental

- Se implementaron los algoritmos mencionados para resolver el problema de las N-reinas con valores de $N = 4, 8, 10, 12, 15$.
- Cada algoritmo se ejecutó 30 veces por cada valor de $N$.
- Se registró:
    - El porcentaje de veces que cada algoritmo alcanzó una solución óptima.
    - El tiempo promedio de ejecución y su desviación estándar.
    - La cantidad promedio de estados visitados antes de encontrar una solución, junto a su desviación estándar.
    - Variaciones de $H(e)$ a lo largo de las iteraciones para una ejecución particular.


---

# Análisis y discusión de resultados


Para comenzar, veremos el porcentaje de éxito de cada algoritmo según los tamaños de tableros.
![[success_rate.png]]

Podemos observar, primero que nada, que Hill Climbing tiene un comportamiento bastante pobre comparado con el resto.

Luego, vemos que Simulated Annealing tiene un rendimiento bastante decente, siendo el único que encuentra soluciones en el entorno más grande (teniendo en cuenta el límite de 1000 iteraciones). Sin embargo, podemos deducir, por la misma naturaleza del algoritmo, que el algoritmo genético tendría un mucho mejor rendimiento en el caso de no existir un límite de iteraciones. Podemos pensar esto, por ejemplo, porque el resto de algoritmos llegan a una solución (o quedan atrapados en un mínimo local) mucho antes de llegar a las 1000 iteraciones.

![[mean_execution_time.png]]

En este gráfico podemos observar la gran diferencia de tiempos de ejecución entre los algoritmos genéticos y el resto, siendo las barras correspondientes a Hill Climbing y Simulated Annealing casi imperceptibles.


A continuación, veremos el cambio de $H(e)$ a través de una ejecución de cada algoritmo.

![[h_list_hc_lineplot.png]]
![[h_list_hc_lineplot.png]]
![[h_list_gen1_lineplot.png]]
![[h_list_gen2_lineplot.png]]

Estos son casos muy favorables para HC y SA, ya que se seleccionaron ejecuciones en las que se llegó a una solución, y muy rápido. 

Aquí podemos ver con mucha claridad la gran ventaja de seleccionar solo una parte de la población al momento de pasar a la siguiente generación.

Finalmente, veremos la distribución de tiempos y generaciones según los algoritmos utilizados.


**Hill Climbing**:

![[hill_climbing_generations_boxplot.png]]
![[hill_climbing_time_boxplot.png]]

**Simulated Annealing**:

![[simulated_annealing_generations_boxplot.png]]
![[simulated_annealing_time_boxplot.png]]


**Algoritmo genético**:

![[genetic_generations_boxplot.png]]
![[genetic_time_boxplot.png]]

---

# Conclusión

En resumen:

- El Hill Climbing es rápido, pero a menudo queda atrapado en mínimos locales.
- El Simulated Annealing, aunque más lento, ofrece una mejor exploración del espacio de soluciones.
- El Algoritmo Genético resulta ser el más robusto para encontrar soluciones, pero a un costo computacional mayor.

En este caso específico, con el límite de iteraciones establecido, Simulated Annealing resulta ser el mejor, pero el Algoritmo Genético sería mucho más eficiente de no tener este límite.