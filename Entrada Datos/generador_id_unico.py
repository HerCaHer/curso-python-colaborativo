# Codigo Corregido y se ajusto

from random import randint
print("*** Generador de ID unico ***" )

nombre_usuario = input("¿Cual es tu nombre? ")
nombre_mayusculas = nombre_usuario.upper()
apellido_usuario = input("¿Cual es tu apellido? ")
apellido_mayusculas = apellido_usuario.upper()
ano_nacimiento = input("¿Cual es tu año de nacimiento (YYYY)? ")

print(f"\nHola {nombre_usuario}")
print("\tTu nuevo numero de identificacion (ID) generado por el sistema es: ")
numero_aleatorio = randint(1000, 9999)
id_generado = f"{nombre_mayusculas[0:2]}{apellido_mayusculas[0:2]}{numero_aleatorio}"

print(id_generado)
print("Felicidades")

# Opcion b

#from random import randint
#n, a, y = input("Nombre: "), input("Apellido: "), input("Año (YYYY): ")
#print(f"Hola {n}\nID: {n[:2].upper()}{a[:2].upper()}{y[2:]}-{randint(100,999)}")