SELECT * FROM data_analyst.sql;
SELECT 
    category,
    COUNT(*) AS total_orders,
    SUM(CASE WHEN return_id IS NOT NULL THEN 1 ELSE 0 END) AS returned_orders,
    ROUND(
        100.0 * SUM(CASE WHEN return_id IS NOT NULL THEN 1 ELSE 0 END) / COUNT(*), 
        2
    ) AS probability_of_return_percent
FROM 
    returns_data
GROUP BY 
    category;
