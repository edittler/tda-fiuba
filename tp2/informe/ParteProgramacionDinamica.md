\newpage

# Programación dinámica

## El problema de la mochila (versión 0-1)

   En este problema, tenemos una cantidad *n* de items, cada uno de los cuales posee un peso *w* no negativo y un valor *v*. Con estos items, nosotros vamos a ir llenando una mochila, la cual posee una capacidad máxima determinada.
   El problema plantea encontrar los items que se incluirán en la mochila, de tal forma que la suma de todos sus pesos particulares *w* no supere la capacidad máxima de la mochila y, además, la suma de todos los valores *v* de los objetos que se incluyen, sea máxima.

   Contrario a lo que uno puede intuir, no existe un algoritmo greedy eficiente que lo resuelva, por lo que caemos en la programación dinámica como una nueva técnica para encontrar soluciones óptimas a determinados problemas, como el de la mochila, partiendo el mismo en sub-problemas cada vez más pequeños (los cuales se resolverán mucho más fácilmente), y solapando las soluciones a dichos sub-problemas para llegar a la solución del problema original. Es decir, debemos procurar resolver sub-problemas cada vez más sencillos, los cuales, en conjunto, forman la solución al problema mayor.
   
   En este informe se verá un pequeño análisis general del orden de complejidad de la solución encontrada, como así también las diferencias entre los tiempos de ejecución de dos enfoques distintos para implementar la solución (Bottom-up y Top-Down)

### Solución y orden de complejidad

   En esta versión del problema de la mochila, podemos entender que un único ítem puede pertenecer a la solución óptima o no. Resumiremos la solución del problema en encontrar el valor máximo $V$ que se puede incluir en la mochila sin superar su capacidad.

   Es trivial ver que, si tenemos un caso hipotético en el que la capacidad de la mochila es 100 y el peso de un elemento $*i* -> *w_i = 101*$, entonces, dicho elemento *i* queda descartado de la solución óptima.
   Por otro lado, si el peso del item es menor a la capacidad de la mochila, puede o no pertenecer a la solución óptima. Esto se resuelve comparando entre el valor máximo que se puede llegar a obtener con una solución óptima *sin* el elemento en cuestión, y el valor máximo que se puede obtener con una solución óptima *incluyendo* el elemento en cuestión.
   
   Suponemos que tenemos *n* elementos {1 .. n}. Quiero encontrar la solución óptima para *n* elementos y una capacidad de $W$. Formalizando lo expresado en los últimos dos párrafos, quiero encontrar el valor máximo que puedo obtener cumpliendo las restricciones planteadas ($valor_optimo(n,W)$).
   Comenzando con el elemento *n*, si $w_n > W$ -> $valor_optimo(n,W) = valor_optimo(n - 1, W)$, ya que no puedo incluir a mi elemento *n*, por lo que debo encontrar una solución óptima con los $n - 1$ elementos restantes de mi conjunto.
   Ahora bien, si $w_n <= W$ -> $valor_optimo(n,W) = max(valor_optimo(n - 1, W), v_n + valor_optimo(n - 1, W - w_n))$. Como se planteó anteriormente, se debe encontrar el valor máximo entre una solución sin incluir al elemento corriente, y una solución incluyendo al elemento (esto es, encontrar una combinación con los n - 1 elementos restantes, ya habiéndole sumado el valor del elemento *n*, y habiéndole restado a la capacidad total de la mochila, el peso del elemento que incluí).
   Esta recurrencia es la que se plantea para resolver el problema de la mochila.
   
   

## El problema del viajante de comercio
