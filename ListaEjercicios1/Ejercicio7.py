numero1 = int(input("Ingrese el valor del numero1: "))
numero2 = int(input("Ingrese el valor del numero2: "))
iguales = (numero1 == numero2)
diferentes = (numero1 != numero2)
primeroMayor = numero1 > numero2
segundoMayorIgual = numero2 >= numero1
print("¿Son iguales?: ", iguales)
print("¿Son diferentes?: ",diferentes)
print("¿El priemro es mayor que el segundo?: ", primeroMayor)
print("¿El segundo es mayor o igual que el primero?: ", segundoMayorIgual)