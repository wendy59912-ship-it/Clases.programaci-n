class producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def aplicar_descuento(self, porcentaje):
        self.precio *= (1 - porcentaje / 100)
        print (f"el nuevo precio es de {self.precio}")
    def actualizar_stock(self,cantidad):
        if (self.stock+cantidad)<0:
            print("no puedes tener stock negativo.")
        else:
            self.stock += cantidad
            print(f"la nueva cantidad de stock es de {self.stock}")

class categoria:
    def __init__(self, nombrecat):
        self.nombre_cat = nombrecat
        self.lista = []
    def agregar_producto(self, producto):
        self.productos.append(producto)
    def eliminar_producto(self, producto):
        self.productos.remove(producto)
    def mostrar_productos(self):
        for producto in self.productos:
            print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Stock: {producto.stock}")
