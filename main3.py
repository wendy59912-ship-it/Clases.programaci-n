from models3 import *

print("Sistema de cafeteria")

nombre = input("Ingrese su nombre: ")
telefono = input("Ingrese su telefono: ")
correo = input("Ingrese su correo: ")

cliente = Cliente(nombre, telefono, correo)

inventario = Inventario()

p1 = Producto(1,"Cafe Americano",35,"Cafe")
p2 = Producto(2,"Cafe Latte",45,"Cafe")
p3 = Producto(3,"Capuchino",50,"Cafe")
p4 = Producto(4,"Chocolate Caliente",40,"Bebidas")
p5 = Producto(5,"Te Verde",30,"Bebidas")
p6 = Producto(6,"Pan Dulce",25,"Panaderia")
p7 = Producto(7,"Croissant",38,"Panaderia")
p8 = Producto(8,"Sandwich",60,"Comida")
p9 = Producto(9,"Pastel de Chocolate",55,"Postres")
p10 = Producto(10,"Galletas",20,"Postres")

inventario.agregar_producto(p1)
inventario.agregar_producto(p2)
inventario.agregar_producto(p3)
inventario.agregar_producto(p4)
inventario.agregar_producto(p5)
inventario.agregar_producto(p6)
inventario.agregar_producto(p7)
inventario.agregar_producto(p8)
inventario.agregar_producto(p9)
inventario.agregar_producto(p10)

print("Productos disponibles")
inventario.mostrar_productos()
compra = Compra(cliente)

id1 = int(input("Ingrese el primer producto que desea comprar: "))
inventario.agregar_a_compra(id1, compra)
id2 = int(input("Ingrese otro producto que desea comprar: "))
inventario.agregar_a_compra(id2, compra)
id3 = int(input("Ingrese otro producto que desea comprar: "))
inventario.agregar_a_compra(id3, compra)

print("Resumen de la compra")
compra.mostrar_compra()
compra.calcular_total()
print("Gracias por su compra")