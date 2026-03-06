from models import *

peliculas = [
    Peliculas("Inception", "Ciencia ficción", 70),
    Peliculas("The Godfather", "Crimen", 80),
    Peliculas("The Dark Knight", "Acción", 75),
    Peliculas("Pulp Fiction", "Crimen", 65),
    Peliculas("The Shawshank Redemption", "Drama", 60),
    Peliculas("The Matrix", "Ciencia ficción", 70),
    Peliculas("Forrest Gump", "Drama", 55),
    Peliculas("The Lord of the Rings", "Fantasía", 80),
    Peliculas("The Avengers", "Superhéroes", 75),
    Peliculas("Gladiator", "Acción", 65)
]
usuarios = [
    Usuario("Juan Pérez", "juanperez@gmail.com", 47, "2498298417", "1234-5678-9012"),
    Usuario("Yeidckol Rodriguez", "yeidckolrodriguez@gmail.com", 19, "2411963415", "2345-6789-0123"),
    Usuario("Irving Dominguez", "irvingdominguez@gmail.com", 25, "2961034460", "3456-7890-1234"),
    Usuario("Karen Morales", "karenmorales@gmail.com", 19, "9611757951", "4567-8901-2345"),
    Usuario("Adonai Ramirez", "adonairamirez@gmail.com", 19, "2498298417", "5678-9012-3456"),
    Usuario("Madison Montero", "madisonmontero@gmail.com", 22, "2491779390", "6789-0123-4567"),
    Usuario("Estefania Palacios", "estefaniapalacios@gmail.com", 19, "2221553860", "6789-0123-4567"),
    Usuario("Daniel Vallejo", "danielvallejo@gmail.com", 19, "2491398508", "7890-1234-5678"),
    Usuario("Leonardo Nava", "leonardonava@gmail.com", 19, "2212095596", "7890-1234-5678"),
    Usuario("Melanie Martinez", "melanie@gmail.com", 20, "2218213826", "8901-2345-6789")
]

dulces = [
    Dulceria("Palomitas", 120),
    Dulceria("Nachos", 100),
    Dulceria("Refresco", 80),
    Dulceria("Chocolate", 50),
    Dulceria("Gomitas", 50),
    Dulceria("Chicles", 30),
    Dulceria("Caramelos", 20),
    Dulceria("Barquillos", 60),
    Dulceria("Chocorroles", 35),
    Dulceria("Hot dogs", 50)
]

def mostrar_peliculas():
    print("\nPELÍCULAS DISPONIBLES")
    for i, p in enumerate(peliculas):
        print(i+1, "-", p.titulo, "-", p.genero, "- $", p.precio)

def mostrar_usuarios():
    print("\nUSUARIOS REGISTRADOS")
    for i, u in enumerate(usuarios):
        print(i+1, "-", u.nombre)

def mostrar_dulces():
    print("\nDULCERÍA")
    for i, d in enumerate(dulces):
        print(i+1, "-", d.dulce, "- $", d.precio)

def hacer_reserva():

    mostrar_usuarios()
    usuario_opcion = int(input("Selecciona usuario: "))
    usuario = usuarios[usuario_opcion-1]

    mostrar_peliculas()
    pelicula_opcion = int(input("Selecciona película: "))
    pelicula = peliculas[pelicula_opcion-1]

    boletos = int(input("¿Cuántos boletos deseas?: "))

    total_boletos = pelicula.precio * boletos

    dulces_total = 0

    print("\n¿Quieres comprar dulces?")
    print("1. Sí")
    print("2. No")
    opcion = input("Opción: ")
    if opcion == "1":

        mostrar_dulces()
        elegir = int(input("Selecciona dulce (0 para terminar): "))

        while elegir != 0:
            dulce = dulces[elegir-1]
            dulces_total += dulce.precio
            elegir = int(input("Otro dulce (0 para terminar): "))
            total = total_boletos + dulces_total

    print("\n----- RESUMEN DE COMPRA -----")
    print("Usuario:", usuario.nombre)
    print("Película:", pelicula.titulo)
    print("Boletos:", boletos)
    print("Total boletos:", total_boletos)
    print("Total dulcería:", dulces_total)
    print("TOTAL A PAGAR:", total)

while True:

    print("\n=== SISTEMA DE CINE ===")
    print("1. Ver películas")
    print("2. Hacer reserva")
    print("3. Salir")

    opcion = input("Selecciona opción: ")

    if opcion == "1":
        mostrar_peliculas()

    elif opcion == "2":
        hacer_reserva()

    elif opcion == "3":
        print("Gracias por usar el sistema del cine")
        break