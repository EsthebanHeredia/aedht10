# centro.py

def calcular_centro(matriz):
    # Calcula el centro del grafo: el nodo con la menor excentricidad
    # La excentricidad es la distancia máxima desde un nodo a cualquier otro
    excentricidades = []
    for fila in matriz:
        excentricidades.append(max(x for x in fila if x != float('inf')))
    
    # El centro es el nodo con menor excentricidad
    menor = min(excentricidades)
    return excentricidades.index(menor)