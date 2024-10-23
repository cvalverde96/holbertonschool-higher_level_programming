-- creando un script que imprime lista de todas las ciudades de california
SELECT @california_id := id FROM states WHERE name = 'California';

SELECT id, name FROM cities WHERE state_id = @california_id ORDER BY id ASC;
