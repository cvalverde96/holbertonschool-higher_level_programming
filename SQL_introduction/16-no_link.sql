-- script que imprime todos los valores de la tabla second_table
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
