import os
from random import randint
os.system('cls' if os.name == 'nt' else 'clear')
numero_usuario = int(input("Dame un numero del 1 - 10 "))
numero_aleatorio =  randint (1 , 10)
adivinanza = "acertaste" if numero_usuario == numero_aleatorio else "no acertaste"
print(f"{adivinanza} el numero es: {numero_aleatorio} ")