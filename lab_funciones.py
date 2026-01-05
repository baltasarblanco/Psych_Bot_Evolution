# ----- LABORATORIO DE FUNCIONES ------

# 1 . DEFINICIÓN DE HERRAMIENTA
# Esta función recibe un nivel de ansiedad y DEVUELVE un diagnóstico.

def calcular_diagnostico(nivel_ansiedad):
    if nivel_ansiedad >= 8:
        return "ALTO RIESGO"
    elif nivel_ansiedad >= 5: 
        return "RIESGO MODERADO"
    else:
        return "BAJO RIESGO"   

# 2 . Otra herramienta!
# Esta calcula el año de nacimiento aproximado
def calcular_nacimiento(edad_actual):
    anio_actual = 2026
    nacimiento = anio_actual - edad_actual
    return nacimiento

def verificar_melatonina(duerme_bien):
    if duerme_bien ==  "no":
        return True
    else:
        return False


# ----- ZONA DE PRUEBAS ( MAIN ) --------

print ("--- PROBANDO MIS HERRAMIENTAS ----")

# Usamos la primera función

paciente_1 = calcular_diagnostico(9)
print (f"Paciente con ansiedad 9: {paciente_1}")

paciente_2 = calcular_diagnostico(3)
print (f"Paciente con ansiedad 3: {paciente_2}")

#Usa mos la segunda función 

anio_baltasar = calcular_nacimiento(23)
print (f"Baltasar nacio aprox en: {anio_baltasar}")

# PODEMOS COMBINANRLAS! 
# Imagina hacer esto en una sola linea sin funciones.... seria un caos


print (f"Pedro (40 años) tiene dx: {calcular_diagnostico(6)} y nacio en {calcular_nacimiento(40)}")


# ZONA DE PRUEBAS -----

print ("-" * 20)
resultado_test = verificar_melatonina("no")
print (f"¿Si dice 'no', necesita melatonina?: {resultado_test}")

# DEBERIA DECIR TRUE!!! 