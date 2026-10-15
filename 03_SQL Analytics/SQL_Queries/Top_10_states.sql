SELECT
    State_Name,
    SUM(Production) AS Total_Production
FROM crop_production
GROUP BY State_Name
ORDER BY Total_Production DESC
LIMIT 10;