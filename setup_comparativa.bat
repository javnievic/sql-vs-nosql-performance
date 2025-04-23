@echo off
echo Configurando base de datos en MySQL...

:: Definir variables
set MYSQL_USER=root
set MYSQL_PASSWORD=root

:: Crear archivo SQL temporal
(
    echo DROP DATABASE IF EXISTS mysql_db;
    echo DROP USER IF EXISTS 'mysql_user'@'localhost';
    echo CREATE DATABASE mysql_db;
    echo CREATE USER 'mysql_user'@'localhost' IDENTIFIED BY 'mysql_password';
    echo GRANT ALL PRIVILEGES ON mysql_db.* TO 'mysql_user'@'localhost';
    echo FLUSH PRIVILEGES;
) > temp.sql

:: Ejecutar el script SQL en MySQL
mysql -u %MYSQL_USER% -p%MYSQL_PASSWORD% < temp.sql

:: Eliminar archivo temporal
del temp.sql

echo Base de datos y usuario configurados correctamente.
pause
