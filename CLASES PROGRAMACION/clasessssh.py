class Persona():
    def __init__(self,nombre,correo):
        self.nombre=nombre
        self.correo=correo

    def registrar(self):
        Persona.lista.append(self)
        print(f"se ha registrado {self.nombre} ha sido registrada con el correo {self.correo}")
    def actualizar_datos(self,nombre,correo):
        self.nombre=nombre
        self.correo=correo
        print(f"los datos han sido actualizados") 

    @classmethod
    def Personas_registradas(cls):
        print("Personas registradas:")
        for p in cls.lista:
            print(f"--{Persona.nombre} -- {Persona.correo}")  