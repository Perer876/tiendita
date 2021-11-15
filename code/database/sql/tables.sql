CREATE TABLE IF NOT EXISTS producto (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR (255) NOT NULL,
    precio DECIMAL (8,2) UNSIGNED NOT NULL,
    codigo VARCHAR (13)
);

CREATE TABLE IF NOT EXISTS venta (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fecha_realizada DATETIME NOT NULL,
    total DECIMAL (10,2) UNSIGNED
);

CREATE TABLE IF NOT EXISTS lista_productos (
    id_venta INT UNSIGNED NOT NULL,
    id_producto INT UNSIGNED NOT NULL,
    precio_producto DECIMAL (8,2) UNSIGNED NOT NULL,
    cantidad INT UNSIGNED NOT NULL,
    FOREIGN KEY (id_venta) REFERENCES venta(id),
    FOREIGN KEY (id_producto) REFERENCES producto(id)
);
