-- Lists all bands with Glam as their main style, ranked by their longevity

SELECT band_name, (IFNULL(split, 2023) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';
