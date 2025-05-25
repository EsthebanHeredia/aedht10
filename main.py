# Programa principal para gestionar rutas entre ciudades con diferentes condiciones climáticas
from grafo import Grafo
from floyd import floyd_warshall, reconstruir_camino
from centro import calcular_centro

def mostrar_menu():
    # Muestra las opciones disponibles para el usuario
    print("\n1. Ruta más corta entre ciudades")
    print("2. Mostrar ciudad centro del grafo")
    print("3. Modificar el grafo")
    print("4. Salir")

def main():
    # Inicialización del grafo y carga de datos
    grafo = Grafo()
    grafo.cargar_desde_archivo("logistica.txt")
    grafo.cargar_todas_las_matrices("logistica.txt")  # Inicializa matrices para cada clima
    matriz = grafo.obtener_matriz()
    ciudades = grafo.obtener_ciudades()
    dist, next_node = floyd_warshall(matriz)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Cálculo de la ruta más corta entre dos ciudades
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

        elif opcion == '2':
            # Identificación del centro del grafo
            centro_idx = calcular_centro(dist)
            print(f"Centro del grafo: {ciudades[centro_idx]}")

        elif opcion == '3':
            # Módulo de modificación del grafo
            print("a) Eliminar conexión")
            print("b) Agregar conexión")
            print("c) Cambiar clima")
            subop = input("Seleccione subopción: ")

            if subop == 'a':
                # Eliminar una conexión existente
                c1 = input("Ciudad origen: ")
                c2 = input("Ciudad destino: ")
                grafo.eliminar_conexion(c1, c2)
                matriz = grafo.obtener_matriz_por_clima("normal")
                dist, next_node = floyd_warshall(matriz)

            elif subop == 'b':
                # Agregar una nueva conexión
                c1 = input("Ciudad origen: ")
                c2 = input("Ciudad destino: ")
                tiempos = []
                for clima in ["normal", "lluvia", "nieve", "tormenta"]:
                    t = int(input(f"Tiempo en {clima}: "))
                    tiempos.append(t)
                grafo.agregar_conexion(c1, c2, tiempos)
                matriz = grafo.obtener_matriz_por_clima("normal")
                dist, next_node = floyd_warshall(matriz)

            elif subop == 'c':
                # Cambiar el clima actual y recalcular rutas
                clima = input("Ingrese clima (normal, lluvia, nieve, tormenta): ").lower()
                matriz = grafo.obtener_matriz_por_clima(clima)
                dist, next_node = floyd_warshall(matriz)
                print(f"Clima cambiado a {clima}. Rutas recalculadas.")

        elif opcion == '4':
            # Salir del programa
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()