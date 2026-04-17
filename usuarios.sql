DROP DATABASE IF EXISTS usuariosdb;
CREATE DATABASE IF NOT EXISTS usuariosdb;
USE usuariosdb;

CREATE TABLE IF NOT EXISTS usuarios(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre varchar(100) NOT NULL,
    email varchar(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS ranking(
    id_usuario INT,
    puntos INT NULL DEFAULT 0,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
);


INSERT INTO usuarios(nombre, email) values
("Javi","Javi@fi.uba.ar"),
("Marcos ","Marcos@fi.uba.ar"),
("Lucas","Lucas@fi.uba.ar"),
("Sofia","Sofia@fi.uba.ar");

INSERT INTO ranking(id_usuario) values
(1),
(2),
(3),
(4);
