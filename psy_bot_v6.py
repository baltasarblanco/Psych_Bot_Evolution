# --------------------------------------------------------------
# APP. PSYTH-TRIAGE BOT V6.0 (FINAL BOSS)
# CARACTERÍSTICA: BASE DE DATOS JSON (CARGA Y GUARDA)
# --------------------------------------------------------------

import json
import datetime
import os # Para verificar si existe el archivo

ARCHIVO_DB = "pacientes_db.json"
historial_clinico = []

# ----- 1. FASE DE CARGA (RECUPERANDO MEMORIA) ------

print ("INITIATING SYSTEM v6.0...")

if os.path.exists(ARCHIVO_DB):
    # Si el archivo existe, lo leemos
    with open(ARCHIVO_DB, "r", encoding= "utf-8") as f:
        historial_clinico = json.load(f)
    print (f"✅ BASE DE DATOS CARGADA: {len(historial_clinico)} pacientes recuperados.")

else:
    # Si no existe, empezamos de cero
    print ("⚠️ No se encontró base de datos. Iniciando sistema limpio.")
    historial_clinico = []

# ---- 2. BUCLE PRINCIPAL ------+

while True:
    print ("\n" + "-"*40)
    nombre = input("Paciente (o 'Salir'): ").strip().title()

    if nombre == 'Salir':
        break

    # --- LÓGICA DE SIEMPRE ---
    try:
        edad = int(input(f"Edad de {nombre}: "))
        ansiedad = int(input(f"Ansiedad (1-10): "))
    except ValueError:
        print ("❌ Error: Porfavor ingrese NÚMEROS en edad y ansiedad.")
        continue # Vuelve al INICIO DEL BUCLE

    duerme = input("¿Duerme bien? (si/no): ").lower().strip()

    diagnostico = "BAJO RIESGO"
    accion = "Control Anual"

    if ansiedad >= 8:
        diagnostico = "ALTO RIESGO"
        accion = "Psiquiatría + Meditación"
    elif ansiedad >= 5:
        diagnostico = "RIESGO MODERADO"
        accion = "Terapia + Higiene Sueño"
    
    if duerme == "no":
        accion += " + Melatonina"
    if edad < 18:
        accion += " + NOTIFICAR PADRES"

    # --- CREAR OBJETO ---
    
    paciente_nuevo = {
        "nombre": nombre,
        "edad": edad,
        "ansiedad": ansiedad,
        "diagnostico": diagnostico,
        "plan": accion,
        "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    historial_clinico.append(paciente_nuevo)
    print (f"✅ {nombre} agregado temporalmente")

    # --- 3. GUARDADO AUTOMÁTICO (AUTO-SAVE) ---
    # Guardamos cada vez que agregemos uno, para no perder nada si se corta la luz.

    with open(ARCHIVO_DB, "w", encoding="utf-8") as f:
        json.dump(historial_clinico, f, indent=4)
    print ("💾 Base de datos actualizada (JSON).")

# --- REPORTE FINAL ---

print ("\n" + "="*40)
print (f"📊 ESTADO FINAL DE LA BASE DE DATOS ({len(historial_clinico)} Registros)")
for p in historial_clinico:
    print (f"- {p['nombre']} ({p['edad']} años): {p['diagnostico']}")

print ("="*40)
print ("SYSTEM OFF.")

