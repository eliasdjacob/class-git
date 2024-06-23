# ejercicio 4: Área y longitud de un circulo
#Hacer un programa para ingresar el radio de un circulo y se reporte su área y la longitud de la circunferencia.

#Área = Pi * r2
#Longitud = 2 * Pi * r
#En este ejercicio vamos a necesitar importar el modulo math porque tiene el valor de Pi
#Se escribe:   import math

import math

# Se le pide al usuario que ingrese el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Se calcula el área del círculo
area = math.pi * (radio ** 2)

# Se calcula la longitud de la circunferencia
longitud = 2 * math.pi * radio

# Se imprimen los resultados
print(f"El área del círculo es: {area}")
print(f"La longitud de la circunferencia es: {longitud}")