# Programa: Recoleccion de datos de clientes y productos
# Autor: Anderson
# Instructor: Mairon Salazar
# Descripcion: Programa basico para ingresar y mostrar datos de clientes y productos.

# Solicitar datos del cliente
print("=== Registro de Cliente ===")
nombre = input("Ingrese el nombre del cliente: ")
correo = input("Ingrese el correo del cliente: ")
telefono = input("Ingrese el telefono del cliente: ")

# Guardar los datos en un diccionario
cliente = {
    "nombre": nombre,
    "correo": correo,
    "telefono": telefono
}

# Solicitar datos del producto
print("\n=== Registro de Producto ===")
nombre_producto = input("Ingrese el nombre del producto: ")

# Validar que el precio sea un numero positivo
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio > 0:
            break
        else:
            print("El precio debe ser un numero positivo.")
    except:
        print("Debe ingresar un numero valido para el precio.")

# Validar cantidad disponible
while True:
    try:
        cantidad = int(input("Ingrese la cantidad disponible: "))
        if cantidad >= 0:
            break
        else:
            print("La cantidad no puede ser negativa.")
    except:
        print("Debe ingresar un numero valido para la cantidad.")

# Guardar datos del producto
producto = {
    "nombre": nombre_producto,
    "precio": precio,
    "cantidad": cantidad
}

# Mostrar la informacion ingresada
print("\n=== Informacion Ingresada ===")
print("Cliente:")
print(f"  Nombre: {cliente['nombre']}")
print(f"  Correo: {cliente['correo']}")
print(f"  Telefono: {cliente['telefono']}")

print("\nProducto:")
print(f"  Nombre: {producto['nombre']}")
print(f"  Precio: ${producto['precio']}")
print(f"  Cantidad disponible: {producto['cantidad']}")

print("\nRegistro completado correctamente.")
