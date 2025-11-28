# -------------------------------
#        CLASES PRINCIPALES
# -------------------------------

class Material:
    """Clase base (superclase) para mostrar herencia."""

    def __init__(self, titulo):
        self.titulo = titulo

    # Metodo polimorfico
    def mostrar_info(self):
        return f"Material: {self.titulo}"


class Libro(Material):
    """Clase Libro que hereda de Material."""

    def __init__(self, titulo, autor, isbn):
        super().__init__(titulo)
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' fue prestado."
        else:
            return f"El libro '{self.titulo}' NO está disponible."

    # Polimorfismo: sobrescritura del metodo
    def mostrar_info(self):
        return f"Libro: {self.titulo} - Autor: {self.autor} - ISBN: {self.isbn}"


class Usuario:
    """Clase Usuario."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        mensaje = libro.prestar()
        if libro.disponible is False:
            self.libros_prestados.append(libro)
        return mensaje


class Biblioteca:
    """Clase Biblioteca."""

    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def prestar_libro(self, titulo, usuario):
        libro = self.buscar_libro(titulo)
        if libro is None:
            return "El libro no existe en la biblioteca."

        if not libro.disponible:
            return "El libro está prestado actualmente."

        usuario.tomar_prestado(libro)
        return f"Préstamo realizado: {usuario.nombre} -> '{libro.titulo}'"


# -------------------------------------
#     EJEMPLO DE USO (EJECUCIÓN)
# -------------------------------------

# Crear biblioteca
biblioteca = Biblioteca()

# Crear libros (herencia + polimorfismo con mostrar_info)
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "9780307474728")
libro2 = Libro("El principito", "Antoine de Saint-Exupéry", "9788498381498")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Crear usuario
usuario1 = Usuario("Anderson")

# Probar el uso de métodos
print("=== Información del material (polimorfismo) ===")
print(libro1.mostrar_info())   # Método sobrescrito

print("\n=== Realizando préstamo ===")
print(biblioteca.prestar_libro("El principito", usuario1))

print("\n=== Estado después del préstamo ===")
print(f"Libros prestados a {usuario1.nombre}:")
for libro in usuario1.libros_prestados:
    print(f"- {libro.titulo}")

print("\nIntento de prestar el mismo libro:")
print(biblioteca.prestar_libro("El principito", usuario1))

