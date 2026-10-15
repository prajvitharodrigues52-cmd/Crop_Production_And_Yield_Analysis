SELECT
    Crop_Year,
    SUM(Production) AS Total_Production
FROM crop_production
GROUP BY Crop_Year
ORDER BY Crop_Year;