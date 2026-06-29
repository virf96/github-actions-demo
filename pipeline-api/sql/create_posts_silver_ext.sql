CREATE OR REPLACE EXTERNAL TABLE `project-73c1e9e8-7da9-4b68-ad8.datos_pipeline.posts_silver_ext`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://datos-002/Silver/jsonplaceholder/2026/06/29/posts.parquet']
);