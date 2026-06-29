import json
from datetime import datetime, timezone

from config import API_NAME, BUCKET_NAME
from storage import upload_json


def guardar_bronze(data):
    """Guarda el JSON original en la capa Bronze."""
    hoy = datetime.now(timezone.utc)
    ruta = (
        f"Bronze/{API_NAME}/"
        f"{hoy.year}/"
        f"{hoy.month:02d}/"
        f"{hoy.day:02d}/"
        "posts.json"
    )
    upload_json(ruta, json.dumps(data, indent=4))
    print(f"Archivo guardado en gs://{BUCKET_NAME}/{ruta}")
