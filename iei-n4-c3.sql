-- SCRIPT SQL: Creación de usuario y Permisos.

-- 1. Crear el usuario para la aplicación (compatible con WampServer / localhost)
CREATE USER IF NOT EXISTS 'iei-n4-c3'@'localhost' IDENTIFIED BY 'Primavera2026';

-- 2. Asignar todos los privilegios al usuario sobre la base de datos
GRANT ALL PRIVILEGES ON iei_n4_c3.* TO 'iei-n4-c3'@'localhost';

-- 3. Actualizar los privilegios en el servidor MySQL
FLUSH PRIVILEGES;