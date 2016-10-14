\newpage

# Estadístico de orden k

## Brute Force

### Complejidad

A simple vista, calcular si un elemento es o no, por ejemplo, el
4\textsuperscript{to} elemento más pequeño, es $O(n)$, ya que se fija cuántos
son menores a él entre todos los demás elementos del conjunto.
Como lo hacemos potencialmente para todos los elementos (ya que, en el peor caso,
el _k-ésimo_ elemento puede ser el último), este método es $O(n^2)$.

### Mejor caso

Cuando el _k-ésimo_ elemento es el primero en la lista.

Ejemplo:

$k = 4$

$l = [4,15,2,1,0,14,6,11,8,9,3,13,12,7,5,10]$

$O(n)$: En este caso, al comenzar a comparar desde el primer elemento, encontramos el 'k' requerido en la primer iteración.

### Peor caso

Cuando el _k-ésimo_ elemento es el último en la lista.

Ejemplo:

$k = 4$

$l = [10,15,2,1,0,14,6,11,8,9,3,13,12,7,5,4]$

$O(n^2)$: En este caso, encontramos el 'k' elegido en la última iteración (luego de recorrer todo el conjunto para cada uno de los elementos anteriores a 4).


## Order and Select

### Complejidad

Para el presente trabajo práctico se utilizó el Timsort (algoritmo de
ordenamiento usado por `Python`), que es $O(n \log n)$ en el peor caso y $O(n)$
en el mejor caso.
Una vez que se ordena el conjunto, se toma el elemento $k$ de la lista en $O(1)$.
Por lo tanto, este algoritmo sería $O(n \log n)$.

### Mejor caso

El mejor caso del Timsort se da cuando la entrada ya está ordenada (ya sea en
forma ascendente o descendente). Luego, encontrar el k-esimo elemento es constante.

Ejemplo:

$k = cualquiera$

$l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]$

$O(n)$

### Peor caso

Lamentablemente no pudimos encontrar un ejemplo claro y concreto para demostrar el peor caso del Timsort

$O(n \log n)$


## k-selecciones

### Complejidad

En la selección se analizan los $n$ elementos de la lista y se pone en primer
lugar al más pequeño.
Luego, sobre los $n-1$ restantes se repite el proceso, luego sobre $n-2$ y así
$k$ veces en total.
Cada una de las selecciones, sobre una lista de $n$ elementos, es $O(n)$ (debe
recorrerlos todos para ver el mínimo).

Este algoritmo tiene $k$ selecciones, con lo cual es entonces $O(k*n)$ (tanto
$k$ como $n$ son parte de la entrada, ninguna es constante).
Ya que $k < n$, esto seguramente sea menor a $O(n^2)$.
Salvo que $k$ sea menor a $\log(n)$, este algoritmo es superado por el Order and
Select.


### Mejor caso

La complejidad del algoritmo depende de $k$, por lo que el mejor caso se da
cuando $k = 0$ (o 1, dependiendo dicha notación si se usa 0-based o no), donde
realiza la selección parcial 1 sola vez, y esto se da con cualquier entrada de
cualquier tamaño $n$.

$k = 0$

$l = [4,15,2,1,0,14,6,11,8,9,3,13,12,7,5,10]$

### Peor caso

Por el mismo argumento anterior, el peor caso se da cuando $k = n$, ya que debe
realizar las selecciones parciales de absolutamente todos los elementos del arreglo.

$k = 15$

$l = [4,15,2,1,0,14,6,11,8,9,3,13,12,7,5,10]$


## k-heapsort

### Complejidad

Un heapsort es un ordenamiento de selección, sólo que se usa un heap de mínimo
para obtener el mínimo en $O(\log n)$ en lugar de $O(n)$.
Si bien observar el mínimo de un heap es $O(1)$, como lo quitaremos debe hacerse
un upheap o float, que es $O(\log n)$.

Entonces, el heapsort consiste en dos etapas:

1. Heapify. Se reordena el array para que sea un heap. Esto es $O(n)$.
2. Las $n$ extracciones del mínimo $O(n \log n)$.

Por lo tanto, un heapsort normalmente es $O(n) + O(n \log n) = O(n \log n)$.

