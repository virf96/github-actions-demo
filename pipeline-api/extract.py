import requests

from bronze import guardar_bronze
from config import URL


def consumir_api():
    """Consume la API y devuelve la respuesta en formato JSON."""
    response = requests.get(URL, timeout=30)
    response.raise_for_status()
    return response.json()


def main():
    print("Extract: consumiendo API...")
    datos = consumir_api()
    print(f"Extract: registros obtenidos: {len(datos)}")
    guardar_bronze(datos)
    print("Extract: proceso finalizado.")


if __name__ == "__main__":
    main()
