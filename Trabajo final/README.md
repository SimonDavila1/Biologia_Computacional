# Análisis de Datos de GRKs, D2r y Actividad Locomotora

Este proyecto analiza datos experimentales de proteínas (GRK2, GRK5 y D2R) en diferentes fracciones (citosólica y sináptica) y actividades (HR y LR). Utiliza herramientas estadísticas para evaluar normalidad, realizar comparaciones y generar gráficos visuales que resumen los resultados.

---

## Tabla de Contenido
1. [Descripción](#descripción)
2. [Características](#características)
3. [Requisitos](#requisitos)
4. [Estructura de los Archivos de Datos](#estructura-de-los-archivos-de-datos)
5. [Ejecución](#ejecución)
6. [Salida](#salida)
7. [Contacto](#contacto)

---

# Descripción

El script realiza un análisis estadístico y visualización basado en datos experimentales de proteínas. Procesa los datos para:
- Normalizar valores experimentales.
- Evaluar diferencias significativas entre las fracciones LR y HR.
- Establecer correlaciones entre la actividad HR y LR.

El objetivo es proporcionar una manera automatizada de evaluar y representar los datos de manera comprensible.

---

# Características

1. **Procesamiento de Datos**:
   - Normalización para evitar errores de división por cero.
   - Filtro dinámico para valores relevantes.
   
2. **Pruebas Estadísticas**:
   - Normalidad: Test de Shapiro-Wilk.
   - Comparaciones de medias: t-test o RankSums.
   - Correlaciones: Pearson o Spearman.

3. **Generación de Gráficos**:
   - Comparación de LR y HR con barras y error estándar de la media (SEM).
   - Correlación HR/LR con líneas de tendencia.

---

# Requisitos

Para ejecutar este script, asegúrate de tener instalado:

- **Python 3.x**
- Bibliotecas:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `scipy`

Instala las dependencias necesarias con:

pip install numpy pandas matplotlib scipy

---

# Estructura de los Archivos de Datos

El script requiere dos archivos CSV:

1. WBRdata_final.csv

	•	Contiene datos de GRKs, D2R y fracciones.
	•	Columnas relevantes:
	•	Columna 1: Identificador de muestra.
	•	Columna 2: Identificador de la proteína (1 para GRK2, 2 para GRK5, 3 para D2R).
	•	Columna 6: Identificador de fracción (1 para citosólica, 2 para sináptica).
	•	Columna 5: Datos para normalización en base a Rojo Ponceau S.

2. LocOFdata.csv

	•	Contiene datos de actividad.
	•	Columnas relevantes:
	•	Columna 1: Identificador de muestra.
	•	Columna 2: Valor de actividad.

---
# Ejecución

1.	Preparar Archivos:

Asegúrate de tener los archivos WBRdata_final.csv y LocOFdata.csv en la misma carpeta que el script.


2.	Ejecutar el Script:

   
Corre el script en la terminal, proporcionando las rutas de los archivos como argumentos:

python3 script.py WBRdata_final.csv LocOFdata.csv

El script:
	•	Normaliza y analiza los datos.
	•	Genera gráficos en formato PDF en una carpeta llamada Figuras_Generadas.

---

# Salida

El programa genera dos tipos de gráficos:

1. Comparación LR vs HR

	•	Barras para valores promedio de LR y HR.
	•	SEM representado como líneas de error.
	•	Significancia estadística por medio de t-test o ranksum indicada por *, ** o ***.

2. Correlación HR/LR
   

	•	Gráfico de dispersión mostrando la relación entre HR y LR.
	•	Línea de tendencia si la correlación es significativa en base a los análisis estadisticos de correlación de Pearson y Spearman.

Los gráficos se guardan en formato PDF en la carpeta Figuras_Generadas.

---
# Contacto
Para preguntas o problemas, contacta a Simón Dávila en davilasimon3@uc.cl
