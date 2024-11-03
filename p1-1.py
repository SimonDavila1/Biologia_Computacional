import sys
from read import read

# Verifica que se proporcione el archivo CSV como argumento
if len(sys.argv) != 2:
    print("Uso: python p1-1.py 'archivo.csv'")
    sys.exit(1)

archivo_csv = sys.argv[1]

# Lee el archivo CSV
columna_1, columna_rest = read(archivo_csv)

# Imprime los primeros 5 elementos de la primera columna
print("Elementos de la primera columna:")
print(columna_1[:5] if len(columna_1) > 5 else columna_1)

# Imprime los primeros 5 elementos de las otras columnas
print("Elementos de la(s) otra(s) columna(s):")
if isinstance(columna_rest, list) and all(isinstance(sublist, list) for sublist in columna_rest):
    for i, sublist in enumerate(columna_rest):
        print(f"Columna {i + 2}: {sublist[:5] if len(sublist) > 5 else sublist}")
else:
    print(columna_rest[:5] if len(columna_rest) > 5 else columna_rest)
