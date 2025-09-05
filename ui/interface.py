import pandas as pd

def get_user_input():
    """
    Solicita al usuario el departamento y el número de registros.
    Valida que el número de registros sea un entero válido.

    Returns:
        tuple: Una tupla conteniendo (departamento, limite_registros).
    """
    print("="*40)
    print("CONSULTA DE CASOS DE COVID-19 EN COLOMBIA")
    print("="*40)
    
    departamento = input("Ingrese el nombre del Departamento que desea consultar: ").strip()
    
    while True:
        try:
            limite_registros = int(input("Ingrese el Número de Registros a obtener: ").strip())
            if limite_registros > 0:
                return departamento, limite_registros
            else:
                print("Error: Por favor, ingrese un número mayor a cero.")
        except ValueError:
            print("Error: El número de registros debe ser un valor numérico entero.")

def display_data(df: pd.DataFrame):
    """
    Muestra los datos del DataFrame en un formato limpio, seleccionando y
    renombrando las columnas solicitadas.

    Args:
        df (pandas.DataFrame): El DataFrame con los datos de la API.
    """
    print("\n--- Resultados de la Consulta ---")
    
    # Si el DataFrame esta vacio, no hay nada que mostrar
    if df.empty:
        print("No se encontraron resultados para los criterios de búsqueda.")
        return

    # Columnas de interes de la API y su nuevo nombre
    columnas_requeridas = {
        'ciudad_de_ubicaci_n': 'Ciudad de ubicación',
        'departamento_nom': 'Departamento',
        'edad': 'Edad',
        'tipo_de_contagio': 'Tipo',
        'estado': 'Estado',
        'pa_s_de_procedencia': 'País de procedencia'
    }

    # Filtar el DataFrame para quedar solo con las columnas que existen en los datos
    columnas_existentes = [col for col in columnas_requeridas.keys() if col in df.columns]
    df_filtrado = df[columnas_existentes]

    # Aca renombro las columnas para que sean más legibles
    df_formateado = df_filtrado.rename(columns=columnas_requeridas)
    
    # Imprimimos el resultado. Pandas lo formatea automáticamente como una tabla.
    # Usamos to_string() para asegurar que se muestren todas las filas y columnas.
    print(df_formateado.to_string(index=False))
    print("="*40)
