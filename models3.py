class Producto:
    def __init__(self, id_producto, nombre, precio, categoria):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    def mostrar(self):
        print(self.id_producto, self.nombre, self.precio, self.categoria)
    def mostrar_compra(self):
        print(self.nombre, self.precio)


class Cliente:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
    def mostrar_cliente(self):
        print("Cliente:", self.nombre)
        print("Telefono:", self.telefono)
        print("Correo:", self.correo)


class Inventario:
    def __init__(self):
        self.productos = []
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        self.productos[0].mostrar()
        self.productos[1].mostrar()
        self.productos[2].mostrar()
        self.productos[3].mostrar()
        self.productos[4].mostrar()
        self.productos[5].mostrar()
        self.productos[6].mostrar()
        self.productos[7].mostrar()
        self.productos[8].mostrar()
        self.productos[9].mostrar()

    def agregar_a_compra(self, id_producto, compra):
        for producto in self.productos:
         if id_producto == producto.id_producto:
            compra.agregar_producto(producto)
            print("Producto agregado:", producto.nombre)
            break
        else:
         print("Producto no encontrado")
      
class Compra:
    def __init__(self, cliente):
        self.productos_compra = []
        self.cliente = cliente
    def agregar_producto(self, producto):
        self.productos_compra.append(producto)
    def mostrar_compra(self):
        print("Datos del cliente")
        self.cliente.mostrar_cliente()
        print("Productos comprados")

        if len(self.productos_compra) > 0:
            self.productos_compra[0].mostrar_compra()
        if len(self.productos_compra) > 1:
            self.productos_compra[1].mostrar_compra()
        if len(self.productos_compra) > 2:
            self.productos_compra[2].mostrar_compra()

    def calcular_total(self):
        total = 0
        if len(self.productos_compra) > 0:
            total = total + self.productos_compra[0].precio
        if len(self.productos_compra) > 1:
            total = total + self.productos_compra[1].precio
        if len(self.productos_compra) > 2:
            total = total + self.productos_compra[2].precio
        print("Total a pagar:", total)