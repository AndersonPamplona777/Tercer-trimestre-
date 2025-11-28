
#no tengo java instalado en mi pc pero aqui te dejo el codigo en java que me pediste

# // #-------------------------------
# //        CLASES PRINCIPALES
# // -------------------------------

# // Superclase (Herencia)
# class Material {
#     protected String titulo;

#     public Material(String titulo) {
#         this.titulo = titulo;
#     }

#     // Método polimórfico
#     public String mostrarInfo() {
#         return "Material: " + titulo;
#     }
# }


# // Subclase Libro que hereda de Material
# class Libro extends Material {
#     private String autor;
#     private String isbn;
#     private boolean disponible;

#     public Libro(String titulo, String autor, String isbn) {
#         super(titulo);
#         this.autor = autor;
#         this.isbn = isbn;
#         this.disponible = true;
#     }

#     public String prestar() {
#         if (disponible) {
#             disponible = false;
#             return "El libro '" + titulo + "' fue prestado.";
#         }
#         return "El libro '" + titulo + "' NO está disponible.";
#     }

#     public boolean estaDisponible() {
#         return disponible;
#     }

#     // Polimorfismo: sobrescritura del método mostrarInfo()
#     @Override
#     public String mostrarInfo() {
#         return "Libro: " + titulo + " - Autor: " + autor + " - ISBN: " + isbn;
#     }
# }


# // Clase Usuario
# class Usuario {
#     private String nombre;
#     private java.util.ArrayList<Libro> librosPrestados;

#     public Usuario(String nombre) {
#         this.nombre = nombre;
#         this.librosPrestados = new java.util.ArrayList<>();
#     }

#     public String tomarPrestado(Libro libro) {
#         String mensaje = libro.prestar();
#         if (!libro.estaDisponible()) {
#             librosPrestados.add(libro);
#         }
#         return mensaje;
#     }

#     public java.util.ArrayList<Libro> getLibrosPrestados() {
#         return librosPrestados;
#     }

#     public String getNombre() {
#         return nombre;
#     }
# }


# // Clase Biblioteca
# class Biblioteca {
#     private java.util.ArrayList<Libro> libros;

#     public Biblioteca() {
#         libros = new java.util.ArrayList<>();
#     }

#     public void agregarLibro(Libro libro) {
#         libros.add(libro);
#     }

#     public Libro buscarLibro(String titulo) {
#         for (Libro libro : libros) {
#             if (libro.titulo.equalsIgnoreCase(titulo)) {
#                 return libro;
#             }
#         }
#         return null;
#     }

#     public String prestarLibro(String titulo, Usuario usuario) {
#         Libro libro = buscarLibro(titulo);

#         if (libro == null) {
#             return "El libro no existe en la biblioteca.";
#         }

#         if (!libro.estaDisponible()) {
#             return "El libro ya está prestado.";
#         }

#         usuario.tomarPrestado(libro);
#         return "Préstamo realizado: " + usuario.getNombre() + " -> '" + titulo + "'";
#     }
# }


# // -------------------------------
# //          PROGRAMA PRINCIPAL
# // -------------------------------
# public class Main {
#     public static void main(String[] args) {

#         // Crear biblioteca
#         Biblioteca biblioteca = new Biblioteca();

#         // Crear libros
#         Libro libro1 = new Libro("Cien años de soledad", "Gabriel García Márquez", "9780307474728");
#         Libro libro2 = new Libro("El principito", "Antoine de Saint-Exupéry", "9788498381498");

#         // Agregar libros
#         biblioteca.agregarLibro(libro1);
#         biblioteca.agregarLibro(libro2);

#         // Crear usuario
#         Usuario usuario = new Usuario("Anderson");

#         System.out.println("=== Polimorfismo ===");
#         System.out.println(libro1.mostrarInfo());

#         System.out.println("\n=== Realizar préstamo ===");
#         System.out.println(biblioteca.prestarLibro("El principito", usuario));

#         System.out.println("\n=== Libros prestados ===");
#         for (Libro l : usuario.getLibrosPrestados()) {
#             System.out.println("- " + l.mostrarInfo());
#         }

