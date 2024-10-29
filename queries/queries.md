// 1. Modificaciones

// Modificar nombre de la jugadora con dni 12345678A

db.jugadoras.updateOne(
  { dni: "12345678A" },
  { $set: { nombre: { $toUpper: "$nombre" } } }
);

// Modificar nombre de la jugadora con dni 87654321B
db.jugadoras.updateOne(
  { dni: "87654321B" },
  { $set: { nombre: { $toUpper: "$nombre" } } }
);


// 2. Consultas (Obteniendo el tiempo de ejecución)

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


// 3. Índices para Optimización

// Índice en el campo dni para acceso directo
db.jugadoras.createIndex({ dni: 1 });

// Índice en el campo equipo.nombre para búsquedas de equipos
db.jugadoras.createIndex({ "equipo.nombre": 1 });

// Índice en el campo equipo.pais para filtrado por país
db.jugadoras.createIndex({ "equipo.pais": 1 });

// Índice en el campo equipo.start_year para consultas por año de inicio
db.jugadoras.createIndex({ "equipo.start_year": 1 });