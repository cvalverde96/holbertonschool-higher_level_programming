-- scipt que imprime lista de los records con la misma puntuacion que en la tabla second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;