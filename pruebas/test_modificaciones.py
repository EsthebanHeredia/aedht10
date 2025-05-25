import os
import sys

# Añade el directorio padre al path para poder importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafo import Grafo

def ejecutar_prueba():
    # Prueba la funcionalidad de eliminar_conexion con datos reales
    print("Ejecutando prueba de eliminar_conexion...")
    
    # Verifica que el archivo de datos existe
    archivo = "logistica.txt"
    ruta_archivo = os.path.join(os.path.dirname(__file__), "..", archivo)
    
    if not os.path.exists(ruta_archivo):
        print(f"OMITIDO: Archivo {archivo} no encontrado")
        return
    
    try:
        # Crea el grafo, carga los datos y elimina una conexión específica
        g = Grafo()
        g.cargar_todas_las_matrices(archivo)
        g.eliminar_conexion("Lima", "Quito")
        matriz = g.obtener_matriz_por_clima("normal")
        
        # Verifica que la conexión se haya eliminado correctamente
        if matriz[g.indices["Lima"]][g.indices["Quito"]] == float('inf'):
            print("ÉXITO: La conexión se eliminó correctamente")
        else:
            print(f"ERROR: La conexión no se eliminó. Valor: {matriz[g.indices['Lima']][g.indices['Quito']]}")
            sys.exit(1)
    except Exception as e:
        print(f"ERROR: La prueba falló con el error: {e}")
        sys.exit(1)

def ejecutar_prueba_mock():
    # Prueba con datos simulados para no depender del archivo externo
    print("Ejecutando prueba mock...")
    
    try:
        g = Grafo()
        
        # Configura un grafo de prueba mínimo
        g.indices = {"Lima": 0, "Quito": 1}
        g.ciudades = ["Lima", "Quito"]
        
        # Crea matriz de adyacencia para clima normal
        matriz_normal = [
            [0, 10],
            [10, 0]
        ]
        
        # Inicializa las matrices para cada tipo de clima
        g.matrices_por_clima = []
        for _ in range(4):
            g.matrices_por_clima.append([[float('inf'), float('inf')], [float('inf'), float('inf')]])
        
        # Asigna la matriz de clima normal
        g.matrices_por_clima[0] = matriz_normal
        
        # Ejecuta la operación a probar
        g.eliminar_conexion("Lima", "Quito")
        
        # Verifica el resultado
        matriz = g.obtener_matriz_por_clima("normal")
        if matriz[g.indices["Lima"]][g.indices["Quito"]] == float('inf'):
            print("ÉXITO: La conexión se eliminó correctamente (mock)")
        else:
            print(f"ERROR: La conexión no se eliminó (mock). Valor: {matriz[g.indices['Lima']][g.indices['Quito']]}")
            sys.exit(1)
    except Exception as e:
        print(f"ERROR: La prueba mock falló con el error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    ejecutar_prueba()
    ejecutar_prueba_mock()
    print("Todas las pruebas completadas con éxito")