SELECT
    State_Name,
    Season,
    SUM(Production) AS Total_Production
FROM crop_production
GROUP BY State_Name, Season
ORDER BY State_Name, Total_Production DESC;