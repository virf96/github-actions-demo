from datetime import datetime, timezone

import pandas as pd

from config import API_NAME, BUCKET_NAME
from storage import upload_parquet


def prepara_silver(data):
    """Preprocesa y estructura los datos para la capa Silver."""
    registros = []
    for item in data:
        registros.append({
            "user_id": item.get("userId"),
            "post_id": item.get("id"),
            "title": item.get("title", "").strip(),
            "body": item.get("body", "").strip(),
        })
    return registros


def guardar_silver(data):
    """Guarda el JSON preprocesado en la capa Silver como Parquet."""
    hoy = datetime.now(timezone.utc)
    ruta = (
        f"Silver/{API_NAME}/"
        f"{hoy.year}/"
        f"{hoy.month:02d}/"
        f"{hoy.day:02d}/"
        "posts.parquet"
    )

    df = pd.DataFrame(prepara_silver(data))
    upload_parquet(ruta, df)
    print(f"Archivo Silver guardado en gs://{BUCKET_NAME}/{ruta}")
