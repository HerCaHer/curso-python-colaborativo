import os
os.system('cls' if os.name == 'nt' else 'clear')
monto_compra, tipo_cliente = float(input("Dame el monto de compra padresanto: ")), int(input("Dame tipo de cliente (1: Regular, 2: Premium): "))
if tipo_cliente == 2 and monto_compra > 1000 : 
    monto_total = (monto_compra * 15)/100
    print(f"Se aplico a {monto_compra} el 15% descuento: {monto_compra-monto_total}")
if tipo_cliente == 2 and monto_compra <= 1000 :
    monto_total = (monto_compra * 10)/100
    print(f"Se aplico a {monto_compra} el 10% descuento: {monto_compra-monto_total}")
if tipo_cliente == 1 and monto_compra > 1000 :
    monto_total = (monto_compra * 5)/100
    print(f"Se aplico a {monto_compra} el 5% descuento: {monto_compra-monto_total}")
if tipo_cliente == 1 and monto_compra <= 1000 :
    print(f"No se aplico a {monto_compra} el descuento: {monto_compra-monto_total}")