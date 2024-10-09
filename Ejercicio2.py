class Libro:
    def __init__(self, titulo, autor, anio_publicacion, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.numero_paginas = numero_paginas

    def mostrar_informacion(self):
        print(f"El titulo del libro es: {self.titulo}")
        print(f"El autor del libro es: {self.autor}")
        print(f"El libro fue publicado en el año {self.anio_publicacion}")
        print(f"El libro cuenta con {self.numero_paginas} paginas")

l1 = Libro("Los juegos del hambre", "Suzanne Collins", "2008", "234")

l1.mostrar_informacion()
