import matplotlib.pyplot as plt
import math
import statistics

def plot1D(x, y, xlabel, ylabel):
    """
    Define una función plot1D que toma cuatro argumentos: x (datos en el eje x), y (datos en el eje y), xlabel (etiqueta del eje x) y ylabel (etiqueta del eje y). La función genera un gráfico lineal.
    """
    plt.figure(figsize=(10, 6))
    """
    Crea una nueva figura de tamaño 10 por 6 pulgadas para el gráfico. Esto ayuda a ajustar la visualización del gráfico.
    """
    plt.plot(x, y, marker='o')
    """
    Dibuja un gráfico de líneas con los datos x y y, y coloca un marcador en cada punto (marker='o').
    """
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    """
    Asigna las etiquetas de los ejes x e y usando los valores proporcionados como xlabel y ylabel.
    """
    plt.grid(True)
    """
    Activa la cuadrícula en el gráfico para facilitar la visualización de los datos.
    """
    plt.title("Gráfico 1D")
    """
    Agrega un título al gráfico con el texto “Gráfico 1D”.
    """
def plot2D(x, y, c, xlabel, ylabel):
    """
    Define una función plot2D que toma cinco argumentos: x (coordenadas en el eje x), y (coordenadas en el eje y), c (valores que definen los colores de los puntos), xlabel y ylabel. La función genera un gráfico de dispersión (scatter plot) en 2D.
    """
    plt.figure(figsize=(10, 6))
    """
    Crea una nueva figura de tamaño 10 por 6 pulgadas para el gráfico de dispersión.
    """
    scatter = plt.scatter(x, y, c=c, cmap='viridis')
    """
    Dibuja un gráfico de dispersión con los datos x y y, coloreando los puntos según los valores de c y usando la paleta de colores viridis.
    """
    plt.colorbar(scatter, label='Valor de campo')
    """
    Agrega una barra de color al gráfico que indica los valores de c, con la etiqueta “Valor de campo”.
    """
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    """
    Asigna las etiquetas de los ejes x e y usando los valores proporcionados como xlabel y ylabel.
    """
    plt.grid(True)
    """
    Activa la cuadrícula en el gráfico para facilitar la visualización de los datos.
    """
    plt.title("Gráfico 2D")
    """
    Agrega un título al gráfico con el texto “Gráfico 2D”.
    """

   
