import json

# 1 . TUS DATOS EN RAM ( Lista de diccionarios )
# Imagina que esto es lo que recolectó tu bot hoy
pacientes_hoy = [
    {"nombre": "Baltasar", "edad": 23, "riesgo": "Alto"},
    {"nombre": "Pedro", "edad": 45, "riesgo": "Bajo"},
    {"nombre": "Ana", "edad": 12, "riesgo": "Medio"}
]

print ("---- GUARDANDO DATOS EN FORMATO JSON ----")

# 2 . GUARDAR (Dump)
# "w" = Write (Sobreescribir)

with open ("base_de_datos.json", "w", encoding ="utf-8") as archivo:
    # json_dump (DATOS, ARCHIVO, indent=4)
    # indent=4 es para que sea bonito y ORDENADO
    json.dump(pacientes_hoy, archivo, indent=4)

print ("✅ Datos exportados a 'base_de_datos.json'.")