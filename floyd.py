import math

# Implementación del algoritmo de Floyd-Warshall.
def floyd_warshall(matriz):
    # Algoritmo para encontrar los caminos más cortos entre todos los pares de nodos
    n = len(matriz)
    # Copia la matriz de distancias
    dist = [row[:] for row in matriz]
    # Matriz que guarda el siguiente nodo en el camino más corto de i a j
    next_node = [[None if matriz[i][j] == math.inf else j for j in range(n)] for i in range(n)]

    # Iteración principal: para cada nodo intermedio k
    for k in range(n): # Nodo intermedio k
        for i in range(n): # Nodo de origen i
            for j in range(n): # Nodo de destino j
                # Si pasar por k mejora la distancia actual
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node

# Reconstruye el camino más corto entre dos nodos i y j.
def reconstruir_camino(next_node, i, j):
    # Reconstruye el camino desde el nodo i hasta el nodo j usando la matriz next_node
    if next_node[i][j] is None: # No hay camino válido
        return []
    camino = [i]
    while i != j:
        i = next_node[i][j]
        camino.append(i)
    return camino