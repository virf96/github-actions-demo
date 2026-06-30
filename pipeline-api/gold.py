from google.cloud import bigquery

from bigquery import execute_sql_file


def main():
    print("Gold: ejecutando consultas SQL...")
    execute_sql_file("sql/create_schema.sql")
    execute_sql_file("sql/create_posts_silver_ext.sql")
    execute_sql_file("sql/gold_posts.sql")
    execute_sql_file("sql/gold_users.sql")
    print("Gold: proceso finalizado.")


if __name__ == "__main__":
    main()
