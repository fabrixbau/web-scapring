from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os

def get_soup(url):
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(options=options)
    driver.get(url)
    sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()
    return soup

def get_amazon_object(soup):
    products = soup.find_all('div', {'class': 's-result-item'})
    if not products:
        print("No se encontraron productos con esa búsqueda.")
    else:
        for i, product in enumerate(products):
            try:
                name = product.find('span', {'class': 'a-size-base-plus a-color-base a-text-normal'}).text
                price = product.find('span', {'class': 'a-price-whole'}).text
                print(f'{i + 1}. {name}. Precio: {price}')
            except Exception as e:
                print(f"Error al extraer información: {e}")



def get_mercadolibre_object(soup):
    products = soup.find_all('li', {'class': 'ui-search-layout__item'})
    if not products:
        print("No se encontraron productos con esa búsqueda.")
    else:
        for i, product in enumerate(products):
            try:
                name = product.find('h2', {'class': 'ui-search-item__title'}).text
                price = product.find('span', {'class': 'andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript'}).text
                print(f'{i + 1}. {name}. Precio: {price}')
            except Exception as e:
                print(f"Error al extraer información: {e}")

def init():
    name = input("Ingrese el nombre del producto a buscar: ").replace(" ", "+")
    amazon_result_url = f'https://www.amazon.com.mx/s?k={name}&__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2J2IEFRHPQI5F&sprefix={name}%2Caps%2C207&ref=nb_sb_noss_1'
    mercadolibre_result_url = f'https://listado.mercadolibre.com.mx/{name}'
    amazon_soup = get_soup(amazon_result_url)
    mercadolibre_soup = get_soup(mercadolibre_result_url)
    get_amazon_object(amazon_soup)
    get_mercadolibre_object(mercadolibre_soup)

if __name__ == "__main__":
    # Ruta al controlador de Edge dentro de la carpeta 'driver'
    edge_driver_path = 'driver/msedgedriver.exe'
    
    # Establecer la ruta del controlador usando la variable de entorno PATH
    os.environ['PATH'] += ';' + edge_driver_path
    
    init()



