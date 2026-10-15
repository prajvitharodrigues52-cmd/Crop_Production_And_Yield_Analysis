SELECT
    Crop,
    Crop_Year,
    SUM(Production) AS Total_Production
FROM crop_production
GROUP BY Crop, Crop_Year
ORDER BY Crop, Crop_Year;