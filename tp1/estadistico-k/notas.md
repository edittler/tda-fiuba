# Notas

## Brute Force

### Orden
A simple vista, calcular si un elemento es o no el 4to es O(n), ya que se fija cuántos son menores a él entre todos los otros. Como lo hacemos potencialmente para todos los elementos, este método es O(n²).

### Sugerencia
Para almacenar los elementos menores al que se está analizando, no convendría directamente usar una lista y utilizar append? Cada elemento nuevo es **siempre** O(1) (a diferencia del set, donde es en promedio O(1), y seguramente es una estructura más sencilla y más rápida para estos fines.

## Sort and Select

### Potencial Problema
La lista indexa desde 0. Debería devolver el elemento de índice k-1.

### Orden.
El timsort (algoritmo de ordenamiento usado por python) es O(n logn) en el peor caso (lineal en el mejor). Una vez que está hecho el orden solo se toma el elemento k de la lista en O(1). Por lo tanto, este algoritmo sería O(n logn).

## k-selecciones

En la selección se analizan los n elementos de la lista y se pone en primer lugar al más pequeño. Luego, sobre los n-1 restantes se repite el proceso. Luego sobre n -2 y así k veces en total. Cada selección es O(n) en el peor caso (suponiendo orden descendente). O(1) en el mejor (suponiendo orden ascendente). El proceso es entonces kO(n) (tanto k como n son parte de la entrada, ninguna es constante). Ya que k < n, esto seguramente sea menor a O(n^2), pero salvo que k sea menor a log(n), este algoritmo es superado por el Sort and Select.

### Potencial Problema
Igual a Sort and Select.

## k-heapsort

Un heapsort es un algoritmo de selección, solo se usa un heap de mínimo para obtener el mínimo en O(logn) (En realidad es O(1), pero al quitarlo se debe hacer un upheap o float, que es O(logn)). Entonces, el heapsort consiste en dos etapas:

1. Heapify. Se reordena el array para que sea un heap. Esto es O(n).
2. las n obtenciones del mínimo O(n logn).

Por lo tanto, un heapsort normalmente es O(n) + O(n logn) = O(n logn).

Aquí, al igual que con el k-selecciones, quitaremos los primeros k elementos. Por esto, aquí se hará el heapify, sucedido de k extracciones del mínimo. El orden sería O(n) + O(k logn) con k < n. Si bien es O(n logn), esta es una cota un poco grosera, dado justamente el k<n.


**OJO** Es probable que el "heapq.nsmallest(k+1, elements)" sea **este** algoritmo, ya que es un heap con todos los elementos. El heapSelect (que es el siguiente) es más barato.

## HeapSelect
Se utiliza un heap de k elementos en lugar de n. Si el heap ya tiene k elementos, el elemento nuevo debería desplazar a uno para poder entrar.

Esto entonces se separa en
1. Construcción del heap: ??
2. k extracciones, cada una O(logk)

Entonces queda pendiente ver cómo se construye este heap, pero si esto no fuera problema, el orden sería O(k logk), que es menor al O(n logn) que teníamos hasta ahora.

## QuickSelect
Se usa la lógica del Quicksort: se define un pivote y se ponen todos los elementos mayores "a la derecha" y todos los menores "a la izquierda". Según la posición p del pivote:
- Si p == k: se devuelve l[p]
- Si p < k: se hace QuickSelect sobre la parte derecha (l[p+1..n])
- Si p > k: se hace QuickSelect sobre la parte izquierda(l[0..p])
Esto entonces, en el caso óptimo de que el pivote siempre queda a la mitad tiene un tiempo de T(n) = T(n/2) + O(n) [n es lo que tarda en poner todo en su lado correspondiente del pivote].

Utilizando el Teorema Maestro, esto es O(n).
