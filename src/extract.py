import pandas as pd
from pathlib import Path

def extract_data(file_path):
    """
    Extrae datos desde un archivo Excel.

    Args:
        file_path (str): Ruta al archivo Excel.

    Returns:
        pd.DataFrame: DataFrame con los datos extraídos.
    """
    data_path = Path(file_path)
    if not data_path.exists():
        print(f"Error: El archivo no existe en la ruta: {data_path}")
        return None

    try:
        df = pd.read_excel(data_path)
        print("Datos extraídos correctamente.")
        return df
    except Exception as e:
        print(f"Error en la extracción de datos: {e}")
        return None

if __name__ == "__main__":
    # Llamada a la función con el argumento de la ruta del archivo
    data = extract_data('../data/raw/Online_retail.xlsx')
