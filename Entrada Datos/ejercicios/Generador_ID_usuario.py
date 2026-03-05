import os
from random import randint
os.system('cls' if os.name == 'nt' else 'clear')
nombre_usuario , apellido_usuario, anio_usuario = input("Dame tu Nombre padresanto: "), input("Dame tu primer apellido padresanto: "), input("Dame tu año do nacimento padresanto: ")
print(f"\nFelicidades por tu matricula")
numero_random = randint(100,999)
print(f"{nombre_usuario.upper()[0:2]}{apellido_usuario.lower()[0:3]}{anio_usuario[0:2]}{numero_random}")