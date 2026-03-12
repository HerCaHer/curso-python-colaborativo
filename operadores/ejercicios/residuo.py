import os
os.system('cls' if os.name == 'nt' else 'clear')
numero_1, numero_2 = int(input("Dame el primer numero entero pf: ")), int(input("Dame el segundo numero entero pf: "))
print(f"la potencia de los numero es: {numero_1%numero_2}")