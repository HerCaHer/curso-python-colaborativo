import os
os.system('cls' if os.name == 'nt' else 'clear')

edad = int(input("Dame tu edad padresanto: "))
comparacion = f"tu edad {edad} es esta en el rango" if edad >= 18 and edad <=30 else f"tu edad {edad} esta fuera del rango"
print(comparacion)