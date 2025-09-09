import pandas as pd
from sodapy import Socrata

# --- MAPA DE TRADUCCIÓN DE NOMBRE DE DEPARTAMENTO A CÓDIGO OFICIAL DIVIPOLA ---
DEPARTAMENTO_A_CODIGO = {
    'AMAZONAS': '91', 'ANTIOQUIA': '05', 'ARAUCA': '81', 'ATLANTICO': '08',
    'BARRANQUILLA': '08', 'BOGOTA D.C.': '11', 'BOLIVAR': '13', 'BOYACA': '15',
    'BUENAVENTURA': '76', 'CALDAS': '17', 'CAQUETA': '18', 'CARTAGENA': '13',
    'CASANARE': '85', 'CAUCA': '19', 'CESAR': '20', 'CHOCO': '27',
    'CORDOBA': '23', 'CUNDINAMARCA': '25', 'GUAINIA': '94', 'GUAVIARE': '95',
    'HUILA': '41', 'LA GUAJIRA': '44', 'MAGDALENA': '47', 'META': '50',
    'NARIÑO': '52', 'NORTE DE SANTANDER': '54', 'PUTUMAYO': '86', 'QUINDIO': '63',
    'RISARALDA': '66', 'SAN ANDRES Y PROVIDENCIA': '88', 'SANTA MARTA': '47',
    'SANTANDER': '68', 'SUCRE': '70', 'TOLIMA': '73', 'VALLE DEL CAUCA': '76',
    'VAUPES': '97', 'VICHADA': '99'
}

DATASET_ID = "gt2j-8ykr"
API_DOMAIN = "www.datos.gov.co"

def get_covid_data(departamento: str, limite: int):
    """
    Consulta la API de Datos Abiertos para obtener casos de COVID-19.
    Utiliza el código DIVIPOLA del departamento para una consulta robusta.
    """
    try:
        departamento_upper = departamento.upper()
        codigo_depto = DEPARTAMENTO_A_CODIGO.get(departamento_upper)

        if not codigo_depto:
            print(f"Error: El departamento '{departamento}' no es un nombre válido.")
            return pd.DataFrame()

        client = Socrata(API_DOMAIN, None)

        # El nombre de campo correcto para el código DIVIPOLA del departamento es 'departamento'.
        where_clause = f"departamento = '{codigo_depto}'"

        results = client.get(
            DATASET_ID,
            limit=limite,
            where=where_clause
        )

        if results:
            return pd.DataFrame.from_records(results)
        else:
            return pd.DataFrame()

    except Exception as e:
        print(f"Ocurrió un error al consultar la API: {e}")
        return pd.DataFrame()