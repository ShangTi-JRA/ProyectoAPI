from ui import interface
from api import logic

def main():
    """
    Función principal que ejecuta el flujo de la aplicación.
    """
    # 1. Obtener los datos del usuario a través del módulo de UI
    departamento, limite = interface.get_user_input()
    
    # 2. Informar al usuario que la consulta está en proceso
    print(f"\nConsultando {limite} registros para el departamento de '{departamento}'...")
    print("Esto puede tardar unos segundos...")
    
    # 3. Obtener los datos de la API a través del módulo de lógica
    data_df = logic.get_covid_data(departamento, limite)
    
    # 4. Mostrar los resultados al usuario a través del módulo de UI
    interface.display_data(data_df)

# Este es el punto de entrada estándar para un script de Python
if __name__ == "__main__":
    main()