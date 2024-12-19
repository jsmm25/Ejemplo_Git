def duplicar_numeros(lista):
    return [x * 2 for x in lista]

def suma_de_cuadrados(a, b):
    return a**2 + b**2

def calcular_area_rectangulo(base, altura):
    return base * altura

def menu():

    while True:
        print("\n--- MENÚ ---")
        print("1. Duplicar valores en una lista")
        print("2. Calcular la suma de los cuadrados de dos números")
        print("3. Calcular el área de un rectángulo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                lista = input("Ingrese los números separados por comas: ")
                numeros = [float(num) for num in lista.split(",")]
                duplicados = duplicar_numeros(numeros)
                print(f"Lista duplicada: {duplicados}")
            except ValueError:
                print("Por favor, ingrese solo números separados por comas.")
        
        elif opcion == "2":
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
                suma = suma_de_cuadrados(a, b)
                print(f"La suma de los cuadrados es: {suma}")
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos.")
        
        elif opcion == "3":
            try:
                base = float(input("Ingrese la base del rectángulo: "))
                altura = float(input("Ingrese la altura del rectángulo: "))
                area = calcular_area_rectangulo(base, altura)
                print(f"El área del rectángulo es: {area}")
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos.")
        
        elif opcion == "4":
            print("Saliendo del programa. ¡Adiós!")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")


menu()

