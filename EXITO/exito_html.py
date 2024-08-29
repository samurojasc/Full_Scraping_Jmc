from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json

firefox_options = Options()
firefox_options.add_argument('--headless')

driver = webdriver.Firefox(options=firefox_options)

# Abrir la página
driver.get('https://www.exito.com/arroz-diana-500-gr-479512/p')

# Esperar a que el script con JSON esté disponible
try:
    script = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//script[@type='application/ld+json']"))
    )
    json_script = script.get_attribute('innerHTML')
    print(json_script)  # Verificar el contenido del JSON
    product_data = json.loads(json_script)

    # Extraer precios del JSON
    offers = product_data.get('offers', {})
    if isinstance(offers, dict):
        low_price = offers.get('lowPrice', 'No disponible')
        high_price = offers.get('highPrice', 'No disponible')
        list_price = 'No disponible'
        if 'offers' in offers:
            for offer in offers['offers']:
                if 'listPrice' in offer:
                    list_price = offer['listPrice']
        print(f"Low Price: {low_price}")
        print(f"High Price: {high_price}")
        print(f"List Price: {list_price}")

finally:
    driver.quit()
