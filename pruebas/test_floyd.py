# Importa la clase Grafo y la función floyd_warshall para las pruebas.
import sys
import os

# Añade el directorio padre al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafo import Grafo
from floyd import floyd_warshall

# Define una función de prueba para un caso simple del algoritmo de Floyd-Warshall.
def test_floyd_simple():
    g = Grafo()
    g.ciudades = ["A", "B", "C"]
    g.indices = {"A":0, "B":1, "C":2}
    # Matriz de adyacencia: 1000 representa infinito.
    g.matriz = [
        [0, 5, 1000],
        [1000, 0, 3],
        [1, 1000, 0]
    ]
    dist, _ = floyd_warshall(g.matriz)
    # Comprueba la distancia más corta de A a C (A -> B -> C = 5 + 3 = 8).
    assert dist[0][2] == 8
    return True

# Este código se ejecuta solo cuando el archivo se ejecuta directamente
if __name__ == "__main__":
    try:
        test_floyd_simple()
        print("El algoritmo de Floyd-Warshall funciona correctamente.")
    except AssertionError as e:
        print(f"La prueba falló: {e}")