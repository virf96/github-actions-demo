from google.cloud import bigquery

from config import DATASET, PROJECT_ID


def actualizar_gold():
    """Crea o actualiza la tabla Gold en BigQuery."""
    client = bigquery.Client(project=PROJECT_ID)

    query = f"""
    CREATE OR REPLACE TABLE `{PROJECT_ID}.{DATASET}.posts_gold` AS
    SELECT
        user_id,
        COUNT(*) AS total_posts,
        MIN(post_id) AS primer_post_id,
        MAX(post_id) AS ultimo_post_id
    FROM `{PROJECT_ID}.{DATASET}.posts_silver_ext`
    GROUP BY user_id
    ORDER BY user_id
    """

    job = client.query(query)
    job.result()

    print(f"Tabla Gold actualizada: {PROJECT_ID}.{DATASET}.posts_gold")
