import pandas as pd
import json

print ("\n--- 🕵️‍♂️ INICIANDO ANÁLISIS DE DATOS --- ")

# 1. CARGA DE DATOS

try:
    with open('pacientes_db.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print (f"✅ Se cargaron {len(data)} pacientes desde el JSON.")
except FileNotFoundError:
    print("❌ ERROR: No encuentro el archivo 'pacientes_db.json'")
    exit()


# 2 . CREACIÓN DEL DATAFRAME (la tabla magica)

df = pd.DataFrame(data)

# 3. MOSTRAR LA TABLA CRUDA 

print("\n--- 📊 TABLA COMPLETA ---")
print(df.to_string()) #to_string() obliga a mostrar todo

# ========================================
# 🧠 AQUI EMPIEZA LA CIENCIA DE DATOS REAL
# ========================================

# 4 . Ordenar datos
# Vamos a ordenar por niveles de ansiedad ( de mayor a menor )
print ("\n\n--- ⚠️ PACIENTES ORDENADOS POR RIESGO (Mayor a Menor) ---")
df_ordenado = df.sort_values(by="ansiedad", ascending=False)
print (df_ordenado.to_string())

# 5 . FILTRAR DATOS (Queries)
# "Múestrame solo los que no duermen bien"
print ("\n\n--- 🌙 PACIENTES CON INSOMIO (Duermen: no) ---")
insomio = df[df["plan"].str.contains("Melatonina")] # Esto es Sintaxis pura de Pandas
print (insomio.to_string())

# 6 . ESTADÍSTICAS AUTOMÁTICAS
print ("\n\n--- 📈 ESTADÍSTICAS RÁPIDAS ---")
promedio_edad = df["edad"].mean()
promedio_ansiedad = df["ansiedad"].mean()

print (f"Edad promedio: {promedio_edad:.1f} años")
print (f"Ansiedad promedio del grpo: {promedio_ansiedad:.1f} / 10")
