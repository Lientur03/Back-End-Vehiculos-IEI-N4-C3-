-- 1. Crear la base de datos con soporte para caracteres especiales (tildes y eñes)
CREATE DATABASE IF NOT EXISTS iei_n4_c3 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 2. Seleccionar la base de datos creada
USE iei_n4_c3;

-- 3. Crear el usuario para la aplicación (compatible con WampServer / localhost)
CREATE USER IF NOT EXISTS 'iei-n4-c3'@'localhost' IDENTIFIED BY 'Primavera2026';

-- 4. Asignar todos los privilegios al usuario sobre la base de datos
GRANT ALL PRIVILEGES ON iei_n4_c3.* TO 'iei-n4-c3'@'localhost';

-- 5. Actualizar los privilegios en el servidor MySQL
FLUSH PRIVILEGES;