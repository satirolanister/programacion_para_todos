import math

# Pedimos al usuario los 2 datos que necesitamos
angulo_lanz = input("Por favor ingrese el angulo de lanzamiento en grados :")
veloci_lanz = input("Por favor ingrese la velocidad de lanzamiento en Km/h:")

# Declaro las variables en cero para despues ser utilizadas
tiempo_max = 0
altura_max = 0
permanencia = 0
df = 0
velocidad_x = 0
velocidad_y = 0


# AQUI FALTA CALCULAR LAS FORMULAS

# Armo la respuesta que le voy ha mostrar al usuario

res = "Altura maxima de la tecnica es : " + str(tiempo_max) + "\n"
res = res + "Altura Maxima Kame Hame Ha es :"+str(altura_max)+"\n"
res = res + "al llega al suelo la distancia es :"+str(df)+"\n"
res = res + "Velocidad en X es :"+str(velocidad_x)+"\n"
res = res + "Velocidad en Y es :"+str(velocidad_y)+"\n"


# muestro la respuesta al usuario
print(res)
