SELECT
    Crop,
    SUM(Production) AS Total_Production
FROM crop_production
GROUP BY Crop
ORDER BY Total_Production DESC
LIMIT 10;