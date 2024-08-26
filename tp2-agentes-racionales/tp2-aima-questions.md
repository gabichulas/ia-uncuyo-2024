#### 2.10: Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement.

a. Can a simple reflex agent be perfectly rational for this environment? Explain.

b. What about a reflex agent with state? Design such an agent. 

c. How do your answers to **a ** and  **b** change if the agent’s percepts give it the clean/dirty status of every square in the environment?



#### <u>Respuesta</u>:

a. Un agente reflexivo simple no podría ser perfectamente racional en este entorno, ya que tiene una penalización por movimiento. Este agente, al tomar decisiones en base a su percepción pero sin tener en cuenta costos, sería incapaz de ser perfectamente racional.

b. Este tipo de agente puede tener memoria de lo ocurrido en el entorno con anterioridad, por lo que sería un poco mas racional que el anterior. Un posible diseño podría ser:

- Percepción: El agente tiene percepción de sus celdas adyacentes y mantiene un registro de su comportamiento anterior respecto a las celdas visitadas.

- Estado Interno: Mapa con datos sobre las visitas anteriores.

- Acciones:
  
  - Si limpia basura, guarda la información en su registro para no volver a pasar por ahí.
  
  - El agente busca el camino de menor costo hacia la próxima basura siguiendo los datos que éste contenga, evadiendo celdas ya limpiadas.
  
  - Si encuentra basura, la limpia.

c. 

- Agente reflexivo simple: Este agente no cambiaría demasiado. Podrían cambiarse las reglas para que este tenga un mayor rango de detección y solo se mueva a celdas que contengan basura, priorizando las más cercanas, pero sigue sin considerar los costos de movimiento.

- Agente reflexivo con estado: Por contrario, este agente cambia drásticamente y podría ser muy optimizado. Teniendo un entorno completamente observable y conocido, podríamos implementar algún algoritmo de búsqueda de caminos de menor costo, como Dijkstra, para que siempre siga el camino más corto entre celdas con basura.



#### 2.11: Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment—its extent, boundaries, and obstacles—is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right.)


a. Can a simple reflex agent be perfectly rational for this environment? Explain.
b. Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments.
c. Can you design an environment in which your randomized agent will perform poorly? Show your results.
d. Can a reflex agent with state outperform a simple reflex agent? Design such an agent
and measure its performance on several environments. Can you design a rational agent of this type?



##### <u>Respuesta</u>:

a. No. Un agente que se guía expresamente por su percepción, no podría ser racional si no puede percibir su entorno.

b. Al no conocer dónde se encuentra la basura, sería exactamente lo mismo. Podría moverse pero no limpiar, por lo que no cumpliría su objetivo.

d. Puede hacerlo, pero específicamente en este entorno, tiene los mismos problemas que el agente reflexivo simple, por lo que tampoco sumaría puntos.