#         System.out.println("\nIntento de prestar el mismo libro:");
#         System.out.println(biblioteca.prestarLibro("El principito", usuario));
#     }
# }
# // -------------------------------
# //        CLASES PRINCIPALES
# // -------------------------------

# // Superclase (Herencia)
# class Material {
#     protected String titulo;

#     public Material(String titulo) {
#         this.titulo = titulo;
#     }

#     // Método polimórfico
#     public String mostrarInfo() {
#         return "Material: " + titulo;
#     }
# }


# // Subclase Libro que hereda de Material
# class Libro extends Material {
#     private String autor;
#     private String isbn;
#     private boolean disponible;

#     public Libro(String titulo, String autor, String isbn) {
#         super(titulo);
#         this.autor = autor;
#         this.isbn = isbn;
#         this.disponible = true;
#     }

#     public String prestar() {
#         if (disponible) {
#             disponible = false;
#             return "El libro '" + titulo + "' fue prestado.";
#         }
#         return "El libro '" + titulo + "' NO está disponible.";
#     }

#     public boolean estaDisponible() {
#         return disponible;
#     }

#     // Polimorfismo: sobrescritura del método mostrarInfo()
#     @Override
#     public String mostrarInfo() {
#         return "Libro: " + titulo + " - Autor: " + autor + " - ISBN: " + isbn;
#     }
# }


# // Clase Usuario
# class Usuario {
#     private String nombre;
#     private java.util.ArrayList<Libro> librosPrestados;

#     public Usuario(String nombre) {
#         this.nombre = nombre;
#         this.librosPrestados = new java.util.ArrayList<>();
#     }

#     public String tomarPrestado(Libro libro) {
#         String mensaje = libro.prestar();
#         if (!libro.estaDisponible()) {
#             librosPrestados.add(libro);
#         }
#         return mensaje;
#     }

#     public java.util.ArrayList<Libro> getLibrosPrestados() {
#         return librosPrestados;
#     }

#     public String getNombre() {
#         return nombre;
#     }
# }


# // Clase Biblioteca
# class Biblioteca {
#     private java.util.ArrayList<Libro> libros;

#     public Biblioteca() {
#         libros = new java.util.ArrayList<>();
#     }

#     public void agregarLibro(Libro libro) {
#         libros.add(libro);
#     }

#     public Libro buscarLibro(String titulo) {
#         for (Libro libro : libros) {
#             if (libro.titulo.equalsIgnoreCase(titulo)) {
#                 return libro;
#             }
#         }
#         return null;
#     }

#     public String prestarLibro(String titulo, Usuario usuario) {
#         Libro libro = buscarLibro(titulo);

#         if (libro == null) {
#             return "El libro no existe en la biblioteca.";
#         }

#         if (!libro.estaDisponible()) {
#             return "El libro ya está prestado.";
#         }

#         usuario.tomarPrestado(libro);
#         return "Préstamo realizado: " + usuario.getNombre() + " -> '" + titulo + "'";
#     }
# }


# // -------------------------------
# //          PROGRAMA PRINCIPAL
# // -------------------------------
# public class Main {
#     public static void main(String[] args) {

#         // Crear biblioteca
#         Biblioteca biblioteca = new Biblioteca();

#         // Crear libros
#         Libro libro1 = new Libro("Cien años de soledad", "Gabriel García Márquez", "9780307474728");
#         Libro libro2 = new Libro("El principito", "Antoine de Saint-Exupéry", "9788498381498");

#         // Agregar libros
#         biblioteca.agregarLibro(libro1);
#         biblioteca.agregarLibro(libro2);

#         // Crear usuario
#         Usuario usuario = new Usuario("Anderson");

#         System.out.println("=== Polimorfismo ===");
#         System.out.println(libro1.mostrarInfo());

#         System.out.println("\n=== Realizar préstamo ===");
#         System.out.println(biblioteca.prestarLibro("El principito", usuario));

#         System.out.println("\n=== Libros prestados ===");
#         for (Libro l : usuario.getLibrosPrestados()) {
#             System.out.println("- " + l.mostrarInfo());
#         }

#         System.out.println("\nIntento de prestar el mismo libro:");
#         System.out.println(biblioteca.prestarLibro("El principito", usuario));
#     }
# }
