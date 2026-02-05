class animales:
    def __init__(self, nombre, color, patas):
        self.nombre=nombre
        self.color=color
        self.patas=patas
    def sonido(self):
        return "sonido genérico"

class Conejo(animales):
    def __init__(self, nombre, color, patas):
        self.nombre=nombre
        self.color=color
        self.patas=patas
    def sonido(self):
        return "poing poing"
    def caract(self):
        return (f"Hola mi conejo se llama {self.nombre}, es de color {self.color} y tiene {self.patas} patas")
    