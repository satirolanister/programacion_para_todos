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
 #termina proyecto

#---------------------------------------------------------------------------------------------------
>>> import math
material_paja = float(3.2)
material_madera = float(33.4)
material_ladrillo = float(150)
Vel_Viento = int(input("Ingrese la velocidad con la que el lobo sopla: "))
>>> if Vel_Viento < 3.2:
    print("El lobo puede tumbar la casa hecha de paja")
elif Vel_Viento < 33.4:
    print("El lobo puede tumbar la casa hecha de paja y madera")
elif velocidad_viento <= 150:
    print("El lobo puede tumbar la casa hecha de paja, madera y ladrillo")
else:
    print("El lobo no puede tirar la casa")
