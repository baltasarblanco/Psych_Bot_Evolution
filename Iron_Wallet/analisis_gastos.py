cimport pandas as pd
import json

print ("---🕵️‍♂️ ANALISIS FINANCIERO IRON WALLET ----")

# PASO 1. CARGAR DATOS
# Carga el archivo 'gastos.json' usando json.load, igual que antes.
with open('gastos.json', 'r', encoding='utf-8') as f:
    datos_brutos = json.load(f) # ????

# PASO 2. CONVERTIR A TABLA (DataFrame)
# Convierte la lista de diccionarios en un DataFrame de Pandas
df = pd.DataFrame(datos_brutos) # ???? 

print("\n📊 TABLA DE GASTOS:")
print(df) # Muestra la tabla

# PASO 3. CÁLCUOS MATEMATICOS
# Sume toda la columna "monto"
total_gastado = df["monto"].sum() # ??? (Busca cómo sumar una columna en Pandas o usa .sum())

print(f"\n💸 TOTAL GASTADO: ${total_gastado}")

# PASO 4. EL GASTO MÁS CARO
# Encuentra el valor maximo 
gasto_maximo = df["monto"].max() # ???? (Usa .max())
print (f"💎 GASTO MAS CARO: ${gasto_maximo}")


# =====================================
# FASE 3 : VISUALIZACIÓN 
# =====================================

import matplotlib.pyplot as plt # (Asegurate de poner esto arriba o aqui)

print ("\n --- 🎨GENERANDO GRÁFICO ---")

# 1 . Agrupar DATOS (La Magia de Pandas)
# Esto dice: " Junta todo lo que tenga la misma categoría y SUMA sus motos"
datos_agrupados = df.groupby("categoria")["monto"].sum()

print("🍰 Datos para el gráfico")
print(datos_agrupados)

# 2 . CREAR EL GRAFICO TORTA
plt.figure(figsize =(7,7)) # TAMAÑO DEL CUADRADO

# plt.pie(numeros, etiquetas, formato porcentaje)
plt.pie(datos_agrupados, labels=datos_agrupados.index, autopct='%1.1f%%', colors=['gold', 'skyblue', 'lightgreen'])

plt.title("Distribución de Gastos - Iron Wallet")

# 3. GUARDAR
plt.savefig("mis_finanzas.png")
print ("\n📸 ¡FOTO TOMADA! Revisa 'mis_finanzas.png'")
