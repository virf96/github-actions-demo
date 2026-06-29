import requests

from bronze import guardar_bronze
from config import URL
from silver import guardar_silver
from gold import actualizar_gold


def consumir_api():
    response = requests.get(URL, timeout=30)
    response.raise_for_status()
    return response.json()


def main():
    print("Consumiendo API...")

    datos = consumir_api()
    print(f"Registros obtenidos: {len(datos)}")

    guardar_bronze(datos)
    guardar_silver(datos)
    actualizar_gold()

    print("Proceso finalizado correctamente.")


if __name__ == "__main__":
    main()