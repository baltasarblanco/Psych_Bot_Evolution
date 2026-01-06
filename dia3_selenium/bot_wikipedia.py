from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

print ("---📚 BOT WIKIPEDIA: MODO LECTOR ----")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://es.wikipedia.org")
time.sleep(2)

try:
    #  1 . buscar
    print ("🔍 Buscando barra...")
    barra = driver.find_element(By.NAME, "search")

    print ("🚀 Buscando 'Python'...")
    # Usamos el truco del COMBO BREAKER que ya dominas
    barra.send_keys("Lenguaje de Programación Python" + Keys.RETURN)

    # 2 . ESPERAR A QUE CARGUE LA NUEVA PAGINA
    # IMPORTANTE: SINO ESPERAS INTETARA LEER LA PAGINA VIEJA
    time.sleep(3)

    # 3. ROBAMOS DATOS ( SCRAPING )
    print("\n--- 📝 DATOS EXTRAÍDOS ---")

    # Buscamos el Título Principal (h1)
    titulo = driver.find_element(By.TAG_NAME, "h1").text
    print (f"📖 TÍTULO: {titulo}")

    # Buscamos el párrafo de definición
    # El ID 'mw-content-text' contiene el cuerpo del articulo en WIkipedia)
    contenido = driver.find_element(By.ID, "mw-content-text").text

    # Solo mostramos los 200 caracteres para no llenar la pantalla
    print (f"📜 RESUMEN: {contenido[:200]}...")
    
    print("📸 Sonríe... Tomando foto de evidencia.")
    driver.save_screenshot("evidencia_wikipedia.png") # ESTA ES LA MAGIA <-----


    print ("------------------------------")
    print ("✅ Lectura Exitosa! Cerrando en 5s...")
    time.sleep(5)

except Exception as e:
    print (f"❌ ERROR: {e}")

driver.quit()

