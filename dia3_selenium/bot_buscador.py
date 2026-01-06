from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By # <---- IMPORTANTE: Herramienta de Busqueda
from selenium.webdriver.common.keys import Keys # <---- IMPORTANTE: Para simular teclas (Enter)
from webdriver_manager.chrome import ChromeDriverManager
import time

print("--- 🕵️‍♂️ BOT INVESTIGADOR INICIADO ---")

# 1 . ABRIR CHROME
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

# 2 . ENCONTRAR LA BARRA DE BÚSQUEDA
# Le decimos: " Busca el elemento cuyo nombre sea 'q'"
# (Si fuera Facebook o Amazon, tendríamos que buscar el nombre que ellos usen)
print ("🔍 Buscando la barra de texto...")
barra_busqueda = driver.find_element(By.NAME, "q")

# 3 . INTERACTUAR
print ("⌨️ Escribiendo consulta...")
barra_busqueda.send_keys("Precio Bitcoin hoy") # Escribe esto
time.sleep(1) # Una pausa dramatica para que lo veas!! 

print ("🚀 Enviando búsqueda...")
barra_busqueda.send_keys(Keys.RETURN) # Presiona la tecla ENTER

# 4 . ADMIRAR EL RESULTADO

print("✅ Búsqueda finalizada. Te dejo 10 segundos para ver.")
time.sleep(10) # Te da tiempo de ver los precios antes de cerrar

driver.quit()

