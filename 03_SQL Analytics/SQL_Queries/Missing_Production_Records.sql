SELECT
    State_Name,
    District_Name,
    Crop_Year,
    Season,
    Crop,
    Area,
    Production
FROM crop_production
WHERE Production IS NULL;