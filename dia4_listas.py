# INICIALIZAMOS LA BASE DE DATOS (Lista vacia)
# Es como ABRIR una caja vacia antes de empezar a trabajar
db_pacientes = []

print ("--- SISTEMA DE REGISTRO RÁPIDO ----")

while True:
    print ("-----------")
    # Pedimos dato
    nombre = input ("Ingresa nombre (o 'fin' para ver la lista): ").title()

    # Kill Swith
    if nombre == "Fin":
        break

    # 2 Guardado (Append)
    # .append () empuja el dato al final del tren
    db_pacientes.append(nombre)
    print (f"--> [OK] {nombre} guardado en memoria.")

# 3 REPORTE FINAL (Fuera del bucle)

print ("\n" + "="*30)
print ("RESUMEN DE LA SESIÓN")
print (f"Total Pacientes: {len(db_pacientes)}") #.len() cuenta la CANTIDAD.
print (f"Nombres: {db_pacientes}") # Imprime la lista cruda.
print ("="*30)
