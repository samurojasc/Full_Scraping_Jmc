import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


# Configuración de Selenium para Firefox
def setup_firefox():
    options = Options()
    driver = webdriver.Firefox(options=options)
    return driver


# Función para procesar los enlaces
def process_links(links):
    driver = setup_firefox()

    for index, link in enumerate(links):
        print(f"Abriendo enlace {index + 1} de {len(links)}: {link}")
        driver.get(link)
        time.sleep(7)

    driver.quit()
    print("¡Todos los enlaces han sido procesados!")


# Leer enlaces del archivo Excel y procesarlos
df_urls = pd.read_excel('links2.xlsx')
links = df_urls['LINK'].tolist()

process_links(links)
