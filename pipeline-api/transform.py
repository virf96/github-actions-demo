import json
from datetime import datetime, timezone

import pandas as pd
from google.cloud import storage

from config import API_NAME, BUCKET_NAME
from storage import upload_parquet


def leer_bronze():
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)

    hoy = datetime.now(timezone.utc)
    ruta = (
        f"Bronze/{API_NAME}/"
        f"{hoy.year}/"
        f"{hoy.month:02d}/"
        f"{hoy.day:02d}/"
        "posts.json"
    )

    blob = bucket.blob(ruta)
    contenido = blob.download_as_text()
    return json.loads(contenido)


def prepara_silver(data):
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
    print(f"Transform: archivo Silver guardado en gs://{BUCKET_NAME}/{ruta}")


def main():
    print("Transform: leyendo Bronze...")
    datos = leer_bronze()
    print(f"Transform: registros leídos: {len(datos)}")
    guardar_silver(datos)
    print("Transform: proceso finalizado.")


if __name__ == "__main__":
    main()
