import pandas as pd

def read(archivo_csv):
    """Lee un archivo CSV y devuelve dos listas: una con la primera columna y otra con las restantes."""
    df = pd.read_csv(archivo_csv)

    # Asegúrate de que hay al menos una columna
    if df.shape[1] == 0:
        raise ValueError("El archivo CSV no tiene columnas.")
        """
        Verifica si el archivo CSV tiene al menos una columna. Si no es así, lanza un ValueError con un mensaje de error explicativo
        """

    columna_1 = df.iloc[:, 0].tolist()
    """
    Extrae la primera columna del DataFrame df usando iloc (selección por índice) y la convierte en una lista, asignándola a la variable columna_1.
    """
    columnas_rest = []
    """
    Crea una lista vacía llamada columnas_rest que se llenará con las columnas restantes del DataFrame.
    """
    for i in range(1, df.shape[1]):
        columnas_rest.append(df.iloc[:, i].tolist())
        """
        Por cada iteración, toma la columna i (con iloc), la convierte en una lista y la agrega a columnas_rest.
        """
    
    return columna_1, columnas_rest
    """
    Devuelve dos listas: columna_1 (la lista de la primera columna) y columnas_rest (una lista de listas con las columnas restantes).
    """
    
    
    
    
    
    
    
