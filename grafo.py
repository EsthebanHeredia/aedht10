import math

# Define la clase Grafo para representar la red de ciudades y rutas.
class Grafo:
    def __init__(self):
        self.ciudades = [] # Lista de nombres de ciudades
        self.indices = {}  # Diccionario que mapea ciudades a sus índices en la matriz
        self.matriz = []   # Matriz de adyacencia para tiempos de ruta (clima normal)

    # Carga los datos del grafo desde un archivo.
    def cargar_desde_archivo(self, archivo):
        # Lee las conexiones desde el archivo de entrada
        with open(archivo, 'r') as f:
            conexiones = [line.strip().split() for line in f if line.strip()]
        
        # Registra todas las ciudades encontradas y les asigna índices
        for c1, c2, *_ in conexiones:
            for ciudad in [c1, c2]:
                if ciudad not in self.ciudades:
                    self.indices[ciudad] = len(self.ciudades)
                    self.ciudades.append(ciudad)

        n = len(self.ciudades)
        # Inicializa la matriz con infinito y 0 en la diagonal principal
        self.matriz = [[math.inf]*n for _ in range(n)]
        for i in range(n):
            self.matriz[i][i] = 0

        # Agrega los tiempos de viaje en clima normal
        for c1, c2, normal, *_ in conexiones:
            i, j = self.indices[c1], self.indices[c2]
            self.matriz[i][j] = int(normal)

    def obtener_matriz(self):
        return self.matriz

    def obtener_ciudades(self):
        return self.ciudades

    def cargar_todas_las_matrices(self, archivo):
        # Carga las matrices para todos los tipos de clima
        with open(archivo, 'r') as f:
            conexiones = [line.strip().split() for line in f if line.strip()]

        # Registro de ciudades
        for c1, c2, *_ in conexiones:
            for ciudad in [c1, c2]:
                if ciudad not in self.ciudades:
                    self.indices[ciudad] = len(self.ciudades)
                    self.ciudades.append(ciudad)

        n = len(self.ciudades)
        # Inicializa matrices para los 4 tipos de clima
        self.matrices_por_clima = []
        for clima_idx in range(4):
            matriz = [[float('inf')] * n for _ in range(n)]
            for i in range(n): matriz[i][i] = 0
            self.matrices_por_clima.append(matriz)

        # Llena las matrices con los tiempos de cada clima
        for c1, c2, normal, lluvia, nieve, tormenta in conexiones:
            i, j = self.indices[c1], self.indices[c2]
            tiempos = [int(normal), int(lluvia), int(nieve), int(tormenta)]
            for idx in range(4):
                self.matrices_por_clima[idx][i][j] = tiempos[idx]

    def obtener_matriz_por_clima(self, clima):
        # Devuelve la matriz correspondiente al clima especificado
        from clima import CLIMA_IDX
        return self.matrices_por_clima[CLIMA_IDX[clima]]

    def eliminar_conexion(self, ciudad1, ciudad2):
        # Elimina la conexión entre dos ciudades en todas las matrices de clima
        i, j = self.indices[ciudad1], self.indices[ciudad2]
        for matriz in self.matrices_por_clima:
            matriz[i][j] = float('inf')

    def agregar_conexion(self, ciudad1, ciudad2, tiempos):
        # Agrega una nueva conexión entre ciudades con sus tiempos
        if ciudad1 not in self.indices or ciudad2 not in self.indices:
            print("Una o ambas ciudades no existen.")
            return
        i, j = self.indices[ciudad1], self.indices[ciudad2]
        for idx in range(4):
            self.matrices_por_clima[idx][i][j] = tiempos[idx]