SELECT
    State_Name,
    COUNT(DISTINCT Crop) AS Number_of_Crops
FROM crop_production
GROUP BY State_Name
ORDER BY Number_of_Crops DESC;