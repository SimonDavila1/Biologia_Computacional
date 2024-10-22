import pandas as pd
import matplotlib.pyplot as plt
import sys
csv_ingresa= sys.argv[1]
png_salida= sys.argv[2]
df=pd.read_csv(csv_ingresa, sep=";")
plt.plot(df['Tiempo'], df['Variable'])
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Gráfico de Tiempo vs Valor')
plt.savefig((png_salida), format='png', dpi=300, bbox_inches='tight')
plt.show()



