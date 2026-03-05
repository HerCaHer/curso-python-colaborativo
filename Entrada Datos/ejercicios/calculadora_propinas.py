import os
os.system('cls' if os.name == 'nt' else 'clear')
cuenta_ucsuario, propina_cuenta = float(input("Dame el total de la cuenta: ")), float(input("Dame el total de la propina que deseas dejar: "))
total_propina = (cuenta_ucsuario * propina_cuenta)/100 
print(f"El monto de la propina es: {propina_cuenta}")
print(f"El monto total a pagar es: {cuenta_ucsuario + total_propina}")
