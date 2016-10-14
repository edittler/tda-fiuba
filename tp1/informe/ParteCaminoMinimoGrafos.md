\newpage

# Camino mínimo en Grafos

Los problemas de camino mínimo en grafos consisten en encontrar una secuencia de
aristas desde un vértice de origen, al que llamaremos $s$ a uno de llegada, al
que llamaremos $t$, que sea la secuencia de menor costo total posible.
El costo total de un camino será la suma de los costos de cada una de las aristas.
Abajo se desarrollan 4 algoritmos posibles para lograr este objetivo.

Si bien todos los algoritmos calculan la distancia del camino mínimo, es posible
reconstruir ese camino si en el proceso se guarda en cada vértice el padre desde
el cual se llegó a él. De esta manera, al finalizar, queda construida la lista hacia
atrás de padres desde el origen que conforma el camino mínimo.


## Búsquedas No Informadas

Los primeros dos algoritmos que utilizaremos no conocen nada del problema modelado y por lo tanto no saben ni pueden estimar sobre lo que habrá más adelante en el grafo. Comienzan desde el vértice $t$ y su frontera de conocimiento sobre el grafo se va expandiendo desde allí.


### BFS

BFS es un recorrido en anchura de uso general para grafos no pesados (o de pesos
iguales, lo cual es equivalente).

Se puede utilizar para medir caminos mínimos en este tipo de grafos y la
solución devuelta es verdaderamente la óptima.
En grafos pesados, sin embargo, no queda garantizado que la solución sea
correcta, y en general no lo es: se obtendrá un camino de $s$ a $t$, pero la
distancia estará mal calculada o podrá no ser la mínima.

Este recorrido utiliza una cola para guardar todos los nodos adyascentes a cada
vértice, y luego desencolar un vértice de esa cola para repetir el proceso con
los aydascentes del nuevo.
De esta forma, la cola comienza únicamente con el vértice $s$, se desencola,
se encolan sus vecinos, y comienza el recorrido desde allí.

En el caso de su uso para búsqueda de camino mínimo, se etiqueta a cada vértice
al ser encolado con un nivel: una distancia discreta a $s$, el primer vértice
encolado, se lo etiqueta con nivel 0.
Luego, cada vértice encolado es etiquetado con el nivel de su padre incrementado en 1.
Al llegar el momento de encolar $t$, su nivel será la longitud del camino mínimo.

#### Optimalidad

Es importante notar que se recorre por niveles.
Es decir, siempre se recorrerán primero los vértices de distancia 0 ($s$),
luego se encolarán todos los vértices de nivel 1, luego se encolarán los de
nivel 2 (y antes de llegar a los de nivel 2 se habrán recorrido todos los del
nivel 1, gracias al orden FIFO) y así sucesivamente.
Esto permite asegurar que nunca se dará el caso de encontrar un camino
alternativo a un vértice que sea menor al antes calculado.

Esto no seguirá valiendo para grafos pesados, donde para asegurar aquello habrá
necesidad de utilizar una cola de prioridad, y en eso se basa Dijkstra.

#### Complejidad

Teniendo en cuenta el algoritmo desarrollado, lo que se hace es recorrer los
vertices una sola vez (se agregan a la cola si y solo si no fueron ya
agregados antes) cortando cuando se llega a destino. Además se recorren las
adyacencias de cada uno también una sola vez, por lo que se visitan las
aristas una sola vez.
En el peor de los casos, el nodo destino es el último que se encuentra, y se
habrán recorrido todos los nodos y aristas adyascentes, por
lo que este algoritmo es $O(|V| + |E|)$.

### Dijkstra

Dado un Grafo G y un vértice u del mismo, el algoritmo calcula la distancia de
$u$ a todos los otros vértices de G.
Opcionalmente, para calcular el camino mínimo entre dos vértices $u$ y $v$, se
puede utilizar Dijkstra hasta que se llegue a calcular la distancia a $v$ y se
lo detiene ahí.


#### Optimalidad

Al igual que BFS para caminos mínimos, Dijkstra se basa en que en todo momento, si se desencola un elemento, se asegura que se llegó a él con el menor costo posible. Para esto se utiliza una cola de prioridad, ordenada por el costo total en llegar desde $s$ hasta cada vértice por el camino desde el cual se lo agregó. Llamaremos a esta distancia $g(v)$.

De este modo nos aseguramos que al visitar un vértice (desencolarlo) se está llegando a él con el menor costo posible (si hubiese un costo menor, ya se lo habría visitado antes). Así como BFS aseguraba que primero se visitaran todos los elementos de nivel 1, luego los de nivel 2, etc, Dijkstra asegura que siempre se visitarán los elementos de menor distancia a $s$ antes de los de mayor distancia.

Entonces la prioridad se calcula con $g(v)$, vértice a vértice, incrementalmente.

