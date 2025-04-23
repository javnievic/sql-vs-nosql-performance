# Proyecto de Comparación de Bases de Datos (SQL vs NoSQL)

Este proyecto compara el rendimiento de inserciones en bases de datos SQL (MySQL) y NoSQL (MongoDB).

## Requisitos

Para ejecutar este proyecto, necesitarás tener instaladas las siguientes dependencias:

- Python 3.x
- MySQL
- MongoDB

Asegúrate de tener un entorno virtual configurado e instalar las dependencias con:
```bash
pip install -r requirements.txt
```
## Configuración de la Base de Datos MySQL

1. **Accede a MySQL como root:**
  ```bash
   mysql -u root -p
  ```
2. **Crear la base de datos y el usuario:**

   Ejecuta los siguientes comandos dentro de la consola MySQL:
   ```sql
   DROP DATABASE IF EXISTS db_mysql;
   CREATE DATABASE db_mysql;
   CREATE USER 'mysql_user'@'localhost' IDENTIFIED BY 'mysql_password';
   GRANT ALL PRIVILEGES ON db_mysql.* TO 'mysql_user'@'localhost';
   FLUSH PRIVILEGES;
   EXIT;
   ```

   Esto creará la base de datos `db_mysql` y el usuario `mysql_user` con la contraseña `mysql_password`.

## Ejecutar el Servidor de MongoDB

1. Navega a la carpeta donde tienes MongoDB instalado, por ejemplo:
   ```bash
   cd C:\Program Files\MongoDB\Server\8.0\bin
   ```
2. Ejecuta el servidor de MongoDB:
   ```bash
   mongod
   ```
   Esto arrancará el servidor de MongoDB.

## Probar la Inserción en MySQL

1. Asegúrate de que el entorno virtual esté activado:
   ```bash
   .\venv\Scripts\activate

2. Ejecuta la shell de Django:
   ```bash
   python manage.py shell

3. Dentro de la shell, importa la función de prueba de SQL y ejecútala:
   ```bash
   from app.tests.test_sql import test_sql_insert
   test_sql_insert()
   ```

   Esto ejecutará las pruebas de inserción en MySQL y mostrará los tiempos de inserción.

## Probar la Inserción en MongoDB

1. Asegúrate de que MongoDB esté corriendo (`mongod`).
2. Ejecuta el script de prueba para MongoDB para medir el tiempo de inserción en la base de datos NoSQL:
   ```bash
   python app/tests/test_mongo.py

## Notas

- Este proyecto está diseñado para realizar comparaciones de rendimiento entre bases de datos SQL y NoSQL en función de las operaciones de inserción.
- Los tiempos de inserción se graficarán automáticamente al ejecutar las pruebas.
