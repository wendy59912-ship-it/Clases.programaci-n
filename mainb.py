from modelsb import Biblioteca, UsuarioBiblioteca

material1 = Biblioteca("Cien años de soledad", "Gabriel Garcia Marquez", "Libro", 1967, 8)
material2 = Biblioteca("National Geographic", "Editorial National Geographic", "Revista", 2024, 5)
material3 = Biblioteca("El principito", "Antoine de Saint-Exupery", "Libro", 1943, 12)
material4 = Biblioteca("Manual de Biologia", "Editorial McGraw Hill", "Texto escolar", 2022, 6)
material5 = Biblioteca("Harry Potter y la piedra filosofal", "J.K. Rowling", "Libro", 1997, 10)
material6 = Biblioteca("Scientific American", "Editorial Scientific American", "Revista", 2024, 3)
material7 = Biblioteca("El alquimista", "Paulo Coelho", "Libro", 1988, 7)
material8 = Biblioteca("Historia de Mexico", "Elena Poniatowska", "Libro", 2010, 4)
material9 = Biblioteca("Revista de Arquitectura", "Editorial Construye", "Revista", 2023, 2)
material10 = Biblioteca("Matar a un ruiseñor", "Harper Lee", "Libro", 1960, 9)

usuario1 = UsuarioBiblioteca("Wendy Montero", 28, 1001, "wendy.montero@gmail.com")
usuario2 = UsuarioBiblioteca("Alex Perez", 35, 1002, "alex.perez@gmail.com")
usuario3 = UsuarioBiblioteca("Ana Garcia", 22, 1003, "ana.garcia@gmail.com")
usuario4 = UsuarioBiblioteca("Luis Rodriguez", 42, 1004, "luis.rodriguez@gmail.com")
usuario5 = UsuarioBiblioteca("Sofia Martinez", 19, 1005, "sofia.martinez@gmail.com")
usuario6 = UsuarioBiblioteca("Carlos Hernandez", 50, 1006, "carlos.hernandez@gmail.com")
usuario7 = UsuarioBiblioteca("Fany Melendez", 31, 1007, "fany.melendez@gmail.com")
usuario8 = UsuarioBiblioteca("Pedro Sanchez", 26, 1008, "pedro.sanchez@gmail.com")
usuario9 = UsuarioBiblioteca("Camila Ramirez", 39, 1009, "camila.ramirez@gmail.com")
usuario10 = UsuarioBiblioteca("Diego Torres", 24, 1010, "diego.torres@gmail.com")

def mostrar_todos_materiales():
    print("===== LISTA DE TODOS LOS MATERIALES DE LA BIBLIOTECA =====\n")
    material1.mostrar_info()
    material2.mostrar_info()
    material3.mostrar_info()
    material4.mostrar_info()
    material5.mostrar_info()
    material6.mostrar_info()
    material7.mostrar_info()
    material8.mostrar_info()
    material9.mostrar_info()
    material10.mostrar_info()

def mostrar_todos_usuarios():
    print("===== LISTA DE TODOS LOS USUARIOS DE LA BIBLIOTECA =====\n")
    usuario1.mostrar_datos_usuario()
    usuario2.mostrar_datos_usuario()
    usuario3.mostrar_datos_usuario()
    usuario4.mostrar_datos_usuario()
    usuario5.mostrar_datos_usuario()
    usuario6.mostrar_datos_usuario()
    usuario7.mostrar_datos_usuario()
    usuario8.mostrar_datos_usuario()
    usuario9.mostrar_datos_usuario()
    usuario10.mostrar_datos_usuario()

def probar_metodos_individuales():
    print("===== PRUEBAS DE METODOS INDIVIDUALES =====\n")
    print("Prueba de limpiar_espacios:")
    material_prueba = Biblioteca("   La sombra del viento   ", "   Carlos Ruiz Zafon   ", "Libro", 2001, 4)
    print("Antes de limpiar:")
    print("Titulo: '" + material_prueba.titulo + "', Autor: '" + material_prueba.autor_o_editor + "'")
    material_prueba.limpiar_espacios()
    print("Despues de limpiar:")
    print("Titulo: '" + material_prueba.titulo + "', Autor: '" + material_prueba.autor_o_editor + "'\n")

    print("Prueba de prestar_material:")
    usuario3.prestar_material(material3)
    usuario3.mostrar_datos_usuario()
    material3.mostrar_info()

    print("Prueba de devolver_material:")
    usuario3.devolver_material(material3)
    usuario3.mostrar_datos_usuario()
    material3.mostrar_info()

def menu_principal():
    seguir_ejecutando = "si"
    while seguir_ejecutando == "si":
        print("\n===== MENU PRINCIPAL BIBLIOTECA =====")
        print("1. Mostrar todos los materiales")
        print("2. Mostrar todos los usuarios")
        print("3. Probar metodos individuales")
        print("4. Salir")
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            mostrar_todos_materiales()
        elif opcion == "2":
            mostrar_todos_usuarios()
        elif opcion == "3":
            probar_metodos_individuales()
        elif opcion == "4":
            print("Gracias por usar el programa de la biblioteca!")
            seguir_ejecutando = "no"
        else:
            print("Opcion no valida, intenta de nuevo")
if __name__ == "__main__":
    print("BIENVENIDO AL PROGRAMA DE GESTION DE LA BIBLIOTECA")
    menu_principal()