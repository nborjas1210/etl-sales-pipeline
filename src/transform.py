import pandas as pd

def transform_data(df):
    """
    Transforma los datos extraídos.

    Args:
        df (pd.DataFrame): DataFrame con los datos extraídos.

    Returns:
        pd.DataFrame: DataFrame transformado.
    """
    # Eliminación de filas con valores nulos en campos clave
    df.dropna(subset=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'], inplace=True)
    
    # Conversión de tipos de datos
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['CustomerID'] = df['CustomerID'].astype(int)
    
    # Eliminación de duplicados
    df.drop_duplicates(inplace=True)
    
    # Agregación: Crear columna 'TotalPrice'
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    
    print("Datos transformados correctamente.")
    return df

if __name__ == "__main__":
    df = pd.read_csv('../data/processed/extracted_data.csv')
    transformed_df = transform_data(df)
    transformed_df.to_csv('../data/processed/transformed_data.csv', index=False)
