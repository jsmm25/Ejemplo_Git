#ejemplo de estructura de datos
estudiantes = [
    {"nombre": "Angel", "calificaciones": {"Programacion": 90, "Interfacez": 85, "Estadistica": 88}},
    {"nombre": "Diego", "calificaciones": {"Programacion": 75, "Interfacez": 92, "Estadistica": 80}},
    {"nombre": "Jorge", "calificaciones": {"Programacion": 85, "Interfacez": 80, "Estadistica": 90}}
]

promedios = [
    {"nombre": estudiante["nombre"], 
     "promedio": sum(estudiante["calificaciones"].values()) / len(estudiante["calificaciones"])}
    for estudiante in estudiantes
]

for resultado in promedios:
    print(f"{resultado['nombre']} tiene un promedio de {resultado['promedio']:.2f}")
