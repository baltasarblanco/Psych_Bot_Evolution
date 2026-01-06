from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

print ("--- 🤖 INICIANDO EL BOT ---")

# 1. INSTALAR Y LANZAR EL NAVEGADOR
# Esto descarga el driver correcto para tu Chrome y abre la ventana
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 2. NAVEGAR A UNA WEB
print ("🌐 Yendo a Google...")
driver.get("https://www.google.com")

# 3. ESPERAR UN POCO
# (Para que veas que funciona antes de cerrarse)
time.sleep(5)

# 4. CERRAR!
print ("👋 Misión cumplida. Cerrando.")
driver.quit()