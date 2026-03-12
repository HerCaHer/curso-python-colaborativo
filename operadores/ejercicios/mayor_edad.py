import os
os.system('cls' if os.name == 'nt' else 'clear')
edad = int(input("Dame tu edad padresanto: "))
edad = (edad >= 18)
print(f"es mayor de edad: {edad}")