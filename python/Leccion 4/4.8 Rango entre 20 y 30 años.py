# Ejercicio: Rango entre 20 y 30 años
edad = int(input("Digite su edad: "))
# veinte = edad >= 20 and edad < 30
# print(veinte)
# treinta = edad >= 30 and edad < 40
# print(treinta)

#if veinte or treinta:
if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    print ("Estas dentro del rango de los (20'0) a (30'0) años")
 #   if veinte:
 #       print('Estás dentro del rango de los (20\'0) años')
 #   elif treinta:
 #        print('Estás dentro del rango de los (30\'0) años')
 #   else:
 #        print('No estas dentro del rango')  
else:
    print("No estás dentro del rango de los (20\'0) a (30'0) años")


#sintaxis simplificada del operador and 
if (20 <= edad < 30 ) or (30 <= edad < 40):
    print ("Estas dentro del rango de los (30'0) a (40'0) años")
