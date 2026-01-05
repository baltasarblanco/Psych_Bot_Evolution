
# Vamos a necesitar 4 cosas:
# 1 . Memoria (RAM): Necesitamos una lista [] para ir guardando los gastos mientras el programa corre
# 2. Bucle (MOTOR): Un while True que no pare de pedirte gastos hasta que digas "basta"
# 3. Estructura: Cada gesto será un Diccionario {} ( porque tiene concepto, monto y categoria).
# 4. Disco Duro: Al final de cada vuelta, guardamos todo en gastos.json 


import json
print ("----💰 IRON WALLET: GESTOR DE GASTOS ---")

# PASO 1. CARGAR LA MEMORIA
# Intentamos leer el archivo. Si no existe, empezamos con la lista vacia.
try:
    with open('gastos.json', 'r', encoding='utf-8') as f:
        mis_gastos = json.load(f)
    print (f"✅ Se cargaron {len(mis_gastos)} gastos anteriores.")
except:
    print ("🆕 Iniciando billetera nueva.")
    mis_gastos = [] # <---- Si falla GENERAMOS UNA NUEVA

# PASO 2. EL BUCLE INFNITO

while True:
    print ("\n" + "="*20)

    # A. PEDIR DATOS AL USUARIO
    print ("Escribe el gasto (o 'salir' para terminar):")
    concepto = input("Concepto: ") ## ?? (Usar input)

    # B. CONDICIÓN DE SALIDA
    if concepto == "salir":
        print ("👋 Guardando y saliendo...")
        break

    # PEDIMOS EL RESTO DE DATOS
    # ¡OJO! El monto debe ser un número (int o float)
    monto = float(input("Monto ($): "))
    categoria = input("Categoria (Comida/Uber/etc): ")

    # C. CREAR EL DICCIONARIO (El paquete de DATOS)
    # Tienes que guardar las 3 variables de arriba aquí dentro
    nuevo_gasto = {
        "concepto": concepto,
        "monto": monto,
        "categoria": categoria
    }

    # D. GUARDAR EN LA LISTA (RAM)
    mis_gastos.append(nuevo_gasto) # ??? Agregar al diccionario la lista de 'mis_gastos')

    # E. GUARDAR EN EL ARCHIVO (DISCO DURO)
    # Esto asegura que si se corta la luz, no pierdes nada.
    with open('gastos.json', 'w', encoding='utf-8') as f:
        json.dump(mis_gastos, f, indent=4) # ??? Usa json.dump para guardar la lista en 'f')
    
    print ("✅ Gasto guardado correctamente")

