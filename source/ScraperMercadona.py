# Librerias
from selenium import webdriver
from selenium.webdriver.common.by import By
from ScraperAccionesIniciales import ScrapingInicio
from ScraperCategoria import ScrapingCategoria
from datetime import datetime
import pandas as pd

# Opciones de navegación
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver_path = 'chromedriver'
driver = webdriver.Chrome(driver_path, chrome_options=options)

# Obtenemos el user-agent
print("User-agent: " + driver.execute_script("return navigator.userAgent"))

# Inicializamos el navegador
driver.get('https://tienda.mercadona.es/categories/')

# Realizamos las acciones iniciales: aceptar cookies y codigo postal
ScrapingInicio(driver)

# Se obtiene el listado de categorías principales
categorias_principales = driver.find_elements(By.CSS_SELECTOR, 'li.category-menu__item')

# Listado de productos
listaProductosMercadona = list()

# Se procesa cada una de las categorías principales
for categoria_principal in categorias_principales:
    # Se procesan los productos de la categoría secundaria
    listaProductosMercadona.extend(ScrapingCategoria(driver, categoria_principal))

    # Se genera el DataFrame y se guarda cada vez que se procesa una categoría principal
    df = pd.DataFrame([x.as_dict() for x in listaProductosMercadona])
    df.to_csv('../dataset/productos_mercadona'+datetime.today().strftime('%Y-%m-%d')+ '.csv', index=False)

# Resumen
print("Productos obtenidos: ", len(listaProductosMercadona))
