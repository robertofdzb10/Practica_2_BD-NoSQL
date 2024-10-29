import pandas as pd
import random
from datetime import datetime, timedelta

# Generar datos aleatorios para completar el CSV con 100 registros
data = []

nombres = ["Ana", "Laura", "Sofia", "Elena", "Lucía", "Maria", "Carmen", "Sara", "Raquel", "Patricia", "Julia", "Cristina", "Elisa", "Paula", "Natalia", "Blanca", "Adriana", "Verónica", "Isabel", "Marta"]
apellidos = ["González", "Martínez", "Jiménez", "Suárez", "Fernández", "Ruiz", "Díaz", "López", "García", "Moreno", "Navarro", "Serrano", "Gómez", "Sanz", "Cruz", "Moya", "Ramírez", "Vega", "Pérez", "Ortega"]
equipos = ["Manchester United", "Real Madrid", "Barcelona", "PSG", "Juventus", "Arsenal", "Olympique Lyon", "Real Sociedad", "Atlético Madrid", "Chelsea", "Valencia", "Sevilla", "AC Milan", "Inter de Milán", "Bayern Munich", "Liverpool", "Manchester City", "Tottenham", "Borussia Dortmund", "Leicester City"]
paises = ["UK", "España", "Francia", "Italia", "Alemania"]
lesiones = ["Lesión muscular", "Esguince de tobillo", "Contusión", "Fractura de nariz", "Contractura", "Tendinitis", "Desgarro muscular", "Lesión de hombro", "Rotura de ligamentos"]
categorias = ["A", "B", "C"]
grupos_sanguineos = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]

for i in range(100):
    dni = f"{random.randint(10000000, 99999999)}{random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    edad = random.randint(20, 30)
    ocupacion = random.choice(["Delantera", "Centrocampista", "Defensora", "Portera"])
    equipo_nombre = random.choice(equipos)
    equipo_pais = random.choice(paises)
    start_year = random.randint(2017, 2023)
    peso = round(random.uniform(55.0, 65.0), 1)
    altura = round(random.uniform(1.60, 1.80), 2)
    enfermedades = random.choice(["asma", "ninguna"])
    categoria = random.choice(categorias)
    grupo_sanguineo = random.choice(grupos_sanguineos)
    posesion_porcentaje = round(random.uniform(60.0, 75.0), 1)
    goles = random.randint(0, 20)
    pases = random.randint(100, 200)
    tipo_lesion = random.choice(lesiones)
    fecha_inicio = datetime.now() - timedelta(days=random.randint(30, 365))
    fecha_fin = fecha_inicio + timedelta(days=random.randint(5, 60))
    descripcion = f"{tipo_lesion.lower()} leve" if "leve" not in tipo_lesion.lower() else tipo_lesion.lower()
    retorno_estimado = random.choice(["Recovered", "Doubtful", "Recovering"])

    data.append([
        dni, nombre, apellido, edad, ocupacion, equipo_nombre, equipo_pais, start_year,
        peso, altura, enfermedades, categoria, grupo_sanguineo, posesion_porcentaje,
        goles, pases, tipo_lesion, fecha_inicio.date(), fecha_fin.date(), descripcion, retorno_estimado
    ])

# Crear DataFrame y exportarlo a CSV
df = pd.DataFrame(data, columns=[
    "dni", "nombre", "apellido", "edad", "ocupacion", "equipo_nombre", "equipo_pais", "start_year",
    "peso", "altura", "enfermedades", "categoria", "grupo_sanguineo", "posesion_porcentaje",
    "goles", "pases", "tipo_lesion", "fecha_inicio", "fecha_fin", "descripcion", "retorno_estimado"
])

# Guardar el archivo CSV
df.to_csv("data/jugadoras.csv", index=False, encoding="utf-8")

print("Archivo jugadoras.csv creado con éxito.")
