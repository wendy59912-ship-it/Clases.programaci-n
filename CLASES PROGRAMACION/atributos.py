class Nombre:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera  

    def __str__(self):
        return f"Nombre: {self.nombre},{self.edad},{self.carrera}"
    def __repr__(self):
        return f"Nombre(nombre:{self.nombre}, edad:{self.edad}, carrera:{self.carrera})"

    def __add__(self, otra):
         return f"{self.nombre} y {otra.nombre}se aman"
    
    def null(self, otra):
        return f"{self.edad * otra.edad}"

    def __eq__(self, otra):
        return self.carrera == otra.carrera

