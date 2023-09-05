SELECT
    category,
    method,
    year,
    SUM(accumulated_depreciation) AS accumulated_depreciation
FROM (
    SELECT
        category,
        method,
        year, 
        SUM(
            CASE
                WHEN method = 'straight-line' THEN (original_value - residual_value) * (useful_life / 12)
                WHEN method = 'accelerated' THEN (original_value - residual_value) * 2 * (1 - EXP(-useful_life / 5))
                ELSE 0
            END
        ) AS accumulated_depreciation
    FROM depreciated_assets
    WHERE business_id = 1
    GROUP BY category, method, year 
) AS accumulated_depreciation_table
JOIN (
    SELECT
        category,
        method,
        year, 
        SUM(original_value) AS original_value,
        SUM(residual_value) AS residual_value,
        SUM(useful_life) AS useful_life
    FROM depreciated_assets
    WHERE business_id = 1
    GROUP BY category, method, year
) AS asset_values_table
ON accumulated_depreciation_table.category = asset_values_table.category
    AND accumulated_depreciation_table.method = asset_values_table.method
    AND accumulated_depreciation_table.year = asset_values_table.year;
