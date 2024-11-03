"""
import pandas as pd
def read(archivo_csv):

    df = pd.read_csv(archivo_csv)
    
    columna_1 = df.iloc[:, 0].tolist()
    columnas_rest = []

    if df.shape[1] == 2:
        columnas_rest = df.iloc[:, 1].tolist()
    elif df.shape[1] == 3:
        columnas_rest = [df.iloc[:, 1].tolist(), df.iloc[:, 2].tolist()]

    return columna_1, columnas_rest
    """
import pandas as pd

def read(archivo_csv):
    """Lee un archivo CSV y devuelve dos listas: una con la primera columna y otra con las restantes."""
    df = pd.read_csv(archivo_csv)

    # Asegúrate de que hay al menos una columna
    if df.shape[1] == 0:
        raise ValueError("El archivo CSV no tiene columnas.")

    columna_1 = df.iloc[:, 0].tolist()  # Primera columna
    columnas_rest = []

    # Agregar las columnas restantes a columnas_rest
    for i in range(1, df.shape[1]):
        columnas_rest.append(df.iloc[:, i].tolist())
    
    return columna_1, columnas_rest

    
    
    
    
    
    
