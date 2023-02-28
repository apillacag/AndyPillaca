PI = 3.141592
opciones = """
    1) Calcular el area del triangulo
    2) Calcular el area del circulo
    3) Calcular el area del cuadrado
"""
print(opciones)
opcion = int(input("Ingrese la opcion: "))
if(opcion == 1):
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    print("El area del triangulo es: ", (base*altura)/2)
elif(opcion == 2):
    radio =int(input("Ingrese el radio: "))
    print("El area del circulo es: ", (radio*(PI**2)))
elif(opcion == 3):
    lado = int(input("Ingrese el lado del cuadrado: "))
    print("El area del cuadrado es: ", lado**2)
else:
    print("Ingrese una opcion valida")
