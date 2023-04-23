from Producto import ProductoMercadona
from selenium.webdriver.common.by import By
from datetime import datetime

def ScrapingSubCategoria (nombre_categoria_principal, elemento) :

    listaProductos = list()

    # Se obtiene el nombre de la categoria secundaria
    nombre_categoria_secundaria = elemento.find_element(By.CSS_SELECTOR, 'h1.category-detail__title.title1-b')

    # Se obtienen las subcategorias de la categoría secundaria
    if not elemento.find_elements(By.CSS_SELECTOR, 'div.category-section'):
        subcategorias = elemento.find_elements(By.CSS_SELECTOR, 'section.section')
    else:
        subcategorias = elemento.find_elements(By.CSS_SELECTOR, 'div.category-section')

    # Se procesa cada subcategoria
    for subcategoria in subcategorias:

        # Se obtiene el nombre de la subcategoria.
        if subcategoria.find_elements(By.CSS_SELECTOR, 'h2.section__header.headline1-b'):
            nombre_subcategoria = subcategoria.find_element(By.CSS_SELECTOR,
                                                            'h2.section__header.headline1-b')
        else:
            # La sección de Pescados tiene el nombre de las subcategorias de forma distinta
            nombre_subcategoria = subcategoria.find_element(By.CSS_SELECTOR, 'h3.category-section__name.title1-b')

        # Se obtienen los productos de la subcategoría
        productos = subcategoria.find_elements(By.CSS_SELECTOR,'div.product-cell')

        # Se procesa cada producto
        for producto in productos:

            # Se obtienen los elementos del producto
            descripcion = producto.find_element(By.CSS_SELECTOR,'h4.subhead1-r.product-cell__description-name')
            formato_tamanio = producto.find_elements(By.CSS_SELECTOR, 'span.footnote1-r')
            if len(formato_tamanio) == 2:
                tamanio = formato_tamanio[1]
            else:
                tamanio = None
            formato = formato_tamanio[0]
            precio = producto.find_element(By.CSS_SELECTOR, 'p.product-price__unit-price.subhead1-b')
            unidad_venta = producto.find_element(By.CSS_SELECTOR, 'p.product-price__extra-price.subhead1-r')

            # Se inserta el producto en la lista de productos
            listaProductos.append(
                ProductoMercadona(nombre_categoria_principal, nombre_categoria_secundaria.text, nombre_subcategoria.text, descripcion.text, formato.text,
                                  " " if tamanio == None else tamanio.text, precio.text.split()[0],
                                  precio.text.split()[1], unidad_venta.text, datetime.today().strftime('%Y-%m-%d')))

    return listaProductos