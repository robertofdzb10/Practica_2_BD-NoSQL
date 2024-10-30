// 1. Insercción manual de una jugadora

// Sentencia de inserción
db.jugadoras.insertOne({
  "_id": "1",
  "dni": "12345678A",
  "nombre": "Ana",
  "apellido": "González",
  "edad": 24,
  "ocupacion": "Delantera",
  "equipo": {
    "nombre": "Manchester United",
    "pais": "UK",
    "start_year": 2022
  },
  "condicion_fisica": {
    "peso": 60.5,
    "altura": 1.68,
    "enfermedades": ["asma"],
    "categoria": "A",
    "grupo_sanguineo": "O+"
  },
  "estadisticas": {
    "posesion_porcentaje": 65.3,
    "goles": 15,
    "pases": 120
  },
  "lesiones": [
    {
      "tipo_lesion": "Lesión muscular",
      "fecha_inicio": ISODate("2024-08-18"),
      "fecha_fin": ISODate("2024-09-18"),
      "descripcion": "Lesión en el muslo",
      "retorno_estimado": "Doubtful"
    }
  ]
})

// Comprobación de inserción
db.jugadoras.find({ 
  dni: "12345678A"
}).pretty()


// 2. Modificaciones

// Modificar nombre de la jugadora con dni 12345678A
db.jugadoras.updateOne(
  { dni: "12345678A" },
  [
    { $set: { nombre: { $toUpper: "$nombre" } } }
  ]
);

// Comprobación de modificación
db.jugadoras.find({
  dni: "12345678A"
}).pretty()

// Modificar nombre de la jugadora con dni 33587252K
db.jugadoras.updateOne(
  { dni: "33587252K" },
  [
    { $set: { nombre: { $toUpper: "$nombre" } } }
  ]
);

// Comprobación de modificación
db.jugadoras.find({
  dni: "33587252K"
}).pretty()

// 3. Consultas (Obteniendo el tiempo de ejecución)

// Consulta por una jugadora específica
db.jugadoras.find({
  dni: "12345678A",
  "equipo.start_year": { $gt: 2020 }
})

db.jugadoras.find({
  dni: "12345678A",
  "equipo.start_year": { $gt: 2020 }
}).explain("executionStats")

// Filtrar por Equipos que Empiecen con "Manchester…"
db.jugadoras.find({
  "equipo.nombre": { $regex: /^Manchester/, $options: "i" }
})

db.jugadoras.find({
  "equipo.nombre": { $regex: /^Manchester/, $options: "i" }
}).explain("executionStats")

// Consulta por un País Específico
db.jugadoras.find({
  "equipo.pais": "España"
})

db.jugadoras.find({
  "equipo.pais": "España"
}).explain("executionStats")


// 4. Índices para Optimización

// Índice en el campo dni para acceso directo
db.jugadoras.createIndex({ dni: 1 });

// Índice en el campo equipo.nombre para búsquedas de equipos
db.jugadoras.createIndex({ "equipo.nombre": 1 });

// Índice en el campo equipo.pais para filtrado por país
db.jugadoras.createIndex({ "equipo.pais": 1 });

// Índice en el campo equipo.start_year para consultas por año de inicio
db.jugadoras.createIndex({ "equipo.start_year": 1 });