Si se encuentra un camino alternativo a un vértice con costo menor, se lo agrega a la cola otra vez, con su nueva prioridad, con lo cual la alternativa más corta será la primera en ser visitada. Esto puede verse como una "actualización de prioridad".

A su vez, nunca ocurrirá que encontremos un camino alternativo más corto a un vértice ya visitado, ya que si así fuera, el subcamino hacia su padre nuevo habría sido visitado antes que él y habría sido agregado con esa prioridad antes
de ser visitado.

Estos puntos, teniendo en cuenta que **los pesos son positivos**, aseguran la optimalidad del algoritmo. Si hubiera pesos negativos, este algoritmo ya no sirve, porque bien podría ocurrir que se encuentrara un camino que supere al anterior en peso, y que al final tenga una arista que compensaba.

#### Complejidad

El algoritmo de Dijkstra se desarrolló utilizando una cola de prioridad implementada con un heap. Por lo que la extracción del siguiente nodo a procesar (menor distancia == raiz) es $O(1)$ y la inserción es $O(log |V|)$.
Ahora bien, en el peor de los casos, cada vertice está conectado a |V| - 1 vértices, que equivale a la cantidad de aristas por vértice. Habiendo implementado un heap, si tengo que encontrar y actualizar el heap por cada arista, entonces $O(|E| * (1 + log|V|))$ -> $O(|E| * log (|V|))$. Ahora, esto es iterativo para cada uno de los vertices del grafo (en el peor de los casos), por lo que sería $O( |V| * |E| * log(|V|))$. Finalmente, puede ajustarse a $O(|E| * log(|V|))$.

## Best First Search
Los dos algoritmos siguientes forman parte de una familia llamada *Best First Search*, que ordena el siguiente nodo a visitar con una función de evaluación f(n) que toma información inherente al problema modelado. Esta es una familia de algoritmos de *Búsqueda informada*.

Estos algoritmos, entonces, a diferencia de los anteriores, no utilizan solo
los datos de la estructura del grafo, si no de lo que representan en el modelo.
Estos datos en general permiten estimar la distancia entre los nodos según la
distancia en términos del problema, con una función llamada *heurística*.

### Heurísticas

Una heurística $h(u,v)$ es una función que *estima* la distancia entre los
vértices $u$ y $v$.

La forma más básica de Best First Search es la usualmente llamada greedy,
que consiste en ordenar únicamente los nodos a visitar por su distancia estimada
al nodo $t$. Esto es: $f(n) = h(n,t)$ De este modo, en lugar de recorrer por niveles
de lejanía al origen, se recorre según la aparente cercanía al destino.

El diseño de $h$ dependerá del problema modelado. Si, por ejemplo, el problema tiene
que ver con el mapa de una ciudad o un laberinto, una heurística puede ser la distancia Manhattan.
En un recorrido a gran escala, se podría usar, por ejemplo, el arco de
circunferencia mínimo entre $s$ y $t$.

Es importante notar que para que la estimación tenga sentido, los nodos deben tener información
de estado (en los ejemplos, la posición física) y los pesos de las aristas deben
también responder al modelo (por ejemplo, con la distancia real entre dos nodos conectados).

Del mismo modo, cabe aclarar que en problems de recorrido físico, $h$ no debe estimar
la distancia entre las posiciones de cada nodo, sino la distancia recorrible entre ambos **en el grafo**.
Por ejemplo, en una manzana de Manhattan, si bien la distancia real entre dos
esquinas es la diagonal que cruza por el centro de la manzana (distancia euclídea), la distancia
que debemos estimar es la que efectivamente costará llegar de una esquina a la
otra, y esta tendrá que ser dando la vuelta a la manzana.

#### Optimalidad

Esta búsqueda, solo con heurísticas, no asegura optimalidad, aunque mejora con la precisión de
la estimación de h sobre la distancia real del camino.

Si la distancia estimada fuera *exactamente igual* a la distancia real en el
grafo, entonces recorreríamos primero un camino mínimo y obtendríamos una
resolución óptima.

### A*

A\* es una mejora de Dijkstra, utilizando heurísticas. Así como Dijsktra ordena según la distancia total hasta un vértice $g(n)$ y la búsqueda con heurísticas minimiza $h(v,t)$, A\* ordena según la suma de ambas. Esta función de evaluación es entonces:

\begin{equation}
    f(v) = d(s,v) + h(v,t)
\end{equation}

De este modo, el orden tiene en cuenta tanto lo ocurrido como la estimación de lo que va a ocurrir por ese camino, lo cual permite una decisión más informada que Dijkstra.

A\* no es óptimo según cualquier heurística, y por eso hay dos propiedades importantes a estudiar.

#### Admisibilidad

Una heurística es admisible cuando nunca sobreestima una distancia.

\begin{equation}
    h(v,t) \le d(v,t)
\end{equation}

