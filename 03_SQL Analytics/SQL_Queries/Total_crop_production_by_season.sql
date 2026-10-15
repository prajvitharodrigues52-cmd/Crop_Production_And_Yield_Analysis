SELECT
    Season,
    SUM(Production) AS Total_Production
FROM crop_production
GROUP BY Season
ORDER BY Total_Production DESC;