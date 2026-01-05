# -----------------------------------
# App: PSYCH-TRIAGE BOT V7.0 (FINAL ARCHITECTURE)
# CARACTERISTICAS: Código Modular (FUCIONES)
# -----------------------------------

import json
import datetime
import os

ARCHIVO_DB = "pacientes_db.json"

# ======================================
# 🛠️ ZONA DE HERRAMIENTAS (FUNCIONES)
# ======================================

def cargar_base_datos():
    """ Busca el archivo JSON y carga los pacientes. Si no existe, devuelve la lista vacia."""
    if os.path.exists(ARCHIVO_DB):
        with open(ARCHIVO_DB, "r", encoding="utf-8") as f:
            return json.load(f)
    return [] # Si no existe, devolvemos la lista vacía

def guardar_base_datos(lista_pacientes):
    """"Recibe la lista completa y la guarda en el disco."""
    with open(ARCHIVO_DB, "w", encoding="utf-8") as f:
            json.dump(lista_pacientes, f, indent=4)
    print ("💾 (Auto-Save) Datos guardados correctamente.")

def calcular_diagnostico(ansiedad):
    """"Motor de decisión clínica."""
    if ansiedad >= 8:
        return "ALTO RIESGO", "Psiquiatría + Meditación"
    elif ansiedad >= 5:
        return "RIESGO MODERADO", "Terapia + Higiene Sueño"
    else:
        return "BAJO RIESGOS", "Control anual"

# ===========================================================
# 🚀 ZONA DE EJECUCIÓN (MAIN LOOP)
# ============================================================

print ("INITIATING SYSTEM v7.0 [MODULAR ARCHITECTURE]...")

# 1. Usamos nuestra herramienta de carga
historial_clinico = cargar_base_datos()
print (f"✅ Sistema listo. {len(historial_clinico)} pacientes en memoria.")

while True:
    print ("\n" + "-"*40)
    nombre = input("Paciente (o 'Salir'): ").strip().title()

    if nombre == "Salir":
        break
    
    try:
        edad = int(input(f"Edad de {nombre}: "))
        ansiedad = int(input(f"Ansiedad (1-10): "))
    except ValueError:
        print("❌ Error: Ingrese solo números")
        continue

    duerme = input("¿Duerme bien? (si/no): ").lower().strip()

# ---- AQUI USAMOS LA MAGIA DE LAS FUNCIONES ------
# EN UNA SOLA LISTA OBTENEMOS EL DIAGNOSTICO Y EL PLAN
    diagnostico, plan_base = calcular_diagnostico(ansiedad)

# Lógica extra ( pequeños ajustes )
    if duerme == "no":
        plan_base += " + Melatonina"
    if edad < 18:
        plan_base += " + NOTIFICAR PADRES"

# Creamos el paciente
    paciente_nuevo = {
        "nombre": nombre,
        "edad": edad,
        "ansiedad": ansiedad,
        "diagnostico": diagnostico,
        "plan": plan_base,
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    historial_clinico.append(paciente_nuevo)
    print (f"✅ Paciente {nombre} procesado con éxito.")

    # 2 . Usamos nuestra herramienta de guardado

    guardar_base_datos(historial_clinico)

# ---- CIERRE -----
print ("\n" + "="*40)
print (f"📊 REPORTE FINAL: ({len(historial_clinico)} Pacientes.)")
for p in historial_clinico:
    print (f"- {p['nombre']} | {p['diagnostico']}")
print ("="*40)