Aquí, al igual que con el k-selecciones, quitaremos los primeros $k$ elementos.
Por esto, aquí se hará el heapify, sucedido de $k$ extracciones del mínimo.
El orden sería $O(n + k \log n)$ con $k < n$.

### Mejor caso

Como en este caso se realiza el heapify sea cual sea la entrada (no importa el
tamaño), el mejor o peor caso se da dependiendo de la cantidad de extracciones
que deban hacerse. Es decir, depende de $k$.
El mejor caso se da cuando hay que hacer una sola extracción, es decir, cuando
$k = 0$

$l = [4,15,2,1,0,14,6,11,8,9,3,13,12,7,5,10]$

### Peor caso

Siguiendo el razonamiento anterior, el peor caso se da cuando $k = n-1$ ya que
hay que realizar $n$ extracciones.

$l = [4,15,2,1,0,14,6,11,8,9,3,13,12,7,5,10]$


## HeapSelect

### Complejidad

Este algoritmo consiste en lo siguiente:

1. Toma los primeros $k$ elementos de la lista y los convierte en un heap de
  máximo con heapify. Esto es $O(k)$.
2. Mantiene los $k$ mínimos en el heap. Para esto recorre cada elemento de la
  lista y, si es menor al máximo lo agrega al heap y quita el nuevo máximo.
  Si es mayor al máximo, no lo agrega. Para cada elemento cuesta $O(\log k)$
  con lo cual este paso completo es $O(n \log k)$.
3. Observamos la raíz del heap final (Máximo de los $k$ mínimos elementos) lo
  cual es $O(1)$.

El tiempo entonces es $O(k + n \log k + 1) = O(n \log k)$.

Esta función es rápida para $k$ pequeño. Si $k$ se acerca a $n$, termina siendo
más conveniente directamente ordenar la lista, ya que de todos modos tendremos
que ordenar en el 3er paso la mayor parte de los elementos en el paso 3.
Esta comparación de cuándo conviene cada una es justamente una comparación entre
este algoritmo y el Order and Select.

### Mejor caso

Siendo que el paso número 1 es indiferente sea cual sea la entrada, $n$ y $k$, y
que la observación del máximo elemento del heap es $O(1)$ siempre, resta
entender que para que se dé el mejor caso, nos conviene realizar la menor
cantidad de inserciones en el heap, a medida que recorremos la lista de $n - k$
elementos restantes en el paso número 2.

Por ende, el mejor caso se da cuando la entrada está parcialmente ordenada,
siendo los primeros $k$ elementos, ya los mínimos de toda la entrada (lo cual
equivaldría a decir que de los $n - k$ elementos restantes que se iteran en el
punto 2, ninguno se insertaría en el heap).

$k = 4$

$l = [4,3,2,1,0,14,6,11,8,9,15,13,12,7,5,10]$

Puede verse que los primeros $k = 4$ elementos (0-based) entrarían en el heap
inicial, y los restantes $n - k = 12$ no entrarían en el heap a medida que se
los itera (ya que ninguno es más pequeño que $4$, la raíz del heap que se genera
luego del punto 1.

Vale aclarar que existe otro mejor caso, el cual depende absolutamente de $k$ y
se da cuando $k = n-1$, es decir, cuando se quiere encontrar el máximo elemento
del conjunto.
Este caso equivale a un HeapSort (ya que hay que ordenar en un heap absolutamente
todos los elementos, el paso 2 no existiría, y leer de la raíz es constante),
por lo que también se da en $O(n)$

### Peor caso

Con el mismo razonamiento anterior, el peor caso se da cuando hay que realizar
absolutamente todas las inserciones al heap generado en el punto 1.
El caso se daría cuando, con un $k$ determinado, los primeros $k$ elementos son
los mayores del conjunto (no importa que este sub-conjunto esté ordenado), y
luego los restantes $n-k$ elementos estén ordenados en orden decreciente.

$k = 12$

$l = [4,12,7,5,10,14,6,11,8,9,15,13,3,2,1,0]$


## QuickSelect

### Complejidad

Se usa la lógica del Quicksort: se define un pivote y se ponen todos los
elementos mayores "a la derecha" y todos los menores "a la izquierda".
Según la posición p del pivote:

- Si $p == k$: se devuelve `l[p]`
- Si $p < k$: se hace QuickSelect sobre la parte derecha (`l[p+1..n]`)
- Si $p > k$: se hace QuickSelect sobre la parte izquierda(`l[0..p]`)

Esto entonces, en el caso óptimo de que el pivote siempre queda a la mitad tiene
un tiempo de $T(n) = T(n/2) + O(n)$ ($n$ es lo que tarda en poner todo en su
lado correspondiente del pivote).

Utilizando el Teorema Maestro, esto es $O(n)$.

Ahora bien, esto depende mucho de cómo se elige al pivote. Si se tiene una
elección de pivote mala para lo que deseamos buscar, es factible ir
particionando el arreglo de a 1 elemento, por lo que estaríamos en 
un caso de $O(n^2)$

### Mejor caso

Como dijimos, depende mucho de la elección del pivote. Si, por ejemplo, elegimos
el pivote que se encuentra en la primer posición del conjunto, se quiere buscar
el primer mínimo (k == 0 en 0-based) y, además, el conjunto está ordenado, 
entonces lo encontraremos en $O(n)$, ya que el primer pivote utilizado es el que
quiero devolver

$k = 0$

$l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]$

