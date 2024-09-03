from pathlib import Path
from sqlalchemy import create_engine

def load_data(df):
    """
    Carga los datos transformados en una base de datos SQLite.

    Args:
        df (pd.DataFrame): DataFrame con los datos transformados.
        db_path (str): Ruta a la base de datos SQLite.

    Returns:
        None
    """
    # Obtener la ruta absoluta al archivo de la base de datos
    db_path = Path(__file__).parent.parent / 'data/processed/sales.db'
    
    # Asegurarse de que el directorio existe
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Crear la cadena de conexión
    db_uri = f"sqlite:///{db_path.resolve()}"
    
    try:
        engine = create_engine(db_uri)
        df.to_sql('sales', con=engine, if_exists='replace', index=False)
        print(f"Datos cargados correctamente en la base de datos en {db_path.resolve()}.")
    except Exception as e:
        print(f"Error en la carga de datos: {e}")
