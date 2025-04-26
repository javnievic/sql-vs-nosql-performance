# Proyecto de Comparación de Bases de Datos (SQL vs NoSQL)

Este proyecto compara el rendimiento de inserciones en bases de datos SQL (MySQL) y NoSQL (MongoDB).

## Requisitos

Para ejecutar este proyecto, necesitarás tener instaladas las siguientes dependencias:

- [Python 3.x](https://www.python.org/downloads/)
- [MySQL](https://dev.mysql.com/downloads/)
- [MongoDB](https://www.mongodb.com/try/download/community)

Asegúrate de tener un entorno virtual configurado e instalar las dependencias con:
```bash
pip install -r requirements.txt
```
## Configuración de la Base de Datos MySQL
Tienes dos formas de configurar la base de datos y el usuario para MySQL:

### Opción A: Ejecutando el script automático

En la raíz del proyecto, encontrarás el archivo `setup_comparativa.bat`. Puedes ejecutarlo directamente con doble clic, o desde la terminal con:
```bash
.\setup_comparativa.bat
```
Este script creará automáticamente la base de datos `mysql_db` y el usuario `mysql_user` con la contraseña `mysql_password`, con usuario y contraseña `root` de mysql.

### Opción B: Manualmente desde MySQL
1. **Accede a MySQL como root:**
  ```bash
   mysql -u root -p
  ```
2. **Crear la base de datos y el usuario:**

   Ejecuta los siguientes comandos dentro de la consola MySQL:
   ```sql
   DROP DATABASE IF EXISTS mysql_db;
   DROP USER IF EXISTS 'mysql_user'@'localhost';
   CREATE DATABASE mysql_db;
   CREATE USER 'mysql_user'@'localhost' IDENTIFIED BY 'mysql_password';
   GRANT ALL PRIVILEGES ON mysql_db.* TO 'mysql_user'@'localhost';
   FLUSH PRIVILEGES;
   EXIT;
   ```

   Esto creará la base de datos `mysql_db` y el usuario `mysql_user` con la contraseña `mysql_password`.

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

## Realizar las Migraciones en Django

1. Asegúrate de que el entorno virtual esté activado:
   ```bash
   .\venv\Scripts\activate
   
2. Crea las migraciones para la base de datos:  
   python manage.py makemigrations

3. Aplica las migraciones a la base de datos:  
   python manage.py migrate

## Ejecutar los Test de Comparación (Python)
Para ejecutar diferentes pruebas de rendimiento en SQL y MongoDB con parámetros específicos, puedes usar el siguiente comando:
```bash
python main.py --test <tipo_de_test> --num <número_de_registros> --repeticiones <número_de_repeticiones>
```
### Opciones de --test:
- `insert`: Prueba de inserción — parámetros: `--num`, `--repeticiones`
- `read_simple`: Prueba de lectura simple — parámetros: `--repeticiones`
- `read_filter`: Prueba de lectura con filtros — parámetros: `--repeticiones`
- `read_complex`: Prueba de lectura compleja — parámetros: `--repeticiones`
- `update_single`: Prueba de actualización simple — parámetros: `--repeticiones`
- `update_multiple`: Prueba de actualización múltiple — parámetros: `--num`, `--repeticiones`
- `update_complex`: Prueba de actualización compleja — parámetros: `--repeticiones`
- `delete_multiple`: Prueba de eliminación múltiple — parámetros: `--num`, `--repeticiones`
- `delete_all`: Prueba de eliminación total — parámetros: `--repeticiones`

#### Parámetros:
`--num`: Número de registros (para insert, delete_multiple, y update_multiple).
`--repeticiones`: Número de repeticiones para las pruebas.

### Ejemplo:
```bash
python main.py --test insert --num 1000 --repeticiones 10
```

## Notas

- Este proyecto está diseñado para realizar comparaciones de rendimiento entre bases de datos SQL y NoSQL en función de las operaciones de inserción.
- Los tiempos de inserción se graficarán automáticamente al ejecutar las pruebas.
