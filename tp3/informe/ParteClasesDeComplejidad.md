\newpage

# Clases de Complejidad

## Introducción Teórica

La clasificación de clases de complejidad de los problemas surge de la necesidad de comparar problemas para los cuales no se conoce una solución eficiente (polinomial), pero no se ha demostrado que no la tienen.

### Reducciones

Para comparar la dificultad de dos problemas X e Y tomamos como criterio la posibilidad de usar a uno para resolver al otro. Si se tiene un algoritmo que resuelve X, y en base a ese resultado podemos obtener una solución para el problema Y en tiempo polinómico, entonces decimos que:

- "Y es polinomialmente reducible a X" ($Y\leqslant_pX$)

- "X es tan difícil como Y", ya que resolver X asegura que podemos resolver Y, pero no se cumple la inversa. No nos referimos estrictamente al tiempo de ejecución.

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

### Certificación

Llamamos _certificado_ a una cadena $t$ que aporta información sobre si una cadena de input $s$ será aceptada para un problema $X$. Por ejemplo, para un problema de decisión como "verificar si en un grafo hay ciclos", un posible certificado es un conjunto de vértices que supuestamente forman un ciclo. Es algo similar a una solución propuesta.

Dado un problema $X$, una entrada $s$ y un certificado $t$, llamamos _certificador_ a una función B que toma certificados y evidencia con ellos que $s \in X$. Para el ejemplo anterior, un certificador tomaría el conjunto de vértices $t$ y la cadena $s$ (que serían los vértices del grafo) y verificaría que $t$ es efectivamente un ciclo. Formalmente:

\begin{equation}
    B(s,t) = si \iff t \textrm{ certifica que } s \in X
\end{equation}

Es importante observar que el certificador no analiza la cadena en sí, sino que evalúa el certificado. Por lo tanto, su función es en realidad comprobar soluciones propuestas al problema, lo cual no necesariamente resuelve el problema en sí mismo. Por este motivo, muchas veces es más sencilla y rápida la acción de un certificador que la de un algoritmo de resolución de un problema.

Llamamos _certificador eficiente_ a uno que certifica en tiempo polinómico.

### $P$ y $NP$

Son de nuestro interés dos clases de complejidad:

- $P$: clase que contiene a todos los problemas para los cuales existen algoritmos que los resuelven en tiempo polinómico. Si X es un problema, A un algoritmo y p es una función polinómica:

\begin{equation}
    P = \{X / \exists A \in O(p(|s|)) \textrm{ que lo resuelve}\}
\end{equation}

- $NP$: clase que contiene a todos los problemas certificables en tiempo polinómico. Si X es un problema y B un certificador:

\begin{equation}
    NP = \{X / \exists B \in O(p(|s|)) \textrm{ que lo certifica}\}
\end{equation}

Inmediatamente podemos observar que $P \subseteq NP$, ya que si un problema puede resolverse en tiempo polinómico, entonces para certificar soluciones propuestas puede usarse el mismo algoritmo polinómico de resolución, ignorando el certificado.

**Quizás se puede plantear la "situación de hoy en día"**

Adicionalmente, de la definición de reducciones podemos observar que:

- Si $Y \leqslant_p X$ y $X$ es resoluble en tiempo polinómico, entonces $Y$ también. $X \in P \Rightarrow Y \in P$.
- Vale la recíproca: $Y\leqslant_pX \land Y \notin P \Rightarrow X \notin P$.

## Determinar la clase de complejidad de un problema.
