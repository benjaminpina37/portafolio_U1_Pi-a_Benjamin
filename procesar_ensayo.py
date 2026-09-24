import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def procesar_ensayo():
    # 1. Obtener la ruta raíz del proyecto (un nivel arriba de /src)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)

    # 2. Ruta exacta al archivo Excel original
    raw_path = os.path.join(
        project_root, 'data', 'raw', 'ensayo_hormigon.xlsx'
    )

    if not os.path.exists(raw_path):
        print(f'ERROR: No se encontró el archivo en: {raw_path}')
        print(
            'Verifica que el archivo ensayo_hormigon.xlsx esté dentro de la carpeta data/raw'
        )
        return

    df_raw = pd.read_excel(raw_path, sheet_name='Hoja1')

    # Extraer datos (filas 2 a 20, columnas A a C)
    df = df_raw.iloc[1:20, 0:3].copy()
    df.columns = ['tiempo_s', 'carga_kN', 'desplazamiento_mm']
    df = df.astype(float)

    # 3. Geometría de la probeta
    D = 150.0  # mm
    H = 300.0  # mm
    area_mm2 = np.pi * (D / 2) ** 2  # A = 17671.46 mm²

    # 4. Cálculos
    df['esfuerzo_MPa'] = (df['carga_kN'] * 1000.0) / area_mm2
    df['deformacion_unitaria'] = df['desplazamiento_mm'] / H

    # 5. Guardar CSV procesado
    processed_dir = os.path.join(project_root, 'data', 'processed')
    os.makedirs(processed_dir, exist_ok=True)
    df.to_csv(
        os.path.join(processed_dir, 'ensayo_procesado.csv'), index=False
    )

    # 6. Generar gráfico
    results_dir = os.path.join(project_root, 'results')
    os.makedirs(results_dir, exist_ok=True)

    plt.figure(figsize=(7, 4.5))
    plt.plot(
        df['desplazamiento_mm'],
        df['esfuerzo_MPa'],
        marker='o',
        linestyle='-',
        color='#1f77b4',
        label='Ensayo de Compresión',
    )

    plt.title('Curva Esfuerzo vs. Desplazamiento - Probeta de Hormigón')
    plt.xlabel('Desplazamiento $u$ [mm]')
    plt.ylabel('Esfuerzo Compresivo $\\sigma$ [MPa]')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()

    plt.savefig(
        os.path.join(results_dir, 'curva_esfuerzo_desplazamiento.png'), dpi=300
    )
    plt.close()

    f_c_max = df['esfuerzo_MPa'].max()
    print('--------------------------------------------------')
    print('¡Procesamiento completado con éxito!')
    print(f"Resistencia máxima calculada (f'c): {f_c_max:.2f} MPa")
    print('--------------------------------------------------')


if __name__ == '__main__':
    procesar_ensayo()
