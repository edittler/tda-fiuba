\newpage

# Flujo de redes

## Objetivo

Esta sección del trabajo tiene como objetivo la resolución del problema de Selección de Proyectos mediante su modelado como una red de flujo y la aplicación del algoritmo de Ford Fulkerson para maximizar la ganancia esperada.

## Introducción Teórica

Los problemas de flujo de redes parten de un grafo G = (V,E) con las siguientes características:

- G es dirigido.
- Hay un nodo $s$ (fuente/origen) que solo tiene aristas salientes.
- Hay un nodo $t$ (sumidero/destino) que solo tiene aristas entrantes.
- Cada arista $e \in E$ tiene una _capacidad_ a la que denominaremos $c_e$.

Por cada arista puede pasar una cantidad determinada de flujo. Esta es una función $f(e)$ aplicable a las aristas, con dos condiciones:

- Capacidad: $f(e) \le c_e$.
- Conservación: el flujo entrante total (entre todas las aristas) debe ser el mismo que el total saliente: $\sum_{e \textrm{in} v} f(e) = \sum_{e \textrm{out} v} f(e)$.

Este tipo de problemas, si bien tiene aplicaciones directas como redes de transporte de vehículos, de flujo, de comunicaciones y muchas otras directas, también puede utilizarse como modelo para problemas complejos que no son intuitivamente comparables. Un problema de este tipo es el tratado en este trabajo, que es el de _selección de proyectos_.

Por otro lado, también es de interés definir un _corte_ $(A,B)$ de la red como una partición de G en dos conjuntos tales que $s \in A$ y $t \in B$. La _capacidad de ese corte_ es la suma de las capacidades que lo cruzan: $c(A,B) = \sum_{e \textrm{out} A} c_e$.

En general, este modelo deviene en problemas de optimización, que son el de _maximización de flujo_ y el de _búsqueda de mínimo corte_. En el primer caso, se busca maximizar el _valor del flujo_ $v(f)$ definido como el flujo total saliente de $s$. En el segundo caso se busca un corte tal que su capacidad sea la mínima.

### Max-Flow, Min-Cut

El teorema de máximo flujo, mínimo corte muestra que el máximo flujo corresponde a la capacidad del mínimo corte. Este teorema se basa en la importante propiedad de que la capacidad de cualquier corte en una red es cota superior del valor del flujo.

Una demostración común, como la encontrada en el capítulo 7 del Kleinberg-Tardos **(CITAR)** acude a mostrar la situación final del algoritmo de Ford Fulkerson para maximización del flujo.

### Algoritmo de Ford Fulkerson

Este algoritmo, que será el utilizado en el trabajo, trabaja con el _Grafo Residual_ $G_f$ de la red, con las siguientes características:

- Una arista $e \in E(G)$ tal que $f(e) < c_e$ produce una _arista residual hacia adelante_ (foreward edge) $e' \in E(G_f)$ tal que $c_{e'} = c_e - f(e)$. Esto puede verse como lo que aún puede aumentarse de flujo en esa arista.
- Una arista $e \in E(G)$ tal que $f(e) > 0$ produce una _arista residual hacia atrás_ (backward edge) $e' \in E(G_f)$ tal que $c_{e'} = f(e)$. Esto puede verse como "lo que puede quitarse de flujo para ser asignado en otro lado".

La estrategia del algoritmo para maximizar el flujo se basa en buscar caminos de $s$ a $t$ en el grafo residual para aumentar el flujo en un cuello de botella (bottleneck) $b$ correspondiente a la mínima capacidad de ese camino. Finalizará cuando ya no haya caminos $s-t$ en $G_f$.

La importancia reside en que en cada paso se aumenta $v(f)$ en $b$ (que es mayor a 0), y sabemos que $v(f)$ está acotado, con lo cual **sabemos que el algoritmo termina**. Además, al terminar, hay un corte natural $(A,B)$ donde $A$ es el conjunto de todos los nodos alcanzables por $s$ y $B$ todo el resto. Como la ejecución termina cuando ya no hay caminos $s-t$, sabemos que la capacidad residual de las aristas entre $A$ y $B$ es nula. Entonces, la capacidad de ese corte está saturada hacia adelante (si no, habría forward edges) y no hay flujo de $B$ hacia $A$ (si no, habría backward edges de A a B). De este modo, nos aseguramos de que ese corte está saturado, mostrando que se realiza la desigualdad de capacidad y valor de flujo, y **demostrando Max-Flow Min-Cut**.

## Problema de Selección de Proyectos

\newpage

# Referencias
