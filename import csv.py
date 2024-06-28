import csv
def menu():
    while True:
        print("\Bienvenido al Sistema de Gestión de Inventario")
        print("1. Agregar producto al inventario")
        print("2. Leer inventario")
        print("3. Clasificar productos y generar archivo de texto")
        print("4. Salir")
        
        op = input("Porfavor elija una opción: (1-4) ")
        
        if op == '1':
            agregar_producto()
        elif op == '2':
            leer_inventario()
        elif op == '3':
            clasificar_productos()
        elif op == '4':
            print("Hasta pronto, cerrando programa...")
            break
        else:
            print("Error opción inválida.")

def agregar_producto():
    with open('inventario.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        id = input("ID del producto: ")
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría (Electrónica, Textil o Calzado): ")
        precio = input("Precio del producto: ")
        writer.writerow([id, nombre, categoria, precio])

    print("Producto añadido exitosamente.")

def leer_inventario():
    try:
        with open('inventario.csv', 'r') as file:
            for line in file:
                print(line.strip())
    except ValueError:
        print("Error el archivo no existe.")

def clasificar_productos():
    categorias = {'Electrónica': [], 'Textil': [], 'Calzado': []}
    try:
        with open('inventario.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                categoria = row[2]
                if categoria in categorias:
                    categorias[categoria].append(f"{row[1]} - Precio: {row[3]}")
        
        with open('clasificacion_productos.txt', 'w') as file:
            for categoria, productos in categorias.items():
                file.write(f"{categoria}:\n")
                for producto in productos:
                    file.write(f"{producto}\n")
                file.write("\n")
        print("Archivo de clasificación generado.")
    except ValueError:
        print("Error el archivo no existe")
menu()

