# importo libreria matematicas
#prueba jonathan
import math

# declaro velocidad viento segun lo que me indique el usuario
velocidad_viento = int(input("Ingrese velocidad viento: "))

# definir condicionales dependiendo el viento
if velocidad_viento < 3.2:
    print("Es paja")
elif velocidad_viento < 33.4:
    print("Es madera")
else:
    print("Es ladrillo")
