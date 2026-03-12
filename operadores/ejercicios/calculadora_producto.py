import os
os.system('cls' if os.name == 'nt' else 'clear')
print("*** Calculadora simple ***")
numero_1, numero_2 = float(input("Dame el primer numero entero pf: ")), float(input("Dame el segundo numero entero pf: "))
print(f"la el producto de los numero es: {numero_1*numero_2}")