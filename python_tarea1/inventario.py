print("este ni lo intente, la verdad me dio pereza de leer todo el texto de la tarea 😔😕")
inventario = {}
def comprar():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    existencias = int(input("Ingrese la cantidad de productos a agregar al inventario: "))
    precio_unitario = float(input("Ingrese el precio unitario del producto: "))
    
    if codigo in inventario:
        inventario[codigo]['existencias'] += existencias
    else:
        inventario[codigo] = {'nombre': nombre, 'existencias': existencias, 'precio_unitario': precio_unitario}
    
    print("Compra registrada correctamente.")

def vender():
    codigo = input("Ingrese el código del producto a vender: ")
    cantidad = int(input("Ingrese la cantidad de productos a vender: "))
    
    if codigo in inventario:
        if inventario[codigo]['existencias'] >= cantidad:
            inventario[codigo]['existencias'] -= cantidad
            print("Venta registrada correctamente.")
        else:
            print("No hay suficientes existencias para realizar la venta.")
    else:
        print("El producto no está en el inventario.")

def mostrar_inventario():
    print("\nInventario:")
    for codigo, producto in inventario.items():
        print(f"Código: {codigo}, Nombre: {producto['nombre']}, Existencias: {producto['existencias']}, Precio unitario: ${producto['precio_unitario']}")

def menu():
    while True:
        print("\n1. Comprar")
        print("2. Vender")
        print("3. Mostrar inventario")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            comprar()
        elif opcion == "2":
            vender()
        elif opcion == "3":
            mostrar_inventario()
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
menu()