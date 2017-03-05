# \n es un salto de linea
# declaro posibles opciones que puede escojer el usuario
opciones = 'Por favor escoja el material de la casa del cerdito: \n'
opciones = opciones + '1 -> PAJA \n'
opciones = opciones + '2 -> MADERA \n'
opciones = opciones + '3 -> LADRILLO \n'
opciones = opciones + '-> : '

# pido las opciones de la casa segun la variavle que cree anteriormente
casa = int(input(opciones))

if casa == 1:
    print ("Correcto")
    # declaro velocidad viento segun lo que me indique el usuario
    velocidad_viento = int(input("Ingrese velocidad viento: "))

    # definir condicionales dependiendo el viento
    if velocidad_viento > 3.2:
        print("EL LOBO TUMBARA LA CASA DEL CERDITO")
    else:
        print("LA CASA DEL CERDITO NO CAERA")
elif casa == 2:
    print ("Correcto")
    # declaro velocidad viento segun lo que me indique el usuario
    velocidad_viento = int(input("Ingrese velocidad viento: "))
    # definir condicionales dependiendo el viento
    if velocidad_viento > 33.4:
        print("EL LOBO TUMBARA LA CASA DEL CERDITO")
    else:
        print("LA CASA DEL CERDITO NO CAERA")
elif casa == 3:
    print ("Correcto")
    # declaro velocidad viento segun lo que me indique el usuario
    velocidad_viento = int(input("Ingrese velocidad viento: "))
    # definir condicionales dependiendo el viento
    if velocidad_viento > 150:
        print("EL LOBO TUMBARA LA CASA DEL CERDITO")
    else:
        print("LA CASA DEL CERDITO NO CAERA")
else:
    print ("esta opcion no es valida por favor vuelva a intentar ")