Si en la búsqueda permitiéramos expandir un nodo múltiples veces (lo que se suele llamar búsqueda en árboles) entonces se puede probar que una heurística hace que A\* sea óptimo. Puede demostrarse que siempre se elegirá un vértice de camino óptimo antes que un estado final $t$ por un camino subóptimo.

Para el diseño de heurísticas admisibles se suele tomar la estrategia de *problema relajado*, que consiste en simplificar el problema, para asegurarse de que la estimación subestime a la distancia.

En un laberinto, por ejemplo, utilizar la distancia Manhattan entre dos puntos consiste en la suposición de que no hay paredes.
De esta manera, la distancia estimada siempre será menor a la real, donde habrá obstáculos, y por lo tanto, será admisible.

Como propiedad adicional, si una heurística es admisible se cumple que $h(u,u) = 0$, lo cual hace que la función de evaluación en $t$ tenga heurística 0.

#### Consistencia

Que una heurística sea admisible, sin embargo, no es suficiente para poder ejecutar el algoritmo de la misma manera que Dijkstra, visitando una sola vez a cada nodo y sin necesidad de tener que actualizarlo. Para poder hacer esto, la heurística debe ser **consistente**.

Una heurística es consistente cuando se cumple que:

\begin{equation}
    h(u,w) \le h(v,w) + d(u,v)
\end{equation}
donde $u$, $v$ y $w$ son tres nodos cualesquiera. Se suele utilizar esta propiedad con $w=t$.

Esta propiedad es intuitivamente similar a la desigualdad triangular:

\begin{figure}[ht!]
    \centering
    \includegraphics[width=0.5\columnwidth]{images/desTriangular.png}
    \caption{Comparación de la desigualdad triangular con la consistencia.}
    \label{fig:bragg}
\end{figure}

Las heurísticas consistentes se llaman también monótonas porque se puede probar que en un camino cualquiera
la función de evaluación f(v) = g(v) + h(v,t) es no decreciente a lo largo del camino. Esta propiedad permite
ordenar según f(v) al igual que en Dijkstra se ordena según $g(v)$, sabiendo que al ser visitado un vértice,
no habrá un camino alternativo más corto (o en este caso con menor $f$) que el que se está expandiendo.

Además, se puede probar fácilmente por inducción que una heurística consistente también es admisible.

**Obs**: en el caso de $h(v) = 0 \quad \forall v$, se cae en el caso de Dijkstra, que es consistente.

#### Optimalidad

Para que una ejecución de A\* sea óptima (que devuelva el mejor camino) y que no se repitan vértices, la heurística utilizada debe ser consistente, y por lo tanto, también admisible.

Si bien es normal que las admisibles sean también consistentes, no ocurre siempre de este modo y es algo que hay que demostrar según el caso.

#### Eficiencia

Cuanto más se acerque una heurística consistente a la verdadera distancia, las elecciones que se tomen primero serán más probablemente las del camino óptimo y por lo tanto se llegará antes al destino $t$. De este modo, Dijkstra constituye la peor heurística consistente para A\*.

Por este motivo, en el problema del laberinto, si bien la distancia euclídea es
admisible (supone que no hay paredes y que uno se puede mover en cualquier
dirección), subestimará aún más a la distancia y por lo tanto es
probablemente menos eficiente que la distancia Manhattan.

De hecho, como $h_{euclidea} \le h_{manhattan} \quad \forall (u,v)$, se dice que la heurística con distancia Manhattan **domina** a la distancia euclídea y por lo tanto es mejor en cualquier punto.

Finalmente, si se tienen dos buenas heurísticas y ninguna domina a la otra, se puede calcular el máximo entre ambas, y esto dará una mejor heurística (y puede probarse que se mantiene la consistencia).

## Ejemplos

### Camino con Heurísticas contra A\*
Previamente se mencionó que mientras la búsqueda con Heurísticas plana se fija únicamente en lo estimado de lo que ocurrirá a futuro, mientras que A\* tiene en cuenta además lo que ocurrió hasta el momento. Esta diferencia puede verse clara en el grafo de la figura \ref{fig:ASvsH}.

Para la búsqueda con heurísticas se ve muy bien que ir por el camino de la derecha se acerca más rápido hacia el destinto $t$. Sin embargo, el desvío producido a partir del nodo 3 no empeora la distancia lo suficiente como para explorar a partir del nodo 14. Como este algoritmo no tiene en cuenta cuánto ya recorrió, entonces nunca explorará el camino de la izquierda, ya que estima la distancia estimada desde allí será de 6, mientras que a la derecha nunca supera 5.

Por este motivo, el programa ejecuta y muestra:

\begin{verbatim}
Camino con búsqueda por heurísticas:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Camino con A*:
[0, 14, 15, 16, 17, 18, 19, 13]
----.----
\end{verbatim}

\begin{figure}[ht!]
    \centering
    \includegraphics[width=0.5\columnwidth]{images/ASvsH.png}
    \caption{Recorridos en A* y en Heurísticas}
    \label{fig:ASvsH}
\end{figure}
