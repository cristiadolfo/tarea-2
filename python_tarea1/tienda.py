print("con ayuda de chatgpt porque no entendi como hacerlo😒")
print("y con ayuda me refiero a que chatgpt lo hizo todo😅")
PRECIO_COMPUTADOR_DE_ESCRITORIO = 2000
PRECIO_COMPUTADOR_PORTATIL = 1200
PRECIO_TABLETA = 3000
PRECIO_VIDEOBEAM = 5000
PRECIO_TELEVISOR = 100

cantidad_computador_escritorio = 0
cantidad_computador_portatil = 0
cantidad_tableta = 0
cantidad_videobeam = 0
cantidad_televisor = 0

def menu():
    while True:
        print("1. Computador de escritorio")
        print("2. Computador portátil")
        print("3. Tableta")
        print("4. Videobeam")
        print("5. Televisor")
        print("6. Facturar")
        
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == "1":
            global cantidad_computador_escritorio
            cantidad_computador_escritorio += 1
        elif opcion == "2":
            global cantidad_computador_portatil
            cantidad_computador_portatil += 1
        elif opcion == "3":
            global cantidad_tableta
            cantidad_tableta += 1
        elif opcion == "4":
            global cantidad_videobeam
            cantidad_videobeam += 1
        elif opcion == "5":
            global cantidad_televisor
            cantidad_televisor += 1
        elif opcion == "6":
            facturar()
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

def facturar():
    total_computador_escritorio = cantidad_computador_escritorio * PRECIO_COMPUTADOR_DE_ESCRITORIO
    total_computador_portatil = cantidad_computador_portatil * PRECIO_COMPUTADOR_PORTATIL
    total_tableta = cantidad_tableta * PRECIO_TABLETA
    total_videobeam = cantidad_videobeam * PRECIO_VIDEOBEAM
    total_televisor = cantidad_televisor * PRECIO_TELEVISOR
    
    total_a_pagar = total_computador_escritorio + total_computador_portatil + total_tableta + total_videobeam + total_televisor
    
    print("\nDetalle de la factura:")
    print(f"Computadores de escritorio: {cantidad_computador_escritorio}")
    print(f"Computadores portátiles: {cantidad_computador_portatil}")
    print(f"Tabletas: {cantidad_tableta}")
    print(f"Videobeams: {cantidad_videobeam}")
    print(f"Televisores: {cantidad_televisor}")
    print(f"Total a pagar: ${total_a_pagar}")

menu()