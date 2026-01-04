# ---- INTRODUCCIÓN A LOS DATOS  -----

# 1. CREACIÓN
# Un diccionario se define con llaves {}
paciente_demo = {
    "nombre": "Juan Perez",
    "edad": 30,
    "peso": 75.5,
    "fuma": False,
    "historial": ["Ansiedad", "Insomio"] #Una lista DENTRO de un diccionario!
}

print ("--- DATOS DEL PACIENTE ----")
# 2. Acceso por clave, no por número)
print (f"Nombre: {paciente_demo['nombre']}")
print (f"Diagnóstico Principal: {paciente_demo['historial'][0]}")

# 3. MODIFICACIÓN
# Juan cumplio años hoy
paciente_demo["edad"] = 31
print (f"Nueva edad: {paciente_demo['edad']}")

# 4. AGREGAR DATOS NUEVOS 
# Nos olvidamos de poner altura
paciente_demo["altura"] = 1.80
print (f"Altura agregada: {paciente_demo['altura']}")

# 5. BORRAR DATOS
# Dejó de fumar, borramos esa clave irrelevante (opcional)
del paciente_demo['fuma']

print ("-" * 20)
print ("FICHA TECNICA FINAL (JSON):")
print (paciente_demo)
