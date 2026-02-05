class Perro():
    tipo= Perro
    def __init__(self,nombre, color):
        self.nombre=nombre
        self.color=color
    def sonido(self):
        return "Guau, Guau"

class Gato():
    tipo=Gato
    def __init__(self, nombre,color):
        self.nombre=nombre
        self.color=color
    def sonido(self):
        return "Miau, Miau"
class Canguro():
    tipo= Canguro
    def __init__(self,nombre,color):
        self.nombre=nombre
        self.color=color
    def sonido(self):
        return "Gruñido, Gruñido"

    class Veterinaria:
        def __init__(self,nombre, lista_mascotas):
            self.nombre=nombre
            self.lista_mascotas= lista_mascotas