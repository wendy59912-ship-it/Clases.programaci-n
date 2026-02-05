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

class categoria
