-- script que crea una tabla id_not_null en el servidor SQL
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
