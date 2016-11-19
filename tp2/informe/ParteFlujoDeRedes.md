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

La estrategia del algoritmo para maximizar el flujo se basa en buscar caminos de $s$ a $t$ en el grafo residual para aumentar el flujo en un cuello de botella (bottleneck) $b$ correspondiente a la mínima capacidad de ese camino. Finalizará cuando ya no haya caminos $s$-$t$ en $G_f$.

La importancia reside en que en cada paso se aumenta $v(f)$ en $b$ (que es mayor a 0), y sabemos que $v(f)$ está acotado, con lo cual **sabemos que el algoritmo termina**. Además, al terminar, hay un corte natural $(A,B)$ donde $A$ es el conjunto de todos los nodos alcanzables por $s$ y $B$ todo el resto. Como la ejecución termina cuando ya no hay caminos $s$-$t$, sabemos que la capacidad residual de las aristas entre $A$ y $B$ es nula. Entonces, la capacidad de ese corte está saturada hacia adelante (si no, habría forward edges) y no hay flujo de $B$ hacia $A$ (si no, habría backward edges de A a B). De este modo, nos aseguramos de que ese corte está saturado, mostrando que se realiza la desigualdad de capacidad y valor de flujo, y **demostrando Max-Flow Min-Cut** y simultáneamente que **el algoritmo efectivamente obtiene el Máximo flujo**.

Una vez finalizada la ejecución de Ford-Fulkerson, lo único necesario para encontrar el corte mínimo es hacer una búsqueda como BFS para encontrar los nodos alcanzables por $t$.

## Problema de Selección de Proyectos

### Problema
El problema en análisis tiene como objetivo maximizar las ganancias del Ing. F.B. Su empresa tiene:

- Un conjunto $P = \{P_1, P_2, \dotsc , P_m\}$ de proyectos posibles para tomar. Cada proyecto $P_i$ llevado a cabo provee una ganancia $g_i$ a la empresa.
- Un conjunto $A = \{A_1, A_2, \dotsc , A_n\}$ de áreas de investigación posibles a tomar. Cada área $A_k$ investigada conlleva un costo $a_k$ de inversión para la empresa.
- Cada proyecto requiere que se haya investigado un cierto conjunto de áreas $R_{i} \subseteq A$ para poder ser ejecutado.

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

### Detalles de implementación

En términos generales, la solución fue implementada con una clase ProjectSelection correspondiente al problema, que utiliza a una clase Flow, que modela la red de flujo y es capaz de aplicar el algoritmo de Ford Fulkerson.

Ya que el grafo de la red y el residual comparten una gran cantidad de información, en lugar de tratarlos por separado utilizamos únicamente al grafo principal, añadiendo las backward edges con capacidad 0 al agregar cada arista.

El uso del grafo residual se da sobre todo en la búsqueda de caminos a aumentar y la capacidad residual se calcula en el momento en la función $e_transitable$ para ver si un camino residual puede pasar por esa arista dado el flujo en ese momento:

```python
def e_transitable(g, e, flow):
    return (e.is_backwards and e.capacity > 0) \
        or ((not e.is_backwards) and flow[e] < e.capacity)
```

Como fue explicado para arriba, si es una _foreward edge_, la capacidad residual es positiva cuando la capacidad no está saturada y por lo tanto puede pasar más flujo por allí. Para una _backward edge_ , la capacidad residual es positiva cuando hay flujo en el sentido contrario que puede ser reducido para usar en otro lado. Estos son los casos en donde un camino $s$-$t$ puede pasar por allí.

La lógica principal del algoritmo de Ford_Fulkerson está implementada del siguiente modo:

```python
def get_max_flow(g, source, target):
    flow = g.get_empty_flow()
    path = g.flow_path(source, target, flow)

    while path != None:
        b = g.bottleneck(path, flow)
        for edge in path:
            flow[edge] -= b if edge.is_backwards else -b
        path = g.flow_path(source, target, flow)

    return flow
```

Como las capacidades residuales son calculadas en el momento y en base al flujo, no hace falta "actualizar" al grafo residual después de un aumento.

La **búsqueda de caminos** entre s y t fue implementada con **DFS**, ya que teniendo en cuenta la estructura del grafo, un BFS produciría siempre recorrer todos los vértices: como se recorre por distancias al origen, se recorrerán siempre primero todos los proyecots (d = 1), luego todas las áreas de investigación (d=3) y recién al final se llegará a $t$ (d = 3). Con DFS el peor caso será el de recorrer todos los vértices, mientras que es posible que llegue en visitando un proyecto y un área.

El **Mínimo corte** también fue implementado con un DFS recursivo, pero esto ocurrió por comodidad y no por eficiencia, ya que tanto en ese caso como en BFS buscar el mínimo corte implica recorrer todos los nodos alcanzables por $s$.

### Complejidad

Para calcular la complejidad es necesario acotar la cantidad de iteraciones que tendrá el algoritmo. Como sabemos que el flujo aumentará en una cantidad positiva en cada iteración y sabemos que $v(f) < C$, entonces a lo sumo habrá $C$ iteraciones.

Cada una de las iteraciones, a su vez, consiste principalmente en la búsqueda de un camino, cuyo peor caso recorre todo los nodos en orden $O(|V| + |E|) = O(n+m+2r)$, siendo $r = \sum_{i=1}^{m}|Ri|$ (la cantidad de aristas). En este orden se ve la cantidad de aristas dos veces por la generación de backward edges, aunque esto no afecta realmente al orden.

Buscar el bottleneck se hace dentro del camino encontrado, que es un camino simple, con lo cual es como máximo $O(n+m)$. Lo mismo para el aumento del camino.

Finalmente, todo el orden total es de $O(C(n+m+r))$. Esto significa que es lineal en el n, m y r siempre y cuando se mantenga $C$.

Sin embargo, no sería lógico decir aquello, ya que $C$ no es independiente de $n$ o de $m$. Para obtener esa cota del valor del flujo puede tomarse el corte tanto en $(\{s\}, G-\{s\})$ o en $(G-\{t\},\{t\})$ y la mínima capacidad entre ambos cortes sería una cota. Por eso podemos expresar la parte de C como $\sum_{i=1}^m g_i + \sum_{k=1}^n a_k$, que también depende de m y n.

Para simplificar las cuentas suponemos (con pérdida de generalidad) que $g_i = a_k = 1 \forall i \forall k$. En este caso relajado podríamos fijar para el problema $\Omega((m + n)(m+n+r))$, lo cual es **cuadrático en $m$ y $n$, y lineal en $r$ (manteniendo las otras entradas fijas)**. El $O$ real será más grande y dependerá de las capcacidades (ganancias y pérdidas).

Esta fuerte dependencia de los costos se debe a que no se implementó un mecanismo inteligente de elección de caminos, permitiendo que el bottleneck pueda ser tan pequeño como 1. Teniendo en cuenta que lo ideal sería aumentar primero los paths de mayor bottleneck, hay algoritmos mejorados como el _Scaling Max Flow_, cuya complejidad resulta de $O((n+m+r)log_2(C))$, lo cual baja el orden de los cuadráticos a $O(xlogx)$. **(CITAR)**

\newpage

# Referencias
