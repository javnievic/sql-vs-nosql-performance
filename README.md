# Proyecto de Comparación de Bases de Datos (SQL vs NoSQL)

Este proyecto tiene como objetivo comparar el rendimiento de las bases de datos MySQL y MongoDB para diversas operaciones como inserciones, lecturas, actualizaciones y eliminaciones. A través de pruebas de rendimiento y gráficas, el proyecto facilita la comparación del rendimiento entre ambas bases de datos.

## Requisitos previos

Para ejecutar este proyecto, necesitarás tener instaladas las siguientes dependencias:

- [Python 3.x](https://www.python.org/downloads/)
- [MySQL](https://dev.mysql.com/downloads/)
- [MongoDB](https://www.mongodb.com/try/download/community)

Se recomienda usar un entorno virtual para aislar las dependencias del proyecto:
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual en Windows
.\venv\Scripts\activate

# Activar entorno virtual en Linux/Mac
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

```
## Configuración de la Base de Datos MySQL
Tienes dos formas de configurar la base de datos y el usuario para MySQL:

### Opción A: Ejecutando el script automático (Windows)

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
   ```bash  
   python manage.py makemigrations

4. Aplica las migraciones a la base de datos:  
   ```bash
   python manage.py migrate

## Ejecutar los Test de Comparación (Python)
Para ejecutar diferentes pruebas de rendimiento en SQL y MongoDB con parámetros específicos, puedes usar el siguiente comando:
```bash
python main.py --test <tipo_de_test> --num <número_de_registros> --repeticiones <número_de_repeticiones>
```
Puedes ver la ayuda completa con:
```bash
python main.py --help
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

### Valores por defecto:

Los parámetros tienen valores por defecto si no se especifican al ejecutar los tests:

- `--num`: Si no se especifica, por defecto:
  - Para `insert`: 10000 registros
  - Para `delete_multiple` y `update_multiple`: 100 registros
  
- `--repeticiones`: Si no se especifica, por defecto:
  - Para `insert`: 5 repeticiones
  - Para otros tests: 20 repeticiones


### Ejemplos de Uso

#### Insertar 1000 registros, repitiendo 10 veces:
```bash
python main.py --test insert --num 1000 --repeticiones 10
```

#### Lectura simple, repitiendo 20 veces:
```bash
python main.py --test read_simple --repeticiones 20
```
#### Lectura filtrada, repitiendo 15 veces:
```bash
python main.py --test read_filter --repeticiones 15
```
#### Lectura compleja de relaciones, repitiendo 5 veces:
```bash
python main.py --test read_complex --repeticiones 5
```
#### Actualizar un solo documento 30 veces:
```bash
python main.py --test update_single --repeticiones 30
```
#### Actualizar 500 documentos en cada repetición (5 repeticiones):
```bash
python main.py --test update_multiple --num 500 --repeticiones 5
```
#### Actualización compleja de relaciones, 10 repeticiones:
```bash
python main.py --test update_complex --repeticiones 10
```
#### Eliminar 200 registros en cada repetición (5 repeticiones):
```bash
python main.py --test delete_multiple --num 200 --repeticiones 5
```
#### Eliminar todos los registros en cada repetición (3 repeticiones):
```bash
python main.py --test delete_all --repeticiones 3
```

## Notas

- Este proyecto está diseñado para realizar comparaciones de rendimiento entre bases de datos SQL y NoSQL en función de las operaciones de inserción.
- Los tiempos de inserción se graficarán automáticamente al ejecutar las pruebas.
