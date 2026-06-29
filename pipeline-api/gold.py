from google.cloud import bigquery

from config import PROJECT_ID, DATASET


def ejecutar_sql(path_sql):
    client = bigquery.Client(project=PROJECT_ID)

    with open(path_sql, "r", encoding="utf-8") as file:
        query = file.read()

    job = client.query(query)
    job.result()

    print(f"SQL ejecutado correctamente: {path_sql}")


def actualizar_gold():
    ejecutar_sql("sql/create_schema.sql")
    ejecutar_sql("sql/create_posts_silver_ext.sql")
    ejecutar_sql("sql/gold_posts.sql")
    ejecutar_sql("sql/gold_users.sql")