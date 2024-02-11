class Producto:
    def __init__(self, nombre, año, categoria):
        self.nombre = nombre
        self.año = año
        self.categoria = categoria
    
    def Display(self):
        print(f"Nombre: {self.nombre}\nAño: {self.año}\nCategoria: {self.categoria}\n")
    
class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            producto.Display()

    def filtrar_año(self, año):
        for producto in self.productos:
            if producto.año == año:
                producto.Display()

    def filtrar_categoria(self, categoria):
        for producto in self.productos:
            if producto.categoria == categoria:
                producto.Display()

def main():
    producto = Producto("Llanta", 2020, "Ruedas")
    producto1 = Producto("Filtro de aceite", 2019, "Motor")
    producto2 = Producto("Pastillas de freno", 2018, "Frenos")

    catalogo = Catalogo()
    catalogo.agregar_producto(producto)
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    print("Productos dentro del catalogo\n")
    catalogo.mostrar_productos()
    print("Filtros\n")
    print("Filtro por año 2020")
    catalogo.filtrar_año(2020)
    print("Filtro por categoria Motor")
    catalogo.filtrar_categoria("Motor")

if __name__ == "__main__":
    main()