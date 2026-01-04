# ---------------------------------
# APP: PSYCH-TRIAGE BOT V1.0
# AUTOR: Baltasar
# OBJETIVO: Determinar urgencia basado
# en INPUT de usuario
# ---------------------------------

print ("INITIATING SYSTEM...")
print ("--------------------------------")
print (" BIENVENIDO AL TRIAJE AUTOMATIZADO")
print ("---------------------------------")

# 1. INPUT DE DATOS (Recolección)
# .strip() quita espacios accidentales,
# .tittle() pone Mayúscula Inicial
nombre_paciente = input("Ingrese nombre del paciente").strip().title()

#TRUCO PRO: Input anidado con conversion
#Si el usuario pone letras aqui, el programa explotará
# (Lo arreglaremos en Semana 3)
edad = int(input(f"Ingrese edad de {nombre_paciente}: "))
nivel_ansiedad = int(input("Nivel de Ansiedad (1-10): "))
duerme_bien = input("¿Duerme bien? (si/no): ").lower().strip() #Convertimos a minuscula para comparar mas fácil

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
print ("\n" + "2") # Dos saltos de linea
print ("==================================")    
print (f"REPORT FOR: {nombre_paciente} (Edad: {edad})")
print ("===================================")
print (f"DIAGNÓSTICO : {diagnostico}")
print (f"PLAN ACCIÓN : {accion}")
print (f"==================================")
print ("SYSTEM SHUTDOWN.")
