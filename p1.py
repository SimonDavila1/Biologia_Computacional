import sys
from read import read
from plot import plot1D, plot2D
import matplotlib.pyplot as plt

archivo_csv = sys.argv[1]
archivo_salida = sys.argv[2]

# Lee los datos del archivo CSV
columna_1, columnas_rest = read(archivo_csv)

# Verifica si hay suficientes columnas para un gráfico 2D
if len(columnas_rest) >= 2:
    # Caso 2D
    print("Generando gráfico 2D...")
    plot2D(columna_1, columnas_rest[0], columnas_rest[1], "Tiempo", "Posición Y")
else:
    # Caso 1D (dos columnas o solo una columna adicional)
    if columnas_rest:  # Asegúrate de que haya datos en columnas_rest
        print("Generando gráfico 1D...")
        plot1D(columna_1, columnas_rest[0], "Tiempo", "Posición Y")
    else:
        print("Error: No hay datos suficientes para generar un gráfico.")

# Guarda la figura generada
plt.savefig(archivo_salida)




