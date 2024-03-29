-- SQL script that ranks country origins of bands,
SELECT DISTINCT `band_name`, IFNULL(`split`, 2020) - `formed` as `lifespan`
FROM `metal_bands`
WHERE FIND_IN_SET('Glam rock', style)
ORDER BY `lifespan` DESC;
