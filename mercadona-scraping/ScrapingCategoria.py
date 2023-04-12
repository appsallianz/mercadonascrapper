from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ScrapingSubCategoria import ScrapingSubCategoria

def ScrapingCategoria (driver, categoria_principal) :

    listaProductos = list()

    # Se hace click en la categoría principal
    categoria_principal.find_element(By.CSS_SELECTOR, 'span.category-menu__header').click()

    # Se obtiene el nombre de la categoría principal
    nombre_categoria_principal = categoria_principal.find_element(By.CSS_SELECTOR, 'span.category-menu__header')

    # Se obtienen las categorías secundarias
    categorias_secundarias = categoria_principal.find_elements(By.CSS_SELECTOR, 'li.subhead1-r.category-item')

    # Se procesa cada una de las categorías secundarias
    for categoria_secundaria in categorias_secundarias:

        # Se hace click en la siguiente categoría secundaria
        categoria_secundaria.find_element(By.CSS_SELECTOR, 'button.category-item__link').click()

        # Se espera a que se haya cargado el contenido
        productos_categoria_secundaria = WebDriverWait(driver, 100) \
            .until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.category-detail__content')))

        # Se procesan los productos de la categoría secundaria
        listaProductos.extend(ScrapingSubCategoria(nombre_categoria_principal.text, productos_categoria_secundaria))

    return listaProductos