\newpage

# Clases de Complejidad

## Objetivo

El objetivo de esta sección del trabajo es analizar 4 problemas, sus posibles soluciones y su clasificación según clase de complejidad.

## Introducción Teórica

La clasificación de clases de complejidad de los problemas surge de la necesidad de comparar problemas para los cuales no se conoce una solución eficiente (polinomial), pero no se ha demostrado que no la tienen.

### Reducciones

Para comparar la dificultad de dos problemas X e Y tomamos como criterio la posibilidad de usar a uno para resolver al otro. Si se tiene un algoritmo que resuelve X, y en base a ese resultado podemos obtener una solución para el problema Y en tiempo polinómico, entonces decimos que:

- "Y es polinomialmente reducible a X" ($Y\leqslant_pX$)

- "X es tan difícil como Y", ya que resolver X asegura que podemos resolver Y, pero no se cumple la inversa. No nos referimos estrictamente al tiempo de ejecución.

Se dice por otro lado que dos problemas son _polinómicamente equivalente_ ($Y \equiv_p X$) cuando cualquiera puede usarse para resolver al otro: $Y\leqslant_pX$ y $X\leqslant_pY$.

### Problemas de decisión

Identificamos a un problema de decisión por las siguientes componentes:

- Entrada: string $s \in S$ (siendo $S$ el espacio de strings posibles).
- Salida: _si_ o _no_ (string aceptada o rechazada).

Definimos entonces a un problema $X$ como el conjunto de strings que acepta.

Definimos a su vez a un algoritmo $A$ que resuelve a un problema $X$ como una función que toma inputs y devuelve si el problema acepta o no a esa string. Formalmente:

\begin{equation}
    A(s) = si \iff s \in X
\end{equation}

**REVISAR**

Nos son particularmente interesantes estos problemas porque la reducción de un problema de decisión $X$ a otro $Y$ consiste en transformar en tiempo polinómico la entrada de $X$ en una entrada de $Y$ de forma tal que la salida de $Y$ sea la esperada por $X$.

### Certificación

Llamamos _certificado_ a una cadena $t$ que aporta información sobre si una cadena de input $s$ será aceptada para un problema $X$. Por ejemplo, para un problema de decisión como "verificar si en un grafo hay ciclos", un posible certificado es un conjunto de vértices que supuestamente forman un ciclo. Es algo similar a una solución propuesta.

Dado un problema $X$, una entrada $s$ y un certificado $t$, llamamos _certificador_ a una función B que toma certificados y evidencia con ellos que $s \in X$. Para el ejemplo anterior, un certificador tomaría el conjunto de vértices $t$ y la cadena $s$ (que serían los vértices del grafo) y verificaría que $t$ es efectivamente un ciclo. Formalmente:

\begin{equation}
    B(s,t) = si \iff t \textrm{ demuestra que } s \in X
\end{equation}

Es importante observar que el certificador no analiza la cadena en sí, sino que evalúa el certificado. Por lo tanto, su función es en realidad comprobar soluciones propuestas al problema, lo cual no necesariamente resuelve el problema en sí mismo. Por este motivo, muchas veces es más sencilla y rápida la acción de un certificador que la de un algoritmo de resolución de un problema.

Llamamos _certificador eficiente_ a uno que certifica en tiempo polinómico.

### P y NP

Son de nuestro interés dos clases de complejidad:

- P: clase que contiene a todos los problemas para los cuales existen algoritmos que los resuelven en tiempo polinómico. Si X es un problema, A un algoritmo y p es una función polinómica:

\begin{equation}
    P = \{X / \exists A \in O(p(|s|)) \textrm{ que lo resuelve}\}
\end{equation}

- NP: clase que contiene a todos los problemas certificables en tiempo polinómico. Si X es un problema y B un certificador:

\begin{equation}
    NP = \{X / \exists B \in O(p(|s|)) \textrm{ que lo certifica}\}
\end{equation}

Inmediatamente podemos observar que $P \subseteq NP$, ya que si un problema puede resolverse en tiempo polinómico, entonces para certificar soluciones propuestas puede usarse el mismo algoritmo polinómico de resolución, ignorando el certificado.

Adicionalmente, de la definición de reducciones podemos observar que:

- Si $Y \leqslant_p X$ y $X$ es resoluble en tiempo polinómico, entonces $Y$ también. $X \in P \Rightarrow Y \in P$.
- Vale la recíproca: $Y\leqslant_pX \land Y \notin P \Rightarrow X \notin P$.

