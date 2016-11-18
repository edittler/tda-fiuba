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

La importancia reside en que en cada paso se aumenta $v(f)$ en $b$ (que es mayor a 0), y sabemos que $v(f)$ está acotado, con lo cual **sabemos que el algoritmo termina**. Además, al terminar, hay un corte natural $(A,B)$ donde $A$ es el conjunto de todos los nodos alcanzables por $s$ y $B$ todo el resto. Como la ejecución termina cuando ya no hay caminos $s-t$, sabemos que la capacidad residual de las aristas entre $A$ y $B$ es nula. Entonces, la capacidad de ese corte está saturada hacia adelante (si no, habría forward edges) y no hay flujo de $B$ hacia $A$ (si no, habría backward edges de A a B). De este modo, nos aseguramos de que ese corte está saturado, mostrando que se realiza la desigualdad de capacidad y valor de flujo, y **demostrando Max-Flow Min-Cut** y simultáneamente que **el algoritmo efectivamente obtiene el Máximo flujo**.

Una vez finalizada la ejecución de Ford-Fulkerson, lo único necesario para encontrar el corte mínimo es hacer una búsqueda como BFS para encontrar los nodos alcanzables por $t$.

## Problema de Selección de Proyectos

### Problema
El problema en análisis tiene como objetivo maximizar las ganancias del Ing. F.B. Su empresa tiene:

- Un conjunto $P = \{P_1, P_2, \dotsc , P_m\}$ de proyectos posibles para tomar. Cada proyecto $P_i$ llevado a cabo provee una ganancia $g_i$ a la empresa.
- Un conjunto $A = \{A_1, A_2, \dotsc , A_n\}$ de áreas de investigación posibles a tomar. Cada área $A_k$ investigada conlleva un costo $a_k$ de inversión para la empresa.
- Cada proyecto requiere para ser ejecutado que se hayan investigado un cierto conjunto de áreas $R_{i} \subseteq A$ para poder ser efectuados.

El objetivo es elegir los proyectos (y por lo tanto también las áreas de investigación) adecuados para maximizar la ganancia del Ingeniero.

### Modelo de Red

Para este modelo creamos la siguiente red de flujo:

- El nodo $s$ simbolizará las ganancias. Por lo tanto, $s$ apuntará a los proyectos. Como en redes de flujo no se utilizan los valores de los nodos, utilizaremos las capacidades de estas aristas, dándoles el valor $g_i$.
- El nodo $t$ simbolizará las inversiones, con lo cual apuntará a las áreas de investigación. En este caso, las capacidades serán los costos $a_k$.
- Entre requerimientos y proyectos habrá aristas de dependencia: una arista $(i,j)$ donde $i$ es un proyecto y $j$ es un requerimiento simboliza que $i$ necesita de $j$ para poder llevarse a cabo. Las capacidades de aquellas serán tratadas más adelante.

Esto da grafos como el siguiente: **(DIBUJAR IMAGEN)**

La idea de este modelo es utilizar el algoritmo de Ford-Fulkerson para obtener un corte mínimo de forma tal que el conjunto alcanzable por $s$ sea el conjunto de proyectos a tomar, con sus áreas correspondientes.

### Compatibilidad

Si bien este sentido de dependencias es poco intuitivo (uno tendería a decir que $(i,j)$ simboliza que $j$ depende de $i$), este modelo tiene un beneficio grande, que consiste en la facilidad de implementar la satisfacción de dependencias.

Para asegurarnos de que el corte final $(A,B)$ sea compatible necesitamos que no haya ninguna arista saliente de A, ya que de haberla, significaría que hemos seleccionado un proyecto sin pagar el costo de investigar una de sus dependencias. Con este fin haremos que las aristas de dependencia tengan **capacidad infinita**.

Sabemos que el flujo está acotado aunque sea por la suma de las capacidades salientes de $s$:

\begin{equation}
v(f) \le \sum_{i \textrm{out} s} c_e = C
\end{equation}

Esto se debe a que $(\{s\}, G - \{s\})$ es un corte válido, y como tal, su capacidad acota al flujo máximo. Como el corte encontrado por el algoritmo es el de mínima capacidad, $c(A,B)$ estará acotada superiormente por $C$. De este modo entonces nos aseguramos que ninguna de esas aristas de capacidad infinita puede cruzar el corte, ya que si así fuera, la capacidad $c(A,B)$ superaría la cota que hallamos previamente.

### Optimalidad

Para comprobar que el córte mínimo es efectivamente el que buscamos, necesitamos ver qué valor tiene la capacidad de un corte. Con este fin resulta útil recordar que queremos maximizar la ganancia $G(A)$, que puede ser escrita de la siguiente manera:

\begin{equation}
    G(A) = \sum_{i/P_i \in A} g_i - \sum_{k / A_k \in A} a_k
\end{equation}

Por otro lado, a la capacidad del corte contribuyen las aristas de las áreas investigadas y las de proyectos no tomados (**IMAGEN**), con lo cual puede ser escrita de la siguiente:

\begin{equation}
    c(A,B) = \sum_{k / A_k \in A} a_k + \sum_{i / P_i \notin A} g_i = \sum_{k / A_k \in A} a_k + C - \sum_{i / P_i \in A} g_i = C - G(A)
\end{equation}

De este modo, ya que C es constante, vemos que minimizar el corte es igual a maximizar la ganancia, con lo cual este modelo resuelve el problema planteado.

\newpage

# Referencias
