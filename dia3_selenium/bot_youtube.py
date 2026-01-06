from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

print ("--- 🎵 DJ DE PYTHON EN LA CASA ---")

# 1. PREPARAR EL EQUIPO
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# 2 . ENTRAR AL CLUB ( YOUTUBE )
print ("🌐 Entrando a YouTube...")
driver.get("https://www.youtube.com")
time.sleep(3) #     Esperamos a que cargue la portada

try:
    print ("Buscando la barra de mezclas...")
    barra = driver.find_element(By.NAME, "search_query") # <------ 3. ENCONTRAR LA BARRA DE BUSQUEDA, EN YOUTUBE ES 'search_query'

    # 4  . ELEGIR LA CANCIÓN (CAMBIA ESTO POR TU TEMA FAVORITO!!! )

    cancion = "Baltasar Blanco - Lugares"
    print(f"💿 Poniendo el disco: {cancion}")

    # Combo breaker: Escribir + Enter
    barra.send_keys(cancion + Keys.RETURN)

    # Esperamos a que carguen los resultados
    print ("⏳ Buscando resultados...")
    time.sleep(3)

    # 5. DARLE PLAY AL PRIMER VIDEO
    # ESTO ES UN TRUCO: Buscamos el elemento con ID 'video-title'
    # Como hay muchos, 'find_element' (en singular) siempre agarra el primero que ve.
    print ("▶️ Dándole PLAY al primer video...")
    video = driver.find_element(By.ID, "video-title")
    video.click()  

    print ("✅ ¡A DISFRUTAR! Dejo el navegador abierto por 30 segundos...")
    time.sleep(30) # Tiempo para escuchar un poco

except Exception as e:
    print (f"❌ LA FIESTA SE ROMPÍO: {e}")


# 6 . CERRAR

print ("👋 Cerrando el club.")
driver.quit()
