import time
import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver import DesiredCapabilities

def run_extraction_zapatoca(df,column_name):

    firefox_options = Options()
    firefox_options.add_argument('--headless')
    capabilities = DesiredCapabilities.FIREFOX.copy()
    capabilities['marionette'] = True
    driver = webdriver.Firefox(options=firefox_options)

    columna_links = df[column_name]

    links = columna_links.tolist()

    products = []
    for link in links:
        driver.get(link)

        try:
            product_name = driver.find_element(By.TAG_NAME, 'h1').text
        except:
            product_name = 'No Name'

        try:
            suggested_price = driver.find_element(By.CSS_SELECTOR, '.suggested_price').text.strip()
        except:
            suggested_price = 'No disponible'

        try:
            list_price = driver.find_element(By.ID, 'itempropprice').text.strip()
        except:
            list_price = suggested_price  # Usa el precio sugerido si no hay precio de lista

        if not suggested_price:
            suggested_price = list_price
        products.append({
            'name': product_name,
            'link': link,
            'precio regular': suggested_price,
            'precio promocional': list_price,
        })

    driver.quit()

    df = pd.DataFrame(products)

    return df