### NP-Completo

Además, existe un subconjunto de NP que cumplen con la característica de ser más difíciles que cualquier otro prolema en NP. A esta subclase la denominamos NP-completo. Visto de otro modo, que un problema pertenezca a aquella clase asegura que si se tiene un algoritmo para resolverlo, entonces es posible utilizarlo para transformarlo en tiempo polinómico a cualquier problema de NP.

Entonces un problema $X$ perteneciente a esta clase cumple con dos características:

1. $X \in NP$
2. $\forall Y \in NP: Y \leqslant_p X$

Es importante que se cumplan ambas, ya que los problemas que cumplen la segunda condición son llamados NP-hard independientemente de si son o no NP.

**Quizás se puede plantear la "situación de hoy en día"**

## Determinar la clase de complejidad de un problema.

Para muchas aplicaciones es de interés determinar si un problema pertenece a alguna de las tres clases anteriores. En cada caso, el método utilizado será:

- P: encontrar una solución polinomial.
- NP: encontrar un certificador polinomial.
- NP-completo: reducir un problema NP-completo conocido al problema en cuestión. Además habrá que probar independientemente que es NP.

A continuación se presentan algunos problemas conocidos que serán de utilidad.

### SAT y 3-SAT

El problema SAT (satisfacibilidad booleana) consiste en los siguientes elementos:

- Un conjunto $X = \{x_1, x_2, ..., x_n\}$ de variables booleanas.
- $k$ condiciones $C_i$ a satisfacer, cada una con $l$ términos unidos por disyunciones ($\lor$).
- Cada término $t_i$ en una condición es una de las variables booleanas de $X$ o su negación.

El problema se trata de decidir si existe una asignación de las variables $\nu: X \to \{0,1\}$ (mapeo concreto de cada variable a 0 o 1) que satisfaga simultáneamente todas las condiciones. Es decir, $\nu$ tal que $\bigwedge_{i=1}^{k} C_i = 1$.

El 3-SAT es un caso particular de este, donde $|C_i| = 3 \quad \forall i$. Es demostrable (**CITAR**) que es polinómicamente equivalente a SAT.

La importancia de este problema reside en que el Teorema de Cook (**CITAR?**) demuestra que es NP-Completo, modelando con una tabla la computación completa de cualquier máquina de Turing y expresándo los valores de la tabla y sus relaciones con variables booleanas. (**MEJORAR**). De este modo se reduce cualquier Máquina de Turing a un problema SAT.

Mostrar que SAT y 3-SAT son NP, por otro lado es sencillo. Un certificado es una asignación propuesta. Para verificarlo, solo será necesario ver para cada condición que esa asignación la hace verdadera. La certificación, por lo tanto, es lineal en el tamaño de la entrada, que es la cantidad total de términos ($\sum_{i=1}^{k} |C_i|$).

### Independent Set (IS)

Un conjunto de vértices de un grafo $G = (V,E)$ es _independiente_ si no contiene ningún par de vértices adyascentes.

Mientras que encontrar un IS de tamaño pequeño es trivial (cualquier vértice es un IS de tamaño 1), encontrar instancias grandes es costoso. Por este motivo, el problema de decisión asociado consiste en decidir si hay un IS de tamaño al menos $k$ para un $k$ dado.

### Vertex Cover (VC)

Se dice que un conjunto de vértices _cubre_ al grafo cuando todas las aristas tienen al menos uno de sus extremos en el conjunto.

Al revés del problema anterior, encontrar un VC de tamaño grande es trivial, ya que por ejemplo el conjunto $V$ completo es un VC. Sin embargo, encontrar instancias pequeñas no es sencillo. Por lo tanto, el problema de decisión asociado consiste en decidir si existe un VC de tamaño a lo sumo $k$ para un $k$ dado.

### Relación entre los problemas

**Teorema**: VC $\equiv_p$ IS

**Demostración**: queremos probar que si $S$ es un IS en $G$, entonces $V-S$ es un VC en $G$.

1. $S$ es IS $\Rightarrow$ $V - S$ es VC:

    Como dijimos antes, $V$ es un VC. Si quitamos uno a uno elementos de $S$ a $V$, sabemos que en ningún caso se quitarán ambos extremos de una arista. Si así fuera, dos de los elementos quitados estarían unidos y $S$ no sería un IS.

