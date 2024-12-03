import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro, ttest_ind, ranksums, pearsonr, spearmanr, linregress
import sys
from matplotlib.ticker import FormatStrFormatter

# Directorio de trabajo
folder = '/Users/simondavila/Downloads/Biologia_Computacional/Trabajo final'
print(f"Estableciendo directorio de trabajo: {folder}")
os.chdir(folder)

# Leer rutas de los archivos desde argumentos del sistema
print("Leyendo rutas de archivo desde los argumentos del sistema...")
wbrdata_path = sys.argv[1]
locofdata_path = sys.argv[2]
print(f"Ruta del archivo WBRdata_final.csv: {wbrdata_path}")
print(f"Ruta del archivo LocOFdata.csv: {locofdata_path}")

# Cargar datos desde los archivos CSV
print("Cargando datos desde los archivos CSV...")
WBRdata_final = pd.read_csv('WBRdata_final.csv').to_numpy()
LocOFdata = pd.read_csv('LocOFdata.csv').to_numpy()

# Calcular percentiles y encontrar índices correspondientes
print("Calculando percentiles y obteniendo índices correspondientes...")
p3366 = np.percentile(LocOFdata[:, 1], [33, 66])
fp33 = np.where(LocOFdata[:, 1] <= p3366[0])[0]
fp66 = np.where(LocOFdata[:, 1] > p3366[1])[0]

# Inicializar contador
k = 0
stat=[]
print("Iniciando el procesamiento de datos...")

