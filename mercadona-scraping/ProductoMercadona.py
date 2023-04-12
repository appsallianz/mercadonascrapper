class ProductoMercadona(object):
    def __init__(self, categoria_principal, categoria_secundaria, subcategoria, descripcion, formato, tamanio, precio, moneda, unidad_venta):
        self.categoria_principal = categoria_principal
        self.categoria_secundaria = categoria_secundaria
        self.subcategoria = subcategoria
        self.descripcion = descripcion
        self.formato = formato
        self.tamanio = tamanio
        self.precio = precio
        self.moneda = moneda
        self.unidad_venta = unidad_venta

    def as_dict(self):
        return {'categoria_principal': self.categoria_principal,
                'categoria_secundaria': self.categoria_secundaria, 'subcategoria': self.subcategoria,
                'descripcion': self.descripcion, 'formato': self.formato,
                'tamanio': self.tamanio, 'precio': self.precio,
                'moneda': self.moneda, 'unidad_venta': self.unidad_venta}