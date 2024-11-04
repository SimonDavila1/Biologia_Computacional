import sys
from read import read
from plot import plot1D, plot2D
import matplotlib.pyplot as plt

archivo_csv = sys.argv[1]
archivo_salida = sys.argv[2]
"""
Toma el primer y el segundo argumento de la línea de comandos (excluyendo el nombre del script) y los asigna a las variables archivo_csv y archivo_salida. Estos representan el archivo CSV de entrada y el nombre del archivo de salida del gráfico.
"""
columna_1, columnas_rest = read(archivo_csv)
"""
Llama a la función read para leer los datos del archivo CSV especificado. La función devuelve columna_1 (la primera columna) y columnas_rest (una lista con las columnas restantes).
"""

if len(columnas_rest) >= 2:
    """
    Comprueba si hay al menos dos columnas adicionales en columnas_rest, lo que permitiría generar un gráfico 2D.
    """
    # Caso 2D
    print("Generando gráfico 2D...")
    plot2D(columna_1, columnas_rest[0], columnas_rest[1], "Tiempo", "Posición Y")
    """
    Si hay al menos dos columnas adicionales, imprime un mensaje indicando que se generará un gráfico 2D y llama a la función plot2D, pasando la primera columna y las dos primeras columnas adicionales, junto con etiquetas para los ejes.
    """
else:
    # Caso 1D (dos columnas o solo una columna adicional)
    if columnas_rest:  # Asegúrate de que haya datos en columnas_rest
        print("Generando gráfico 1D...")
        plot1D(columna_1, columnas_rest[0], "Tiempo", "Posición Y")
        """
        Si no hay suficientes columnas para un gráfico 2D, verifica si hay al menos una columna adicional. Si es así, imprime un mensaje indicando que se generará un gráfico 1D y llama a la función plot1D, pasando la primera columna y la única columna adicional.
        """
    else:
        print("Error: No hay datos suficientes para generar un gráfico.")
        """
        Si columnas_rest está vacío (no hay columnas adicionales), imprime un mensaje de error indicando que no hay suficientes datos para generar un gráfico.
        """


plt.savefig(archivo_salida)
"""
Utiliza plt.savefig() para guardar la figura generada en un archivo con el nombre especificado por archivo_salida.
"""





