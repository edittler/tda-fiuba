Para todos los casos llamaremos _s_ al nodo de salida u origen y _t_ al nodo de llegada u objetivo.

## BFS

BFS es un recorrido en anchura de uso general para grafos no pesados (o de pesos iguales, lo cual es equivalente). Se puede utilizar para medir caminos mínimos en este tipo de grafos y la solución devuelta es verdaderamente la óptima. En grafos pesados, sin embargo, no queda garantizado que la solución sea correcta, y en general no lo es: se obtendrá un camino de _s_ a _t_, pero la distancia estará mal calculada o podrá no ser la mínima.

Este recorrido utiliza una cola para guardar todos los nodos adyascentes a cada vértice, y luego desencolar un vértice de esa cola para repetir el proceso con los aydascentes del nuevo. De esta forma, la cola comineza únicamente con el vértice _s_, se desencola, se encolan sus vecinos, y comienza el recorrido desde allí.

En el caso de su uso para búsqueda de camino mínimo, se etiqueta a cada vértice al ser encolado con un nivel: una distancia discreta a _s_. a _s_, el primer vértice encolado, se lo etiqueta con nivel 0. Luego, cada vértice encolado es etiquetado con el nivel de su padre, incrementado en 1. Al llegar el momento de encolar _t_, su nivel será la longitud del camino mínimo.

### Optimalidad
Es importante notar que se recorre por niveles. Es decir, siempre se recorrerán primero los vértices de distancia 0 (_s_), luego se encolarán todos los vértices de nivel 1, luego se encolarán los de nivel 2 (y antes de llegar a los de nivel 2 se habrán recorrido todos los del nivel 1, gracias gracias al orden FIFO) y así sucesivamente. Esto permite asegurar que nunca se dará el caso de encontrar un camino alternativo a un vértice que sea menor al antes calculado.

Esto no seguirá valiendo para Grafos pesados, donde para asegurar aquello habrá necesidad de utilizar una cola de prioridad, y en eso se basa Dijkstra.

### Reconstrucción

Tanto para este algoritmo como para otros, para reconstruir el camino basta guardar los padres de cada nodo encolado para luego armar la lista hacia atrás desde el destino.

## Heurísticas

La búsqueda con Heurísticas utiliza un criterio distinto para recorrer el grafo. En lugar de una cola común utiliza una cola de prioridad, ordenada según una función _h(u,v)_ llamada Heurística, que _estima_ la distancia entre los vértices _u_ y _v_. De este modo, en lugar de recorrer por niveles, se recorre según lo estimado, recorriendo siempre primero lo que _aparenta_ estar más cercano del destino.

La función heurística requiere un diseño que no es inherente al grafo como estructura abstracta, sino que responde al problema que se está modelando. Si por ejemplo, el problema tiene que ver con el mapa de una ciudad o un laberinto, una heurística puede ser la distancia Manhattan. En un recorrido a gran escala, se podríausar, por ejemplo, el arco de circunferencia mínimo entre _s_ y _t_.

### Optimalidad

La búsqueda con heurísticas no asegura optimalidad y es tan buena como lo sea la estimación de h sobre la distancia real del camino. Por ejemplo, en una manzana de Manhattan, si bien la distancia real entre dos esquinas es la diagonal que cruza la manzana (distancia euclídea), la distancia que debemos estimar es la que efectivamente costará llegar de una esquina a la otra, y esta tendrá que ser dando la vuelta a la manzana. Entonces es importante tener en cuenta que **la distancia estimada es la del camino en el grafo**, no la _distancia física_ si la hubiera.

Si la distancia estimada fuera _exactamente igual_ a la distancia real en el grafo, entonces recorreríamos primero el camino mínimo y obtendríamos una resolución óptima.

## Dijkstra

Dado un Grafo G y un vértice v del mismo, el algoritmo calcula la distancia de v a todos los otros vértices de G. Opcionalmente, para calcular el camino mínimo entre dos vértices u y v, se puede utilizar Dijkstra hasta que se llegue a calcular la distancia a u y se lo detiene ahí.

### Optimalidad

Al igual que BFS para caminos mínimos, se basa en que en todo momento, si se desencola un elemento, se asegura que se llegó a él con el menor costo posible. Para esto se utiliza una cola de prioridad, ordenada por el costo total en llegar hasta cada vértice. De este modo nos aseguramos que al visitar un vértice (desencolarlo) se está llegando a él con el menor costo posible (si hubiese un costo menor, ya se lo habría visitado antes). Así como BFS aseguraba que primero se visitaran todos los elementos de nivel 1, luego los de nivel 2, etc, Dijkstra asegura que siempre se visitarán los elementos de menor distancia a _s_ antes de los de mayor distancia.

Entonces la prioridad se calcula: `f(v) = d(s,v)`, donde _d(s,v)_ se calcula vértice a vértice incrementalmente.

Si se encuentra un camino alternativo a un vértice con costo menor, se lo agrega a la cola otra vez, con su nueva prioridad, con lo cual la alternativa más corta será la primera en ser visitada. Esto puede verse como una "actualización de prioridad".

A su vez, nunca ocurrirá que encontremos un camino alternativo más corto a un vértice ya visitado, ya que si así fuera, el subcamino hacia su padre nuevo habría sido visitado antes que él y habría sido agregado con esa prioridad antes de ser visitado.

Estos puntos, teniendo en cuenta que **los pesos son positivos**, aseguran optimalidad. Si hubiera pesos negativos, este algoritmo ya no sirve, porque bien podría ocurrir que se encuentre un camino que superaba al anterior en peso, y que al final tenía una arista que compensaba.

## A*

A* es una mejora de Dijkstra, utilizando heurísticas. Así como Dijsktra minimiza la distancia total hasta un vértice, A* minimiza la distancia de _s_ hasta ese vértice sumada a la distancia estimada de ese vértice a _t_ (la heurística) y ese es su criterio para el orden en la cola de prioridad. Numéricamente la prioridad `f(v) = d(s,v) + h(v,t)`.

De este modo, lo minimizado tiene en cuenta lo ocurrido y la estimación de lo que va a ocurrir, lo cual permite una decisión más informada que Dijkstra.

### Optimalidad

Para que se mantenga la optimalidad que brindaba Dijkstra, se debe cumplir que la heurística sea **admisible**, es decir que nunca sobreestime la distancia faltante. Numéricamente `h(v,t) <= d(v,t)`.

Por este motivo se suele tomar la estrategia de _problema relajado_ para el diseño de heurísticas. Esta estrategia consiste en simplificar el problema, para asegurarse de que la estimación subestime a la distancia. En un laberinto, por ejemplo, utilizar la distancia Manhattan entre dos puntos consiste en la suposición de que no hay paredes. De esta manera, la distancia estimada siempre será menor a la real, donde habrá obstáculos, y por lo tanto, será admisible.

`TODO: explicar por qué una heurística admisible permite optimalidad.`

### Eficiencia

Por otro lado, cuanto más se acerque una heurística admisible a la verdadera distancia, las elecciones que se tomen primero serán más probablemente las del camino óptimo y por lo tanto se llegará antes al destinto _t_.

Por este motivo, en el problema del laberinto, si bien la distancia euclídea es admisible (supone que no hay paredes y que uno se puede mover en cualquier dirección), pero subestimará aún más a la distancia y por lo tanto es probablemente menos eficiente que la distancia Manhattan.
