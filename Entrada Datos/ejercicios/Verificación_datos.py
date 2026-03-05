import os
os.system('cls' if os.name == 'nt' else 'clear')

numero_usuario = int(input("Dame un numero cualquiera (Como tu ex): "))

numero_usuario = numero_usuario > 10 

print(f"El resultado de {numero_usuario}" )
