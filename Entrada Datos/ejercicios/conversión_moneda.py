import os
os.system('cls' if os.name == 'nt' else 'clear')
moneda_mx = float(input("Dame cuantos pesos mexicanos quieres convertir: "))
a_dolar = moneda_mx * 0.056
a_euro = moneda_mx * 0.049
print(f"El tipo de cambio de {moneda_mx} a dolares es {a_dolar:.2f} y a dolares es {a_euro:.2f}")