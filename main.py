# Importa la clase Grafo y las funciones del algoritmo de Floyd-Warshall.
from grafo import Grafo
from floyd import floyd_warshall, reconstruir_camino

# Muestra el menú de opciones.
def mostrar_menu():
    print("\n1. Ruta más corta entre ciudades")
    print("2. Mostrar ciudad centro del grafo")
    print("3. Modificar el grafo")
    print("4. Salir")

# Función principal del programa.
def main():
    grafo = Grafo()
    grafo.cargar_desde_archivo("logistica.txt")
    matriz = grafo.obtener_matriz()
    ciudades = grafo.obtener_ciudades()
    # Calcula las distancias más cortas y los nodos siguientes.
    dist, next_node = floyd_warshall(matriz)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # Opción 1: Ruta más corta.
        if opcion == '1':
            origen = input("Ciudad origen: ")
            destino = input("Ciudad destino: ")

            if origen not in grafo.indices or destino not in grafo.indices:
                print("Una o ambas ciudades no existen.")
                continue

            i, j = grafo.indices[origen], grafo.indices[destino]
            if dist[i][j] == float('inf'):
                print("No hay camino entre esas ciudades.")
            else:
                camino = reconstruir_camino(next_node, i, j)
                print("Ruta más corta:")
                print(" -> ".join(ciudades[k] for k in camino))
                print(f"Distancia total: {dist[i][j]}")

        # Opción 2: Centro del grafo.

        elif opcion == '2':
            print("Haz seleccionado la opción 2.")

        # Opción 3: Modificar el grafo.

        elif opcion == '3':
            print("Haz seleccionado la opción 3.")

        # Opción 4: Salir.
        elif opcion == '4':
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()