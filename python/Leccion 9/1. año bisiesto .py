# Diseñar un programa que ingresando un año, 
# nos devuelva por consola si es un año bisiesto o no, 
# repetir la acción hasta que el usuario lo decida

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

while True:
    # Se le pide al usuario que ingrese un año
    anio = int(input("Ingrese un año: "))
    
    # Se determina si el año es bisiesto
    if es_bisiesto(anio):
        print(f"El año {anio} es bisiesto.")
    else:
        print(f"El año {anio} no es bisiesto.")

        
    # Se le pregunta al usuario si desea continuar
    continuar = input("¿Desea verificar otro año? (sí/no): ").strip().lower()
    if continuar != 'sí' and continuar != 'si':
        break