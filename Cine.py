class Peliculas:
    def __init__(self, titulo, genero, precio):
        self.titulo = titulo
        self.genero = genero
        self.precio = precio

    def mostrar_info(self):
        lista = [self.titulo, self.genero, self.precio]
pelicula1 = Peliculas("Inception", "Ciencia ficción", 70)
pelicula1.mostrar_info()
pelicula2 = Peliculas("The Godfather", "Crimen", 80)
pelicula2.mostrar_info()
pelicula3 = Peliculas("The Dark Knight", "Acción", 75)
pelicula3.mostrar_info()
pelicula4 = Peliculas("Pulp Fiction", "Crimen", 65)
pelicula4.mostrar_info()
pelicula5 = Peliculas("The Shawshank Redemption", "Drama", 60)
pelicula5.mostrar_info()
pelicula6 = Peliculas("The Matrix", "Ciencia ficción", 70)
pelicula6.mostrar_info()
pelicula7 = Peliculas("Forrest Gump", "Drama", 55)
pelicula7.mostrar_info()
pelicula8 = Peliculas("The Lord of the Rings: The Fellowship of the Ring", "Fantasía", 80)
pelicula8.mostrar_info()
pelicula9 = Peliculas("The Avengers", "Superhéroes", 75)
pelicula9.mostrar_info()
pelicula10 = Peliculas("Gladiator", "Acción", 65)
pelicula10.mostrar_info()

class Usuario:
    def __init__(self, nombre, correo, edad, numero_de_telefono, numero_de_tarjeta):
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.numero_de_telefono = numero_de_telefono
        self.numero_de_tarjeta = numero_de_tarjeta
    def mostrar_info(self):
        lista = [self.nombre, self.correo, self.edad, self.numero_de_telefono, self.numero_de_tarjeta]
usuario1 = Usuario("Juan Pérez", "juanperez@gmail.com", 47, "2498298417", "1234-5678-9012")
usuario1.mostrar_info()
usuario2 = Usuario("Yeidckol Rodriguez", "yeidckolrodriguez@gmail.com", 19, "2411963415", "2345-6789-0123")
usuario2.mostrar_info()
usuario3 = Usuario("Irving Dominguez", "irvingdominguez@gmail.com", 25, "2961034460", "3456-7890-1234")
usuario3.mostrar_info()
usuario4 = Usuario("Karen Morales", "karenmorales@gmail.com", 19, "9611757951", "4567-8901-2345")
usuario4.mostrar_info()
usuario5 = Usuario("Adonai Ramirez", "adonairamirez@gmail.com", 19, "2498298417", "5678-9012-3456")
usuario5.mostrar_info()
usuario6 = Usuario("Madison Montero", "madisonmontero@gmail.com", 22, "2491779390", "6789-0123-4567")
usuario6.mostrar_info()
usuario7 = Usuario("Estefania Palacios", "estefaniapalacios@gmail.com", 19, "2221553860", "6789-0123-4567")
usuario7.mostrar_info()
usuario8 = Usuario("Daniel Vallejo", "danielvallejo@gmail.com", 19, "2491398508", "7890-1234-5678")
usuario8.mostrar_info()
usuario9 = Usuario("Leonardo Nava", "leonardonava@gmail.com", 19, "2212095596", "7890-1234-5678") 
usuario9.mostrar_info()
usuario10 = Usuario("Melanie Martinez", "melanie@gmail.com", 20, "2218213826", "8901-2345-6789")
usuario10.mostrar_info()

class Dulceria:
    def __init__(self, dulce, precio):
        self.dulce = dulce
        self.precio = precio

    def mostrar_info(self):
        lista = [self.dulce, self.precio]
dulce1 = Dulceria("Palomitas", 120)
dulce1.mostrar_info()
dulce2 = Dulceria("Nachos", 100)
dulce2.mostrar_info()
dulce3 = Dulceria("Refresco", 80)
dulce3.mostrar_info()
dulce4 = Dulceria("Chocolate", 50)
dulce4.mostrar_info()
dulce5 = Dulceria("Gomitas", 50)
dulce5.mostrar_info()
dulce6 = Dulceria("Chicles", 30)
dulce6.mostrar_info()
dulce7 = Dulceria("Caramelos", 20)
dulce7.mostrar_info()
dulce8 = Dulceria("Barquillos", 60)
dulce8.mostrar_info()
dulce9 = Dulceria("Chocorroles", 35)
dulce9.mostrar_info()
dulce10 = Dulceria("Hot dogs", 50)
dulce10.mostrar_info()

class Sala:
    def __init__(self, numero_de_sala, capacidad, tipo_de_sala):
        self.numero_de_sala = numero_de_sala
        self.capacidad = capacidad
        self.tipo_de_sala = tipo_de_sala

    def mostrar_info(self):
        lista = [self.numero_de_sala, self.capacidad, self.tipo_de_sala]
sala1 = Sala(1, 100, "2D")
sala1.mostrar_info()
sala2 = Sala(2, 150, "3D")
sala2.mostrar_info()
sala3 = Sala(3, 200, "VIP")
sala3.mostrar_info()
sala4 = Sala(4, 120, "2D")
sala4.mostrar_info()
sala5 = Sala(5, 180, "3D")
sala5.mostrar_info()
sala6 = Sala(6, 220, "VIP")
sala6.mostrar_info()
sala7 = Sala(7, 130, "2D")
sala7.mostrar_info()
sala8 = Sala(8, 170, "3D")
sala8.mostrar_info()
sala9 = Sala(9, 250, "VIP")
sala9.mostrar_info()
sala10 = Sala(10, 140, "2D")
sala10.mostrar_info()