\newpage

# Programación dinámica

## El problema de la mochila

   En este problema, tenemos una cantidad *n* de items, cada uno de los cuales posee un peso *w* no negativo y un valor *v*. Con estos items, nosotros vamos a ir llenando una mochila, la cual posee una capacidad máxima determinada.
   El problema plantea encontrar los items que se incluirán en la mochila, de tal forma que la suma de todos sus pesos particulares *w* no supere la capacidad máxima de la mochila y, además, la suma de todos los valores *v* de los objetos que se incluyen, sea máxima.

   Contrario a lo que uno puede intuir, no existe un algoritmo greedy eficiente que lo resuelva, por lo que caemos en la programación dinámica como una nueva técnica para encontrar soluciones óptimas a determinados problemas, como el de la mochila, partiendo el mismo en sub-problemas cada vez más pequeños (los cuales se resolverán mucho más fácilmente), y solapando las soluciones a dichos sub-problemas para llegar a la solución del problema original. Es decir, debemos procurar resolver sub-problemas cada vez más sencillos, los cuales, en conjunto, forman la solución al problema mayor.
   
   En este informe se verá un pequeño análisis general del orden de complejidad de la solución encontrada, como así también las diferencias entre los tiempos de ejecución de dos enfoques distintos para implementar la solución (Bottom-up y Top-Down)

### Solución y orden de complejidad

   

## El problema del viajante de comercio