# Bucle para procesar proteínas, fracciones y normalización
for prot in range(1, 4):  # Iterar sobre GRK2, GRK5 y D2R
    print(f"Procesando datos para la proteína {prot}...")
    for f in range(1, 3):  # Iterar sobre fracciones Citosolica y Sinaptica
        print(f"  Procesando fracción {f}...")
        for n in [5]:  # Normalización Rojo Ponceau S
            
            # Filtrar datos por GRKs, D2R y fracción
            f1 = np.where((WBRdata_final[:, 1] == prot) & (WBRdata_final[:, 6] == f))[0]
            # Evitar divisiones por cero o valores inválidos
            divisor = WBRdata_final[f1, n - 1]
            divisor[divisor == 0] = np.nan  # Sustituir 0 por NaN
            normdata = np.column_stack((WBRdata_final[f1, 0], WBRdata_final[f1, 3] / divisor))
            normdata = normdata[~np.isnan(normdata).any(axis=1)]  # Remover filas con NaN

            #Creación lista nueva para agregar el valor de GRKs y D2R a su respectivo número indicador de rata (Solo valores mayores a 0.05)
            normdata2 = []
            for m in range(4, 54):  # Iterar sobre muestras
                f2 = np.where(normdata[:, 0] == m)[0]
                data1 = normdata[f2, 1]
                data1 = data1[data1 > 0.05]
                if len(data1) > 0:
                    normdata2.append([m, np.mean(data1)])
            normdata2 = np.array(normdata2)

            if normdata2.size == 0:
                print(f"    No hay datos válidos para proteína {prot}, fracción {f}.")
                continue  # Saltar si no hay datos válidos

            # Filtrar índices válidos
            valid_fp33 = fp33[fp33 < len(normdata2)]
            valid_fp66 = fp66[fp66 < len(normdata2)]

            LR = normdata2[valid_fp33, 1] if len(valid_fp33) > 0 else []
            HR = normdata2[valid_fp66, 1] if len(valid_fp66) > 0 else []

            LR = LR[LR > 0]
            HR = HR[HR > 0]

            if len(LR) == 0 or len(HR) == 0:
                print("No hay datos válidos para LR o HR.")
                continue  # Saltar iteraciones sin datos válidos
            
            # Calcular medias y normalizar datos
            mean_combined = np.mean(np.concatenate([LR, HR]))
            LRnorm = LR / mean_combined
            HRnorm = HR / mean_combined

            # Gráfico 1: Comparación LR vs HR
            print(f"    Generando gráfico {k + 1}...")
            k += 1  # Incrementar contador de gráficos
            fig, ax = plt.subplots()
            data1 = LRnorm[~np.isnan(LRnorm)]
            data2 = HRnorm[~np.isnan(HRnorm)]

            h_LR, _ = shapiro(data1)
            h_HR, _ = shapiro(data2)

            if h_LR > 0.05 and h_HR > 0.05:
                _, p = ttest_ind(data1, data2)
            else:
                p, _ = ranksums(data1, data2)

            meanData = [np.mean(data1), np.mean(data2)]
            semData = [np.std(data1) / np.sqrt(len(data1)), np.std(data2) / np.sqrt(len(data2))]
            # Personalizacion del grafico como colores, tamaño, se agrega el SEM 
            if h_LR > 0.05 and h_HR > 0.05:
                ax.bar(1, meanData[0], color='blue', edgecolor='blue', linewidth=3, width=0.5)
                ax.bar(2, meanData[1], color='red', edgecolor='red', linewidth=3, width=0.5)
                ax.errorbar(1, meanData[0], yerr=semData[0], fmt='none', capsize=30, linewidth=3, color='blue')
                ax.errorbar(2, meanData[1], yerr=semData[1], fmt='none', capsize=30, linewidth=3, color='red')
            else:
                group_data = np.concatenate([data1, data2])
                group_labels = np.concatenate([np.ones(len(data1)), np.ones(len(data2)) * 2])
                ax.boxplot(group_data, labels=['LR', 'HR'], widths=0.5, patch_artist=True, boxprops=dict(linewidth=2.5))

            # Configuración de bordes y ejes
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            ax.spines['bottom'].set_linewidth(3)
            ax.spines['left'].set_linewidth(3)

            # Ajustar límites de los ejes X e Y
            ax.set_ylim([0, max(meanData) * 2])  # Límites dinámicos para el eje Y
            ax.set_xticks([1, 2])
            ax.set_xticklabels(['LR', 'HR'])
            ax.tick_params(axis='both', labelsize=14)
            ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            
            # Dependiendo de la proteína agrega los ejes X e Y
            if prot == 1:
                ax.set_ylabel('Niveles de GRK2/Proteína total', fontsize=15, fontweight='bold')
            elif prot == 2:
                ax.set_ylabel('Niveles de GRK5/Proteína total', fontsize=15, fontweight='bold')
            else:
                ax.set_ylabel('D2R/Proteína total', fontsize=15, fontweight='bold')

            if f == 1:
                ax.set_title('Fracción Citosólica', fontsize=15, fontweight='bold')
            else:
                ax.set_title('Fracción Sináptica', fontsize=15, fontweight='bold')

            # Agregar significancia del t-test
            if p < 0.05:
                max_y = max(meanData) * 1.5
                if p < 0.001:
                    ax.text(2, max_y, '***', ha='center', fontsize=30, fontweight='bold')
                elif p < 0.01:
                    ax.text(2, max_y, '**', ha='center', fontsize=30, fontweight='bold')
                else:
                    ax.text(2, max_y, '*', ha='center', fontsize=30, fontweight='bold')

            # Guardar figura del gráfico 1
            output_folder = os.path.join(folder, 'Figuras_Generadas')
            os.makedirs(output_folder, exist_ok=True)
            fig.savefig(os.path.join(output_folder, f'01_Figure_{prot}_{f}_{n}.pdf'), format='pdf')
            plt.close(fig)
            
            # Gráfico 2: Correlación HRLR
            print("    Generando gráfico de correlación HR/LR...")
            normdata2[:, 0] = LocOFdata[:len(normdata2), 1]
            HRLR = normdata2[np.concatenate([valid_fp33, valid_fp66]), :]
            HRLR = HRLR[HRLR[:, 1] > 0, :]
            HRLR[:, 1] = HRLR[:, 1] / np.mean(HRLR[:, 1])

            fig, ax = plt.subplots()
            ax.scatter(HRLR[:, 0], HRLR[:, 1], edgecolor='k', facecolor='none', s=75)
            ax.spines['top'].set_visible(False)  # Ocultar el borde superior
            ax.spines['right'].set_visible(False)  # Ocultar el borde derecho
            ax.spines['bottom'].set_linewidth(2)  # Ancho del borde inferior
            ax.spines['left'].set_linewidth(2)  # Ancho del borde izquierdo


            #Análisis estadistico test de Shapiro-Wilk y posterior análisis de correlación
            h_HRLR, _ = shapiro(HRLR[:, 1])
            stat.append(h_HRLR)

            if h_HRLR > 0.05:
                r, p = pearsonr(HRLR[:, 0], HRLR[:, 1])
                if p < 0.05:
                    slope, intercept, _, _, _ = linregress(HRLR[:, 0], HRLR[:, 1])
                    y_fit = slope * HRLR[:, 0] + intercept
                    ax.plot(HRLR[:, 0], y_fit, 'r-', linewidth=2)
            else:
                r, p = spearmanr(HRLR[:, 0], HRLR[:, 1])
                if p < 0.05:
                    slope, intercept, _, _, _ = linregress(HRLR[:, 0], HRLR[:, 1])
                    y_fit = slope * HRLR[:, 0] + intercept
                    ax.plot(HRLR[:, 0], y_fit, 'r-', linewidth=2)

            if prot == 1:
                ax.set_ylabel('Niveles de GRK2/Proteína total', fontsize=12)
            elif prot == 2:
                ax.set_ylabel('Niveles de GRK5/Proteína total', fontsize=12)
            else:
                ax.set_ylabel('D2R/Proteína total', fontsize=12)
            ax.set_xlabel('Actividad total (m)', fontsize=12)
            ax.set_title(f'r = {r:.2f}, p = {p:.4f}', fontsize=12)

            # Guardar figura del gráfico 2
            fig.savefig(os.path.join(output_folder, f'02_FigureCorr_{prot}_{f}_{n}.pdf'), format='pdf')
            plt.close(fig)