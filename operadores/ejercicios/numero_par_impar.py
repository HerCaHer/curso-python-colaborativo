import os
os.system('cls' if os.name == 'nt' else 'clear')
numero = int(input("Dame un numero padresanto: "))
comparacion = f"El numero {numero} es par" if ((numero % 2) == 0) else f"el numero {numero} es impar"
print(comparacion)