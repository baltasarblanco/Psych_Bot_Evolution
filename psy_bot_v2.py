# ---------------------------------
# APP: PSYCH-TRIAGE BOT V2.0
# AUTOR: Baltasar
# OBJETIVO: Determinar urgencia basado
# en INPUT de usuario
# ---------------------------------

print ("INITIATING SYSTEM v2.0...")

# 1. INPUT DE DATOS (Recolección)
# .strip() quita espacios accidentales,
# .tittle() pone Mayúscula Inicial

while True:
    # 1 pedimos la condición  de salida (KILLSWITH)
    # PEDIMOS EL NOMBRE PRIMERO.
    print ("\n" + "-"*30) #Linea Separadora ESTETICA
    nombre_paciente = input ("Ingrese nombre del paciente o escribe 'salir' para apagar): ").strip().title()

# SI EL USUARIO ESCRIBE SALIR MATAMOS EL BUCLE
    if nombre_paciente == "Salir":
        print ("SISTEMA APAGADO. GUARDANDO DATOS... BYE")
        break # <-- ESTO ROMPE EL BUCLE Y TERMINA EL PROGRAMA
# ---------------------------------------------------------
# AQUI PEGAS TU LOGICA VIEJA (CUIDADO CON LA SANGRIA/IDENTATION)
# Todo lo de abajo debe tener TAB (4 ESPACIOS) a la derecha.
# para estar dentro del "WHILE"
# ----------------------------------------------------------

#TRUCO PRO: Input anidado con conversion
#Si el usuario pone letras aqui, el programa explotará
# (Lo arreglaremos en Semana 3)
    edad = int(input(f"Ingrese edad de {nombre_paciente}: "))
    nivel_ansiedad = int(input("Nivel de Ansiedad (1-10): "))
    duerme_bien = input("¿Duerme bien? (si/no): ").lower().strip() #Convertimos a minuscula para comparar mas fácil
    input ("Presiona ENTER para continuar con el siguiente paciente...")

# 2. LÓGICA DE NEGOCIO (El cerebro)
# Aquí definimos la "Gravedad"
    diagnostico = ""
    accion = ""

# Condicionales (Lo veremos a fondo mañana, pero intúyelo hoy)
    if nivel_ansiedad >= 8:
        diagnostico = "ALTO RIESGO"
        accion = "Derivar a Psiquiatría Inmediata + Ansiolíticos SOS."
    elif nivel_ansiedad >= 5:
        diagnostico = "RIESGO MODERADO"
        accion = "Programar terapia semanal + Higiene de Sueño"
    else:
        diagnostico = "BAJO RIESGO"
        accion = "Check-up mensual"

# Logica booleana extra
    if duerme_bien == "no":
        accion = accion + " Evaluar Melatonina"

# Si tiene menos de 18
    if edad < 18:
        accion = accion + " + NOTIFICAR A PADRES"

# 3. RENDERIZADO (Output)
    print ("\n" * 2) # Dos saltos de linea
    print ("==================================")    
    print (f"REPORT FOR: {nombre_paciente} (Edad: {edad})")
    print ("===================================")
    print (f"DIAGNÓSTICO : {diagnostico}")
    print (f"PLAN ACCIÓN : {accion}")
    print (f"==================================")
    input ("Presiona ENTER para procesar siguiente paciente...")

print ("SYSTEM SHUTDOWN.")

