import os
import unittest
from grafo import Grafo

class TestGrafo(unittest.TestCase):
    def test_eliminar_y_recalcular(self):
        # Prueba la eliminación de conexión usando datos reales
        archivo = "logistica.txt"
        ruta_archivo = os.path.join(os.path.dirname(__file__), "..", archivo)
        
        if not os.path.exists(ruta_archivo):
            self.skipTest(f"Archivo {archivo} no encontrado, omitiendo prueba")
        
        try:
            g = Grafo()
            g.cargar_todas_las_matrices(archivo)
            g.eliminar_conexion("Lima", "Quito")
            matriz = g.obtener_matriz_por_clima("normal")
            self.assertEqual(matriz[g.indices["Lima"]][g.indices["Quito"]], float('inf'))
        except Exception as e:
            self.fail(f"La prueba falló con el error: {e}")
            
    def test_eliminar_y_recalcular_mock(self):
        """Prueba alternativa que no depende de archivos externos"""
        # Configuración de datos de prueba
        g = Grafo()
        g.indices = {"Lima": 0, "Quito": 1}
        g.ciudades = ["Lima", "Quito"]
        matriz_normal = [[0, 10], [10, 0]]
        g._matrices = {"normal": matriz_normal}
        
        # Ejecuta la operación y verifica el resultado
        g.eliminar_conexion("Lima", "Quito")
        matriz = g.obtener_matriz_por_clima("normal")
        self.assertEqual(matriz[g.indices["Lima"]][g.indices["Quito"]], float('inf'))

if __name__ == "__main__":
    unittest.main()
