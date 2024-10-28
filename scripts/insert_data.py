import csv
from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['futbol']
jugadoras = db['jugadoras']

# Lee el archivo CSV e inserta en MongoDB
with open('data/jugadoras.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Transformar los campos de fecha y otros formatos si es necesario
        row['edad'] = int(row['edad'])  # Convertimos edad a entero
        row['equipo'] = {
            "nombre": row['equipo_nombre'],
            "pais": row['equipo_pais'],
            "start_year": int(row['start_year'])
        }
        row['condicion_fisica'] = {
            "peso": float(row['peso']),
            "altura": float(row['altura']),
            "enfermedades": row['enfermedades'].split(","),
            "categoria": row['categoria'],
            "grupo_sanguineo": row['grupo_sanguineo']
        }
        row['estadisticas'] = {
            "posesion_porcentaje": float(row['posesion_porcentaje']),
            "goles": int(row['goles']),
            "pases": int(row['pases'])
        }
        # Inserta el documento en la colección
        jugadoras.insert_one(row)

print("Inserción completada")
