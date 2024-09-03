# Pipeline de ETL para Procesamiento de Datos de Ventas

## Introducción

Este proyecto desarrolla un pipeline ETL (Extract, Transform, Load) para procesar datos de ventas provenientes del dataset [Online Retail](https://archive.ics.uci.edu/ml/datasets/Online+Retail) del UCI Machine Learning Repository. El objetivo es extraer los datos, transformarlos para análisis y cargarlos en una base de datos relacional.

## Tecnologías Utilizadas

- **Lenguaje de Programación:** Python
- **Librerías:** pandas, sqlalchemy, sqlite3, matplotlib
- **Base de Datos:** SQLite
- **Entorno de Desarrollo:** Jupyter Notebook


## Requisitos

- Python 3.x
- Librerías listadas en `requirements.txt`

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/etl-sales-pipeline.git
    cd etl-sales-pipeline
    ```

2. Crea y activa un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Descarga el dataset [Online Retail](https://archive.ics.uci.edu/ml/datasets/Online+Retail) y colócalo en `data/raw/`.

## Uso

### Ejecutar el Pipeline ETL

```bash
python src/run_etl.py