### Peor caso

Si por el contrario, y tomando como base el caso anterior, queremos el máximo
elemento (es decir, el n-esimo elemento más pequeño), pero siempre elegimos al
primer elemento como pivote y además el conjunto está ordenado en forma
ascendente, llegamos al peor caso (ir particionando el conjunto de a 1 elemento)

$k = 15$

$l = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]$


## Nota general sobre k

$k <= n$. Sería absurdo pedir algo como el $n + 1$ menor elemento.

Si $k == n$, entonces el $k$ mínimo es el máximo, y puede encontrarse en $O(n)$
más rápido que con cualquiera de los otros.
De hecho, todos los algoritmos antes descriptos pueden ser mejorados
sustancialmente con este razonamiento.
Si $k > n/2$, entonces el *k-mínimo* es el *n-k-máximo* y será más barato buscar
al *k-máximo* con el mismo algoritmo.


## Comparación de tiempos de ejecución

Visualizaremos los tiempos de ejecución de cada algoritmo, variando el tamaño de la entrada y obteniendo resultados para buscar los casos particulares $k = 1$, $k = n/2$ y $k = n$.

\newpage

### $k = 1$

\begin{figure}[H]
\centering
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_10_0.png}
  \caption{Con algoritmos exponenciales}
  \label{fig:k_one_with_exponential}
\end{subfigure}%
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_12_0.png}
  \caption{Sin algoritmos exponenciales}
  \label{fig:k_one_without_exponential}
\end{subfigure}
\caption{$k=1$, elementos desordenados}
\label{fig:k_1_desordenada}
\end{figure}

\begin{figure}[H]
\centering
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_18_0.png}
  \caption{Con algoritmos exponenciales}
  \label{fig:k_one_with_exponential}
\end{subfigure}%
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_20_0.png}
  \caption{Sin algoritmos exponenciales}
  \label{fig:k_one_without_exponential}
\end{subfigure}
\caption{$k=1$, elemento único}
\label{fig:k_1_elemento único}
\end{figure}

\begin{figure}[H]
\centering
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_22_0.png}
  \caption{Con algoritmos exponenciales}
  \label{fig:k_one_with_exponential}
\end{subfigure}%
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_24_0.png}
  \caption{Sin algoritmos exponenciales}
  \label{fig:k_one_without_exponential}
\end{subfigure}
\caption{$k=1$, elementos ordenados}
\label{fig:k_1_elementos_ordenados}
\end{figure}


### $k = n/2$

\begin{figure}[H]
\centering
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_10_1.png}
  \caption{Con algoritmos exponenciales}
  \label{fig:k_n2_with_exponential}
\end{subfigure}%
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_12_1.png}
  \caption{Sin algoritmos exponenciales}
  \label{fig:k_n2_without_exponential}
\end{subfigure}
\caption{$k=n/2$, elementos desordenados}
\label{fig:k_n2}
\end{figure}

\begin{figure}[H]
\centering
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_18_1.png}
  \caption{Con algoritmos exponenciales}
  \label{fig:k_n2_with_exponential}
