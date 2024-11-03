import matplotlib.pyplot as plt
import math
import statistics

def plot1D(x, y, xlabel, ylabel):
    """Genera un gráfico 1D con matplotlib."""
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.title("Gráfico 1D")

def plot2D(x, y, c, xlabel, ylabel):
    """Genera un gráfico 2D con matplotlib (scatter)."""
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(x, y, c=c, cmap='viridis')
    plt.colorbar(scatter, label='Valor de campo')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.title("Gráfico 2D")
   
