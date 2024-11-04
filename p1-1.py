import sys
from read import read
archivo_csv = sys.argv[1]
"""
Asigna el argumento pasado al script (el nombre del archivo CSV) a la variable archivo_csv.
"""
columna_1, columna_rest = read(archivo_csv)
"""
Llama a la función read, pasando archivo_csv como argumento, y guarda las dos listas devueltas en columna_1 y columna_rest
"""
print("Elementos de la primera columna:")
print(columna_1[:5] if len(columna_1) > 5 else columna_1)
"""
Imprime un encabezado y luego imprime los primeros 5 elementos de columna_1. Si la lista tiene 5 elementos o menos, imprime toda la lista.
"""
print("Elementos de la(s) otra(s) columna(s):")
if isinstance(columna_rest, list) and all(isinstance(sublist, list) for sublist in columna_rest):
    for i, sublist in enumerate(columna_rest):
        print(f"Columna {i + 2}: {sublist[:5] if len(sublist) > 5 else sublist}")
else:
    print(columna_rest[:5] if len(columna_rest) > 5 else columna_rest)

"""
Imprime un encabezado para las otras columnas. Verifica si columna_rest es una lista de listas. Si es así, recorre cada sublista (que representa una columna) usando enumerate y las imprime con un índice que comienza en 2 (para reflejar las columnas después de la primera). Imprime solo los primeros 5 elementos de cada sublista o la sublista completa si tiene 5 elementos o menos.

imprime los primeros 5 elementos de columna_rest o la lista completa si tiene 5 elementos o menos.
"""

