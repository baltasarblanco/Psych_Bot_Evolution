import pandas as pd
import json
import matplotlib.pyplot as plt

print ("---🎨 INICIANDO MOTOR GRÁFICO (SIN PROTECCION) ---")

# PASO 1. CARGAR JSON
# Si el archivo no existe o esta roto, morirá aquí

print ("1. Buscando archivo 'pacientes_db.json'...")
with open ('pacientes_db.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
print (f"✅ Archivo encontrado. Pacientes: {len(data)}")

# PASO 2. CARGAR DATAFRAME
print ("2. Creando tabla maestra (DataFrame)...")
df = pd.DataFrame(data)
print ("✅ Tabla creada.")
print(df) # Imprimimos la tabla para verificar

# PASO 3. DIBUJAR
print ("3. Generando gráfico...")
plt.figure(figsize=(10,6))
barras = plt.bar(df["nombre"], df["ansiedad"], color='skyblue')

plt.title("Niveles de Ansiedad - Enero 2026", fontsize=16)
plt.xlabel("Pacientes", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.bar_label(barras, padding=3)

# PASO 4. GUARDAR
print ("4. Gurdando imagen...")
nombre_archivo = "reporte_visual_ansiedad.png"
plt.savefig(nombre_archivo)
print (f"\n🎉 ¡ÉXITO! Imagen guardada como: {nombre_archivo}")
