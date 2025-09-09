from ui import interface
from api import logic

def main():
    """
    Función principal que ejecuta el flujo de la aplicación.
    """
    # Obtener los datos del usuario a través del módulo de UI
    departamento, limite = interface.get_user_input()
    
    # Informar al usuario que la consulta está en proceso
    print(f"\nConsultando {limite} registros para el departamento de '{departamento}'")
    
    # Obtener los datos de la API a través del módulo de lógica
    data_df = logic.get_covid_data(departamento, limite)
    
    # Mostrar los resultados al usuario a través del módulo de UI
    interface.display_data(data_df)

if __name__ == "__main__":
    main()