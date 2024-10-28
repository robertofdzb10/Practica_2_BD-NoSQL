---
# Práctica: Bases de Datos NoSQL - Jugadoras de Fútbol en Europa

Este repositorio contiene el desarrollo de una práctica sobre bases de datos NoSQL. La base de datos seleccionada es **MongoDB**, y el objetivo es modelar, insertar y consultar información sobre jugadoras de fútbol en Europa. Este ejercicio permite explorar el uso de MongoDB para almacenar datos semi-estructurados de manera eficiente.

## Estructura del Proyecto

- **`scripts/`**: Contiene los scripts de Python para insertar registros desde un archivo CSV en MongoDB.
- **`queries/`**: Incluye las consultas y modificaciones en MongoDB, documentadas y explicadas.
- **`README.md`**: Este archivo, con la descripción general y pasos para ejecutar el proyecto.
- **`requirements.txt`**: Archivo con las dependencias necesarias para el entorno Python.

## Requisitos

- **MongoDB**: Se debe tener MongoDB instalado y en ejecución (local o en servidor).
- **Python 3.8+**
- **Dependencias**: Se pueden instalar las dependencias ejecutando:
  ```bash
  pip install -r requirements.txt
  ```

## Configuración de la Base de Datos

1. **Conexión a MongoDB**: Asegúrate de tener MongoDB ejecutándose. Puedes modificar la URL de conexión en el script para conectar a un servidor remoto si es necesario.
   
2. **Estructura del Esquema**: No es necesario definir un esquema rígido en MongoDB, pero los documentos siguen esta estructura general:
    ```json
    {
      "_id": "uuid",
      "dni": "string",
      "nombre": "string",
      "apellido": "string",
      "edad": "int",
      "ocupacion": "string",
      "equipo": {
        "nombre": "string",
        "pais": "string",
        "start_year": "int"
      },
      "condicion_fisica": {
        "peso": "float",
        "altura": "float",
        "enfermedades": ["string"],
        "categoria": "string",
        "grupo_sanguineo": "string"
      },
      "estadisticas": {
        "posesion_porcentaje": "float",
        "goles": "int",
        "pases": "int"
      },
      "lesiones": [
        {
          "tipo_lesion": "string",
          "fecha_inicio": "date",
          "fecha_fin": "date",
          "descripcion": "string",
          "retorno_estimado": "string"
        }
      ]
    }
    ```

## Ejecución de los Scripts

1. **Inserción de Datos desde CSV**:
   - Coloca tu archivo `jugadoras.csv` en el directorio `scripts/`.
   - Ejecuta el script para insertar registros:
     ```bash
     python scripts/insert_data.py
     ```
   - Este script lee los datos desde el archivo CSV y los inserta en la colección `jugadoras` de MongoDB.

2. **Consultas y Modificaciones**:
   - Las consultas y modificaciones se encuentran en el archivo `queries/queries.md`.
   - Ejemplos de ejecución:
     - **Modificar nombre de jugadoras a mayúsculas**:
       ```javascript
       db.jugadoras.updateOne(
         { dni: "12345678A" },
         { $set: { nombre: { $toUpper: "$nombre" } } }
       );
       ```

     - **Consulta de jugadoras en equipos que empiecen con "Manchester"**:
       ```javascript
       db.jugadoras.find({
         "equipo.nombre": { $regex: /^Manchester/, $options: "i" }
       });
       ```

## Optimización con Índices

Para mejorar el rendimiento de las consultas, se agregaron índices en los siguientes campos:
- **`dni`**: Acceso directo a registros.
- **`equipo.nombre`**: Búsquedas por equipo.
- **`equipo.pais`**: Filtrado por país.
- **`equipo.start_year`**: Filtrado por año de inicio.

Para verificar los tiempos de ejecución, utiliza `explain("executionStats")` en MongoDB, como en el siguiente ejemplo:

```javascript
db.jugadoras.find({
  "equipo.nombre": { $regex: /^Manchester/, $options: "i" }
}).explain("executionStats")
```

## Conclusión

MongoDB es una opción ideal para este caso de uso, proporcionando flexibilidad, escalabilidad y un excelente rendimiento en consultas. Este repositorio demuestra cómo modelar datos de jugadoras de fútbol y optimizar consultas mediante índices en MongoDB.

---