\end{subfigure}%
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_20_1.png}
  \caption{Sin algoritmos exponenciales}
  \label{fig:k_n2_without_exponential}
\end{subfigure}
\caption{$k=n/2$, elemento único}
\label{fig:k_n2}
\end{figure}

\begin{figure}[H]
\centering
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_22_1.png}
  \caption{Con algoritmos exponenciales}
  \label{fig:k_one_with_exponential}
\end{subfigure}%
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_24_1.png}
  \caption{Sin algoritmos exponenciales}
  \label{fig:k_one_without_exponential}
\end{subfigure}
\caption{$k=n/2$, elementos ordenados}
\label{fig:k_n2_elementos_ordenados}
\end{figure}


### $k = n$

\begin{figure}[H]
\centering
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_10_2.png}
  \caption{Con algoritmos exponenciales}
  \label{fig:k_n_with_exponential}
\end{subfigure}%
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_12_2.png}
  \caption{Sin algoritmos exponenciales}
  \label{fig:k_n_without_exponential}
\end{subfigure}
\caption{$k=n$, elementos desordenados}
\label{fig:k_n}
\end{figure}

\begin{figure}[H]
\centering
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_18_2.png}
  \caption{Con algoritmos exponenciales}
  \label{fig:k_n_with_exponential}
\end{subfigure}%
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_20_2.png}
  \caption{Sin algoritmos exponenciales}
  \label{fig:k_n_without_exponential}
\end{subfigure}
\caption{$k=n$, elemento único}
\label{fig:k_n}
\end{figure}

\begin{figure}[H]
\centering
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_22_2.png}
  \caption{Con algoritmos exponenciales}
  \label{fig:k_n_with_exponential}
\end{subfigure}%
\begin{subfigure}{.5\textwidth}
  \centering
  \includegraphics[width=.8\linewidth]{images/algoritmos_24_2.png}
  \caption{Sin algoritmos exponenciales}
  \label{fig:k_n_without_exponential}
\end{subfigure}
\caption{$k=n$, elementos ordenados}
\label{fig:k_n_elementos_ordenados}
\end{figure}


## Elección de algoritmo óptimo para cada $k$ según $n$

Podemos ver una aproximación del cálculo cualitativo en el siguiente gráfico

\begin{figure}[H]
  \centering
  \includegraphics[width=.9\textwidth]{GraficoKOptimo.png}
  \caption{Comparación del $k$ óptimo para todos los algoritmos}
  \label{fig:bragg}
\end{figure}

El grafico muestra una relación entre la complejidad de cada algoritmo variando
el parámetro $k$.
Simplemente a modo de ejemplo, se eligió un tamaño de entrada determinado ($n = 16$).

Ahora bien, fuera del tamaño determinado, podemos rescatar que hay 3 algoritmos
que no tienen un determinado $k$ para el cual alguno es mejor que el otro.
Es el caso del algoritmo de fuerza bruta, el de order and select y el QuickSelect.
Lógicamente, el algoritmo de fuerza bruta no puede competir contra absolutamente nadie.
Solo resta decir para el mismo que la complejidad de el k-selections se equipara
con el de fuerza bruta cuando $k = n$.

Para valores pequeños de $k$, observamos que el algoritmo más óptimo es el HeapSelect.
A medida que aumentamos el k pedido, éste algoritmo es superado por el k-heapsort.
Partiendo de la complejidad de los dos algoritmos, esto comienza a ocurrir a
partir de que $k*\log(n) = n*\log(k) -> k/\log(k) = n/\log(n)$.
Luego, podemos ver que el QuickSelect es el que termina siendo el más óptimo
para valores de $k$ más altos. Tomando los órdenes de complejidad mostrados
anteriormente, esto ocurre a partir de que $n = k * \log(n) -> k = n/\log(n)$.
Para el ejemplo dado con $n = 16$, esto comienza a ocurrir para $k >= 6$.

Es de notar también que para valores altos de $k$, tanto el k-heapsort como el
HeapSelect convergen al mismo orden que el Timsort utilizado.
También vemos que el k-selections es más eficiente que el Timsort para elecciones
$k$ menores a 3 (igualando la complejidad calculada de ambos, se da cuando
$n*\log(n) = k*n -> \log(n) = k$, lo cual da un $k$ ~ $2.77$ para el ejemplo).
