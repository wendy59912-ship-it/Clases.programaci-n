class Biblioteca:
    def __init__(self, titulo, autor_o_editor, tipo_material, año_publicacion, ejemplares_disponibles):
        self.titulo = titulo
        self.autor_o_editor = autor_o_editor
        self.tipo_material = tipo_material
        self.año_publicacion = año_publicacion
        self.ejemplares_disponibles = ejemplares_disponibles
        self.estado_texto = "Disponible para prestamo" if ejemplares_disponibles > 0 else "No hay ejemplares disponibles"

    def limpiar_espacios(self):
        self.titulo = self.titulo.strip()
        self.autor_o_editor = self.autor_o_editor.strip()
        print("Espacios limpiados en el titulo y autor/editor del material " + self.titulo)

    def actualizar_estado(self):
        if self.ejemplares_disponibles > 0:
            self.estado_texto = "Disponible para prestamo"
        else:
            self.estado_texto = "No hay ejemplares disponibles"

    def mostrar_info(self):
        print("\nTitulo: " + self.titulo)
        print("Autor o Editor: " + self.autor_o_editor)
        print("Tipo de Material: " + self.tipo_material)
        print("Año de Publicacion: " + str(self.año_publicacion))
        print("Ejemplares Disponibles: " + str(self.ejemplares_disponibles))
        print("Estado: " + self.estado_texto + "\n")

class UsuarioBiblioteca:
    def __init__(self, nombre, edad, numero_socio, correo):
        self.nombre = nombre
        self.edad = edad
        self.numero_socio = numero_socio
        self.correo = correo
        self.materiales_prestados = []
        self.prestamos_texto = "No tiene materiales prestados"

    def prestar_material(self, material):
        if material.estado_texto == "Disponible para prestamo":
            self.materiales_prestados.append(material.titulo)
            material.ejemplares_disponibles = material.ejemplares_disponibles - 1
            material.actualizar_estado()
            self.actualizar_prestamos_texto()
            print("Material " + material.titulo + " prestado a " + self.nombre)
        else:
            print("No se puede prestar " + material.titulo + ", no hay ejemplares")

    def devolver_material(self, material):
        if material.titulo in self.materiales_prestados:
            self.materiales_prestados.remove(material.titulo)
            material.ejemplares_disponibles = material.ejemplares_disponibles + 1
            material.actualizar_estado()
            self.actualizar_prestamos_texto()
            print("Material " + material.titulo + " devuelto por " + self.nombre)
        else:
            print(self.nombre + " no tiene prestado el material " + material.titulo)

    def actualizar_prestamos_texto(self):
        if len(self.materiales_prestados) > 0:
            self.prestamos_texto = "Materiales prestados:"
        else:
            self.prestamos_texto = "No tiene materiales prestados"

    def mostrar_datos_usuario(self):
        print("\nNombre usuario: " + self.nombre)
        print("Edad: " + str(self.edad))
        print("Numero de socio: " + str(self.numero_socio))
        print("Correo: " + self.correo)
        print(self.prestamos_texto)
        if len(self.materiales_prestados) > 0:
            for material in self.materiales_prestados:
                print("- " + material)
        print("")