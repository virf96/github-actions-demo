CREATE OR REPLACE TABLE `project-73c1e9e8-7da9-4b68-ad8.datos_pipeline.users_gold` AS
SELECT
    user_id,
    COUNT(*) AS total_posts,
    MIN(post_id) AS primer_post_id,
    MAX(post_id) AS ultimo_post_id
FROM `project-73c1e9e8-7da9-4b68-ad8.datos_pipeline.posts_silver_ext`
GROUP BY user_id
ORDER BY user_id;
