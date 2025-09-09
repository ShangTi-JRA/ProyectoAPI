import pandas as pd
from sodapy import Socrata

# El identificador del conjunto de datos de COVID-19 en Colombia
DATASET_ID = "gt2j-8ykr"
# El dominio del portal de Datos Abiertos
API_DOMAIN = "www.datos.gov.co"

def get_covid_data(departamento: str, limite: int):
    """
    Consulta la API de Datos Abiertos para obtener casos de COVID-19.

    Args:
        departamento (str): El nombre del departamento a consultar.
        limite (int): El número máximo de registros a obtener.

    Returns:
        pandas.DataFrame: Un DataFrame con los datos obtenidos o un DataFrame vacío si no hay resultados.
    """
    try:
        # Se crea un cliente para la API sin autenticación (para datos públicos)
        client = Socrata(API_DOMAIN, None)

        # La API espera el nombre del departamento en mayúsculas
        departamento_upper = departamento.upper()

        # Se realiza la consulta (get) al dataset usando el ID
        # El parámetro de la API para el nombre del departamento es 'departamento_nom'
        results = client.get(
            DATASET_ID,
            limit=limite,
            departamento_nom=departamento_upper
        )

        # Se convierten los resultados (una lista de diccionarios) en un DataFrame de pandas
        if results:
            return pd.DataFrame.from_records(results)
        else:
            return pd.DataFrame() # Retorna un DataFrame vacío si no hay resultados

    except Exception as e:
        print(f"Ocurrió un error al consultar la API: {e}")
        return pd.DataFrame() # Retorna DataFrame vacío en caso de error