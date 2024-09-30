import requests
import json
import base64
import pandas as pd
from tqdm import tqdm
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def setup_firefox():
    options = Options()
    driver = webdriver.Firefox(options=options)
    print('driver conectado.')
    return driver

def extract_sku(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    sku = soup.find('span', class_='product-title_product-title__specification__UTjNc').text.strip().split(':')[-1].strip()
    return sku

def code_cookies(regionId):
    vtex_segment = {
        "campaigns": None, "channel": "1", "priceTables": None, "regionId": regionId, "utm_campaign": None,
        "utm_source": None, "utmi_campaign": None, "currencyCode": "COP", "currencySymbol": "$",
        "countryCode": "COL", "cultureInfo": "es-CO", "admin_cultureInfo": "es-CO", "channelPrivacy": "public"
    }
    cadena_json = json.dumps(vtex_segment, separators=(',', ':')).encode('utf-8')
    cadena_base64 = base64.b64encode(cadena_json).decode('utf-8')
    return cadena_base64

def extract_prices(url,regionId):
    sku = extract_sku(url)
    vtex_segment = code_cookies(regionId)
    url = "https://www.exito.com/api/product/getProductBySku"
    querystring = {"skuid":str(sku)}
    payload = ""
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://www.exito.com/huevo-rojo-a-x-30-insuperable-742696/p",
    "Connection": "keep-alive",
    "Cookie": f"checkout.vtex.com=__ofid=297ea3777be34d8ea4bb2fd73dd5fcd6; checkout.vtex.com=__ofid=297ea3777be34d8ea4bb2fd73dd5fcd6; CheckoutOrderFormOwnership=; _gcl_au=1.1.319435687.1723231502; _ga_W617R65N74=GS1.1.1726501139.19.1.1726502267.60.0.0; _ga=GA1.1.731529654.1723231502; _ga_S44GR46V45=GS1.1.1726501139.18.1.1726502290.37.0.0; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22qvamQVpmQk8pk7BHTsR6%22%7D; _clck=13400qt%7C2%7Cfp8%7C0%7C1682; _tt_enable_cookie=1; _ttp=ddgYMg63156BchtYDn0h6GerStG; _hjSessionUser_1473829=eyJpZCI6IjQ4ZWQxMzlkLWQyOWItNTE2ZS1iODI5LTg3MGZhMDIxYWFlZCIsImNyZWF0ZWQiOjE3MjMyMzE1MDUzNDQsImV4aXN0aW5nIjp0cnVlfQ==; _fbp=fb.1.1723231505471.95295616484517368; exTcIdE=%40%4022%40%4020sr2oAmSiWGXVyDF8d41g%7C1754767509779; VtexRCMacIdv7=20f22b1b-673a-4792-bfcc-4c49cc7e106d; vtex-search-anonymous=bfb5c8d6ce2a4c37b65b98d18d41004b; __gads=ID=f765979ac6db4d60:T=1723231552:RT=1726497978:S=ALNI_MZyFvtdHJruPY5JZAwiT96UKSY2BQ; __gpi=UID=00000ec197bec17a:T=1723231552:RT=1726497978:S=ALNI_MYQVonBO5rIKMX9K_LcNlJGB-4fjQ; __eoi=ID=80c3cb1484dd0bcc:T=1723231552:RT=1726497978:S=AA-Afja-zH6KHGfFXQOeyeIv7brQ; gbi_visitorId=clzn3li8500012a6cgscc1xrp; scarab.visitor=%2276548B39F2F49A1E%22; _hjSession_1473829=eyJpZCI6IjRlZWU1MDJiLThkNWUtNDUyOS04ZjgwLTRjZWRiOGQzYzIyNyIsImMiOjE3MjY0OTc5NzgzMDgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _clsk=1tgvfnc%7C1726502272108%7C7%7C0%7Cq.clarity.ms%2Fcollect; vtex_session=eyJhbGciOiJFUzI1NiIsImtpZCI6IjJDMTBDMTQzRTUyNjQzOENGMjExQ0M4OTM3QTZCN0E0RjY3NjM0M0IiLCJ0eXAiOiJqd3QifQ.eyJhY2NvdW50LmlkIjoiZjQ1MzFhM2ItNzc2ZS00MDdjLWIyMTMtNjhkNmRlOWU0MDVhIiwiaWQiOiJkMDA3MTFjNS0wYzg1LTQ3OTctOGFlNy1jYjUyNDU2OTk5ZDAiLCJ2ZXJzaW9uIjo3LCJzdWIiOiJzZXNzaW9uIiwiYWNjb3VudCI6InNlc3Npb24iLCJleHAiOjE3MjcxOTI2NDcsImlhdCI6MTcyNjUwMTQ0NywiaXNzIjoidG9rZW4tZW1pdHRlciIsImp0aSI6ImUwMjIzZDA2LWQ0NmMtNDhmMi05Mjc1LWQ1MzZjOGYxMjBiYiJ9.2FanAMXokyxNi7a5HvpPKwL7Y18PGigQEhWGfIzrTF5qK-ech89Tnh-8q778SagPZoCFh0GsFUdbdAkKjhpD3g; vtex_segment={vtex_segment}; VtexRCSessionIdv7=adb092de-69c2-45b3-8a89-5336d15a7c2d; gbi_sessionId=cm156bwbj00002a6dfmmj3bud",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=4",
    "TE": "trailers"
}
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data = json.loads(response.text)
    try:
        regular_price = data[0]['items'][0]['sellers'][0]['commertialOffer']['ListPrice']
    except:
        regular_price = 'No disponible'
    try:
        promotional_price = data[0]['items'][0]['sellers'][0]['commertialOffer']['Price']
    except:
        promotional_price = regular_price
    return promotional_price, regular_price

def run_extraction(city,excel_dir, output_dir, column_name):
    excel_filename = excel_dir  # Nombre del archivo Excel con las URLs
    df_urls = pd.read_excel(excel_filename)

    stores = {'Bogota': 'U1cjZXhpdG9jb2w7ZXhpdG9jb2wwOTM=', 'Pereira': 'U1cjZXhpdG9jb2w7ZXhpdG9jb2wwNjM='}

    data_list = []
    for url in tqdm(df_urls[column_name], desc="Procesando URLs"):
        try:
            promotional_price, regular_price = extract_prices(url, stores[city])
            data_list.append({
                'Url': url,
                'Precio Promocional': promotional_price,
                'Precio Regular': regular_price
            })
        except:
            data_list.append({
                'Url': url,
                'Precio Promocional': 'No disponible',
                'Precio Regular': 'No disponible'
            })

    data_df = pd.DataFrame(data_list)
    output_excel_filename = output_dir # Nombre del archivo Excel de salida
    data_df.to_excel(output_excel_filename, index=False)  # Guardar el DataFrame en el archivo Excel

    print(f'Datos guardados en {output_excel_filename}')


