import math

# Define la clase Grafo para representar la red de ciudades y rutas.
class Grafo:
    def __init__(self):
        self.ciudades = [] # Lista de nombres de ciudades.
        self.indices = {} # Mapeo de nombres de ciudades a índices.
        self.matriz = [] # Matriz de adyacencia (tiempos de ruta).

    # Carga los datos del grafo desde un archivo.
    def cargar_desde_archivo(self, archivo):
        with open(archivo, 'r') as f:
            conexiones = [line.strip().split() for line in f if line.strip()]
        
        # Registra ciudades y asigna índices.
        for c1, c2, *_ in conexiones:
            for ciudad in [c1, c2]:
                if ciudad not in self.ciudades:
                    self.indices[ciudad] = len(self.ciudades)
                    self.ciudades.append(ciudad)

        n = len(self.ciudades)
        # Inicializa la matriz con infinito, 0 en la diagonal.
        self.matriz = [[math.inf]*n for _ in range(n)]
        for i in range(n):
            self.matriz[i][i] = 0

        # Agrega tiempos de viaje (clima normal) a la matriz.
        for c1, c2, normal, *_ in conexiones:
            i, j = self.indices[c1], self.indices[c2]
            self.matriz[i][j] = int(normal)

    def obtener_matriz(self):
        return self.matriz

    def obtener_ciudades(self):
        return self.ciudades