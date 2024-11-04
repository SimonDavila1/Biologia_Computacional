import sys
import numpy as np
import matplotlib.pyplot as plt

class Celda:
    def __init__(self, estado=False):
        self.estado = estado
        """
        Define una clase Celda que representa una celda en la grilla. Su constructor inicializa el estado de la celda (por defecto False, lo que significa que la celda está “muerta”).
        """
    def interactuar(self, vecinas):
        vivas = sum([1 for vecina in vecinas if vecina.estado])
        
        if self.estado:
            if vivas < 2 or vivas > 3:
                return Celda(False)  # Muere
            else:
                return Celda(True)  # Sigue viva
        else:
            if vivas == 3:
                return Celda(True)  # Vive
            else:
                return Celda(False)  # Sigue muerta
"""
Método interactuar: toma una lista de celdas vecinas y calcula cuántas están vivas. 
Si la celda actual está viva y tiene menos de 2 o más de 3 vecinas vivas, muere (por subpoblación o sobrepoblación). 
Si está muerta y tiene exactamente 3 vecinas vivas, revive (por reproducción). 
Devuelve una nueva instancia de Celda con el estado resultante.
"""

class Grilla:
    def __init__(self, tamaño, vivas_iniciales, archivo_exportar):
        self.tamaño = tamaño
        self.celdas = [[Celda() for _ in range(tamaño)] for _ in range(tamaño)]
        self.celdas_siguiente = [[Celda() for _ in range(tamaño)] for _ in range(tamaño)]
        self.archivo_exportar = archivo_exportar
        self.contador = 0
        
        for (i, j) in vivas_iniciales:
            self.celdas[i][j] = Celda(True)
            """
            Define la clase Grilla, que representa el tablero del juego. 
            Inicializa una matriz celdas y celdas_siguiente de objetos Celda de tamaño tamaño. 
            Marca las posiciones vivas iniciales basadas en la lista vivas_iniciales. 
            La variable archivo_exportar se usa para nombrar los archivos de salida, 
            y contador sirve para llevar la cuenta de las iteraciones.
            """
            
    
    def actualizar_celdas(self):
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                self.celdas[i][j].estado = self.celdas_siguiente[i][j].estado
                """
                Método actualizar_celdas: actualiza el estado de las celdas actuales 
                con los estados calculados en celdas_siguiente
                """
    
    def obtener_vecinas(self, x, y):
        vecinas = []
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if (i, j) != (x, y) and 0 <= i < self.tamaño and 0 <= j < self.tamaño:
                    vecinas.append(self.celdas[i][j])
        return vecinas
    """
    Método obtener_vecinas: devuelve una lista de celdas vecinas alrededor de una celda en la posición (x, y),
    verificando que los índices estén dentro de los límites de la grilla.
    """
    def avanzar(self):
        for i in range(self.tamaño):
            for j in range(self.tamaño):
                vecinas = self.obtener_vecinas(i, j)
                self.celdas_siguiente[i][j] = self.celdas[i][j].interactuar(vecinas)
        self.actualizar_celdas()
    """
    Método avanzar: actualiza el estado de cada celda en la grilla basándose en 
    la interacción con sus vecinas y actualiza la grilla después de calcular los nuevos estados.
    """
    def visualizar(self):
        matriz = np.array([[1 if self.celdas[i][j].estado else 0 for j in range(self.tamaño)] for i in range(self.tamaño)])
        plt.imshow(matriz, cmap='binary')
        plt.savefig(f"{self.archivo_exportar}_{self.contador}.png")
        plt.close()
        self.contador += 1
"""
Método visualizar: genera una representación visual de la grilla en forma de imagen binaria 
(1 para celdas vivas, 0 para celdas muertas) 
y la guarda como un archivo PNG. Incrementa el contador de iteraciones.
"""
def leer_datos(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        tamaño = int(lineas[0].strip())
        posiciones_vivas = []
        for linea in lineas[1:]:
            if linea.strip():
                posiciones_vivas.append(tuple(map(int, linea.strip().split(','))))
    return tamaño, posiciones_vivas
"""
Función leer_datos: lee un archivo de texto que contiene el tamaño de la grilla en la primera línea y 
las coordenadas de las celdas vivas en las siguientes líneas, devolviendo el tamaño y las posiciones 
iniciales de las celdas vivas.
"""
def main():
    if len(sys.argv) != 2:
        print("Uso: python conway.py <archivo_datos>")
        return
    """
    Función main: verifica que se pase un archivo de datos como argumento. 
    Llama a leer_datos para obtener el tamaño de la grilla y las posiciones iniciales de las celdas vivas. 
    Crea un objeto Grilla, avanza la simulación 10 iteraciones y guarda gráficos en cada paso.
    """
    archivo_datos = sys.argv[1]
    tamaño, posiciones_vivas = leer_datos(archivo_datos)
    
    grilla = Grilla(tamaño, posiciones_vivas, "estado_grilla")
    
    # Número de iteraciones que quieres avanzar
    num_iteraciones = 10
    
    print("Ejecutando la simulación...")
    for _ in range(num_iteraciones):
        grilla.avanzar()
        grilla.visualizar()
    
    print("Simulación completada y gráficos guardados.")

if __name__ == "__main__":
    main()
"""
Ejecuta la función main solo si el script se ejecuta directamente (no cuando se importa como módulo).
"""