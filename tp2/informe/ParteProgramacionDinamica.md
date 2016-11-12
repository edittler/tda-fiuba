\newpage

# Programación dinámica

## El problema de la mochila


## El problema del viajante de comercio

El algoritmo Bellman-Held–Karp fue propuesto en 1962 independientemente por
Bellman [@Bellman1962] y por Held y Karp [@HeldKarp1962].

En la formulación de Bellman, se define la función $D(v,S)$ la distancia mínima
desde $v$ hasta la ciudad de origen, $S$ el conjunto de ciudades a visitar.
Si el conjunto S se encuentra vacío (o contiene la ciudad de origen),
$D(v,S)=d_{v0}$.
Se define $d_{ij}$ como la distancia desde la ciudad i hasta la ciudad j.
Para el resto de los casos, $D(v,S)=\min_{u\in S}(d_{vu} + D(u, S - \{u\}))$

Un pseudocódigo para calcular la distancia del ciclo hamiltoniano mínimo es el
siguiente:

```
function TSP (M, n)
  for k := 2 to n do
    C({1, k}, k) := M[1,k]
  end for

  for s := 3 to n do
    for all S in {1, 2, . . . , n}, |S| = s do
      for all k in S do
        {C(S, k) = min [C(S - {k}, m) + M[m,k] ]}
      end for
    end for
  end for

  opt := min [C({1, 2, 3, . . . , n}, k) + M[k,1] ]
  return (opt)
end
```

Sin embargo, como se debe construir el camino mínimo, para el costo hacia cada
conjunto se guarda el padre desde el cual se llega.

```
function TSP (M, n)
  for k := 2 to n do
    C({1, k}, k) := (M[1,k], 1)
  end for

  for s := 3 to n do
    for all S in {1, 2, . . . , n}, |S| = s do
      for all k in S do
        C(S, k) = min[(C(S - {k}, m) + M[m,k], m)]
      end for
    end for
  end for

  // TODO: Código para obtener el camino
end
```