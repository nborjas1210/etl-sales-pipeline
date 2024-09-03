from extract import extract_data
from transform import transform_data
from load import load_data
from pathlib import Path

def run_etl():
    # Obtener la ruta absoluta al archivo de datos
    data_path = Path(__file__).parent.parent / 'data/raw/Online_retail.xlsx'

    # Extracción
    df_extracted = extract_data(data_path)
    if df_extracted is None:
        return
    
    # Transformación
    df_transformed = transform_data(df_extracted)
    
    # Carga
    load_data(df_transformed)

if __name__ == "__main__":
    run_etl()
