from google.cloud import bigquery

from config import PROJECT_ID


def execute_sql_file(path_sql):
    client = bigquery.Client(project=PROJECT_ID)

    with open(path_sql, "r", encoding="utf-8") as file:
        query = file.read()

    job = client.query(query)
    job.result()

    print(f"BigQuery: SQL ejecutado correctamente: {path_sql}")


def actualizar_gold():
    execute_sql_file("sql/create_schema.sql")
    execute_sql_file("sql/create_posts_silver_ext.sql")
    execute_sql_file("sql/gold_posts.sql")
    execute_sql_file("sql/gold_users.sql")
