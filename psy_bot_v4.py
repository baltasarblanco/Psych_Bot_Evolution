import datetime # <---- AGREGA ESTO EN LA LINEA 1

# ---------------------------------- 
# APP: PSYCH-TRIAGE BOT V3.0 (FINAL)
# CARACTERÍSTICA: MEMORIA PERSISTENTE
# ----------------------------------

# 1 MEMORIA (RAM)
# Iniciamos la lista vacía antes de arrancar la máquina.
historial_clinico = []

print ("INITIATING SYSTEM v3.0 [RECORDING ON]...")

while True:
    # --- INPUT DE CONTROL ---
    print("\n" + "-"*40)
    nombre_paciente = input ("Paciente (o 'Salir'): ").strip().title()

    # KILL SWITCH (SALIDA)
    if nombre_paciente == "Salir":
        print ("CERRANDO SISTEMA...")
        break

# ----- LOGICA DE DIAGNOSTICO (Tu motor V2) ----

    edad = int(input(f"Edad de {nombre_paciente}: "))
    nivel_ansiedad = int(input("Ansiedad (1-10): "))
    duerme_bien = input("¿Duerme bien? (si/no): ").lower().strip()

    diagnostico = ""
    accion = ""

# CÁLCULOS

    if nivel_ansiedad >= 8:
        diagnostico = "ALTO RIESGO"
        accion = "Derivar a Psiquiatría + Meditación"
    elif nivel_ansiedad >=5:
        diagnostico = "RIESGO MODERADO"
        accion = "Terapia + Higiene Sueño"
    else:
        diagnostico = "BAJO RIESGO"
        accion = "Control anual"
    if duerme_bien == "no":
        accion += " + Melatonina"
    if edad < 18:
        accion += " + NOTIFICAR PADRES"

# --- AQUI OCURRE LA MAGIA (GUARADADO) -----
# Creamos una "Ficha" de texto con el resumen
    ficha_tecnica = f"[PACIENTE: {nombre_paciente}] -> {diagnostico} ({accion})"

# La metemos en el tren (Lista)
    historial_clinico.append(ficha_tecnica)
    print (f"✅ {nombre_paciente} archivado en RAM.")

# NUEVA FUNCIÓN: GUARDADO EN DISCO DUR (.txt)

# 1. Obtenemos la fecha y la hora actual
    hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 2. Abrimos el archivo en modo "a" (Append/Agregar)
#encoding='utf-8' es vital para que las tildes (á, ñ) se guarden bien
    with open("registro_pacientes.txt", "a", encoding="utf-8") as archivo:
        # Escribimos: HORA | FICHA | Salto de linea (\n)
        archivo.write (f"{hora_actual} | {ficha_tecnica}\n")
    print ("💾 Datos guardados en 'registro_pacientes.txt' exitosamente.")



# REPORTE INMEDIATO (opcional, para ver qué pasa)
    print (f"Dianostico actual: {diagnostico}")

# ---- ESTO PASA CUANDO ROMPES EL BUCLE (OUTSIDE) ---
print ("\n" + "="*40)
print ("📑 REPORTE FINAL DEL DÍA")
print (f"Total Pacientes Atendidos: {len(historial_clinico)}")
print ("="*40)

# Bucle For: Imprimimos paciente por paciente (Elegancia pura)

for ficha in historial_clinico:
    print (ficha)

print ("="*40)
print ("SYSTEM OFF.")
