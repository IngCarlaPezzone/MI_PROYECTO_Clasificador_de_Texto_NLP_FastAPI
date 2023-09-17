CREATE TABLE predicciones(
	id SERIAL PRIMARY KEY,
    texto VARCHAR(255),
    resultado VARCHAR(50),
    probabilidad_formateada FLOAT,
    calificacion VARCHAR(255)
);

SELECT * FROM predicciones;