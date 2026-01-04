# --------------------------------------------------
# APP: PSYCH-TRIAGE VOT V5.0 (DATA DRIVEN)
# CARACTERÍSTICA: ESTRUCTURA DE DATOS REAL (DICCIONARIOS)
# --------------------------------------------------

import datetime

# 1. BASE DE DATOS (Lista de diccionarios)
# Antes guardabamos textos, ahora guardaremos "Ficha de Objetos"

historial_clinico = []

print ("INITIATING SYSTEM v5.0 [DATA MODE]...")

while True:
    print ("\n" + "-"*40)
    nombre = input("Paciente (o 'Salir'): ").strip().title()

    if nombre == "Salir":
        break

    # LOGICA DE DIAGNOSTICO 
    edad = int(input(f"Edad de {nombre}: "))
    ansiedad = int(input("Ansiedad (1-10)"))
    duerme = input("¿Duerme bien? (si/no): ").lower().strip()

    diagnostico = "BAJO RIESGO"
    accion = "Control Anual"

    # Lógica de Condicional (Resumida para ahorrar espacio)

    if ansiedad >= 8:
        diagnostico = "ALTO RIESGO"
        accion = "Psiquiatría + Meditación"
    elif ansiedad >= 5:
        diagnostico = "RIESGO MODERADO"
        accion = "Terapia + Higiene de Sueño"
    
    if duerme == "no":
        accion += " + Melatonina"
    if edad < 18:
        accion += " + NOTIFICAR PADRES"

    # ---- AQUI OCURRE LA EVOLUCIÓN (DICCIONARIO) ----------
    # En lugar de texto plano, creamos una ESTRUCTURA

    paciente_nuevo = {
        "nombre": nombre,
        "edad": edad,
        "nivel_ansiedad": ansiedad,
        "diagnostico": diagnostico,
        "plan": accion,
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    # Guardamos el DICCIONARIO en la lista

    historial_clinico.append(paciente_nuevo)
    print(f"✅ Paciente {paciente_nuevo['nombre']} guardado como OBJETO.")

    # ----- PERSISTENCIA (GUARDAR EN TXT) --------
    # Convertimos el diccionario a texto solo para guardar en el archivo
    with open ("registro_v5.txt", "a", encoding="utf-8") as archivo:
        archivo.write(str(paciente_nuevo) + "\n")
    
    # REPORTE INTELIGENTE (Al salir)

print ("\n" + "="*40)
print (f"📊 REPORTE DE DATA SCIENCE ({len(historial_clinico)} Pacientes)")
print ("="*40)

    # Ahora podemos acceder a datos especificos

for p in historial_clinico:
        # Fijamos  como llamamos por CLAVE ["clave"]
        print (f"ID: {p['nombre']} | Edad: {p['edad']} | Dx: {p['diagnostico']}")


print ("="*40)
print ("SYSTEM OFF.")

