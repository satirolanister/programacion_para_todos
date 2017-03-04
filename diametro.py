import math

pi = math.pi
diametro = int
area = int(input(" Ingrese el area del circulo: "))
diametro = ((4 * area) / pi) ** (1/2)
print("El diametro del circulo es :" + str(diametro))
