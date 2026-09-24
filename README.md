# Ensayo de Compresión Cilíndrica en Hormigón - Portafolio U1

## 1. Propósito del Proyecto
Este proyecto documenta y procesa de forma reproducible el ensayo de compresión axial realizado a una probeta cilíndrica de hormigón. Su objetivo es calcular la curva esfuerzo-desplazamiento y determinar la resistencia máxima a la compresión 

## 2. Datos de Entrada (Inputs)
- **Archivo origen**: `data/raw/ensayo_hormigon.xlsx` (Preservado sin modificaciones).
- **Parámetros Geométricos**:
  - Diámetro de la probeta ($D$): 150
  - Altura de la probeta ($H$): 300
  - Área transversal ($A$): $A =  17671.46

## 3. Procedimiento de Ejecución
Para reproducir el análisis desde cero:
1. Clonar este repositorio.
2. Asegurarse de tener instalado Python 3.x con las librerías `pandas`, `matplotlib`, `numpy` y `openpyxl`.
3. Ejecutar el script principal:
   ```bash
   python src/procesar_ensayo.py
