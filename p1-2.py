from plot import plot1D, plot2D
import sys

out1d = sys.argv[1]
out2d = sys.argv[2]

t1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
x1 = [0, 1, -1, 1, -1, 1, -1, 1, -1]
"""
Define los datos de entrada t1 (tiempo) y x1 (posiciones) para la función plot1D.
"""
t2 = [0.0, 0.33, 0.66, 0.99, 1.32, 1.65, 1.98, 2.31, 2.64, 2.98,
      3.31, 3.64, 3.97, 4.30, 4.63, 4.96, 5.29, 5.62, 5.95, 6.28]
x2 = [1.0, 0.95, 0.79, 0.55, 0.25, -0.08, -0.4, -0.68, -0.88, -0.99,
      -0.99, -0.88, -0.68, -0.4, -0.08, 0.25, 0.55, 0.79, 0.95, 1.0]
y2 = [0.00, 0.325, 0.614, 0.837, 0.969, 0.997, 0.916, 0.736, 0.476,
      0.165, -0.165, -0.476, -0.736, -0.916, -0.997, -0.969, -0.837,
      -0.614, -0.325, -0.000245]
"""
Define los datos de entrada t2 (tiempo), x2 (coordenadas x) y y2 (coordenadas y) para la función plot2D. Estos datos se utilizan para representar un gráfico de dispersión en 2D.
"""

plot1D(t1, x1, "Tiempo", "Posición")
"""
Llama a la función plot1D pasando t1 como eje x, x1 como eje y, y los textos “Tiempo” y “Posición” como etiquetas de los ejes. Esta función genera un gráfico 1D de los datos proporcionados.
"""



plot2D(t2, x2, y2, "Tiempo", "Posición X")
"""
Llama a la función plot2D pasando t2 como eje x, x2 como eje y y y2 como valores de color para el gráfico. Las etiquetas de los ejes son “Tiempo” y “Posición X”. La función genera un gráfico de dispersión en 2D donde los puntos se colorean según los valores en y2.
"""

