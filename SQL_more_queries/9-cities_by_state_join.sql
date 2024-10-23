-- script que imprime todas las ciudades contendias en la base de datos
SELECT cities.id, cities.name, states.name FROM cities, states
WHERE cities.state_id = states.id ORDER BY cities.id ASC;