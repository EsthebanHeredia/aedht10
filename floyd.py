import math

# Implementación del algoritmo de Floyd-Warshall.
def floyd_warshall(matriz):
    n = len(matriz)
    dist = [row[:] for row in matriz]
    # next_node[i][j] almacena el siguiente nodo en el camino más corto de i a j.
    next_node = [[None if matriz[i][j] == math.inf else j for j in range(n)] for i in range(n)]

    for k in range(n): # Nodo intermedio k
        for i in range(n): # Nodo de origen i
            for j in range(n): # Nodo de destino j
                # Si el camino de i a j a través de k es más corto, actualiza.
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node

# Reconstruye el camino más corto entre dos nodos i y j.
def reconstruir_camino(next_node, i, j):
    if next_node[i][j] is None: # No hay camino.
        return []
    camino = [i]
    while i != j:
        i = next_node[i][j]
        camino.append(i)
    return camino