2. $V - S$ es VC $\Rightarrow$ $S$ es IS:

    Por contradicción: Si $S$ no fuera un IS, entonces podríamos afirmar que existen dos vértices $v_1,v_2 \in S$ tal que $v_1$ y $v_2$ están conectados. Entonces, $V - S$ no contendrá la unión entre esos dos vértices y por lo tanto no será un VC, contradiciendo la hipótesis.

Entonces se ve que con resolver IS para tamaño $k$, se resuelve VC para tamaño $n-k$ y viceversa. Entonces, la única transformación requerida entre un problema y otro es la cuenta $n-k$, lo cual es $O(1)$, lo cual demuestra que son polinomialmente equivalentes.

**Teorema**: 3-SAT $\leqslant_p$ IS

**Demostración**: queremos probar que se puede modelar el problema de 3-SAT como un problema de conjuntos independientes. Creamos el siguiente modelo:

- Para cada una de las $k$ condiciones creamos tres vértices, uno por cada término. Tendremos entonces, $|V| = 3k$
- Para modelar las incompatibilidades entre los términos de distintas condiciones ($x_i$ en una y $~x_i$ en otra), unimos con aristas estos casos.
- Como es suficiente satisfacer un término de cada condición para que la asignación satisfaga a todas, entonces unimos los 3 vértices de cada condición entre sí, formando triángulos. Esto no significa que no es posible satisfacer más términos, solo que hacerlo complica las incompatibilidades y no es necesario para demostrar que existe una asignación satisfactoria.

De este modo, si encontramos un conjunto independiente de al menos $k$ vértices, nos aseguramos de que elegimos al menos $k$ términos, uno de cada condición, sin que haya incompatibilidades. Este conjunto da como resultado, justamente, una asignación satisfactoria.

**Corolario**: 3-SAT $\equiv_p$ SAT $\leqslant_p$ IS $\equiv_p$ VC

Por este motivo, tanto IS como VC son NP-completos y podemos tratar de reducir esos problemas a los que querramos demostrar que también lo son.

## Problema de Ciclos Negativos (CN)
_Se tiene un grafo dirigido y pesado G, cuyas aristas tienen pesos que pueden ser negativos. Se pide devolver si el grafo tiene algún ciclo con peso negativo._

El algoritmo de Bellman-Ford de búsqueda de caminos mínimos en grafos tiene la característica de ser óptimo con aristas de pesos negativos (cuando Dijkstra no lo es) y la ventaja de detectar, al final de su ejecución, ciclos negativos.

Aquel consiste, en cada paso, en recorrer todas las aristas $(u,v) \in E$ viendo si la distancia actual al vértice $v$ es mejorable si se llega desde $u$. Esto puede verse en pseudocódigo como:

```python
for e in edges:
    if(distance[e.dst] > distance[e.src] + e.weight):
        distance[e.dst] = distance[e.src] + e.weight
        parent[e.dst] = e.src
```

**Si no hay ciclos negativos**, en cada uno de estos pasos el algoritmo deja en su valor óptimo la distancia a cada vértice a distancia sin peso más cercano. Es decir, en el primer paso, los vértices adyascentes al origen $s$ quedarán con su menor distancia. En el segundo, los adyascentes a esos (distancia sin peso 2 a $s$) quedarán minimizados. Por este motivo, como el camino mínimo no puede tener más de $|V| - 1$ aristas (no puede recorrer más de una vez un vértice o no sería óptimo) y por lo tanto al terminarse $|V|-1$ pasos de los anteriores puede asegurarse que se llegó a destino con el mejor camino posible.

Por otro lado, **en caso de haber ciclos negativos**, estos son mejorables infinitamente (se los puede seguir recorriendo sin fin y seguir bajando su peso total). De este modo, si luego de $|V|-1$ iteraciones todavía hay una arista mejorable, podemos asegurar que el grafo tiene ciclos negativos, que era el objetivo de este problema.

Entonces, el problema se reduce a aplicar el algoritmo de Bellman-Ford y responder 1 si el algoritmo encontró ciclos negativos.

Esto no significa necesariamente que sea el algoritmo más eficiente para resolver este problema, pero a los fines de este trabajo es suficiente, dado que el algoritmo es claramente polinómico, con complejidad $O(|E||V|)$. Concluimos entonces que CN $\in$ P.

## Ciclos nulos
