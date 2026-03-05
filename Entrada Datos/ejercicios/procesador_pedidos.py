import os
os.system('cls' if os.name == 'nt' else 'clear')
print(""" *** menu ***
      
Hamburguesa simple: $80

Hamburguesa con queso: $95

Papas fritas: $45

Refresco: $30""")
hamburguesa_simple = 80
hamburguesa_queso = 95
papas_fritas = 45
refresco = 30

pedido_hamburguesa_simple = int(input("Deseas pedir una hamburquesa simple indica el numero (0 si no deseas)")) 

pedido_hamburguesa_queso = int(input("Deseas pedir una hamburquesa con queso indica el numero (0 si no deseas)"))

pedido_papas = int(input("Deseas pedir unas papitas indica el numero (0 si no deseas)"))

pedido_refresco = int(input("Deseas pedir un cherry(refresco) indica el numero (0 si no deseas)"))

total_pedido = (pedido_hamburguesa_simple*hamburguesa_simple) + (hamburguesa_queso * pedido_hamburguesa_queso) + (pedido_papas * papas_fritas) + (pedido_refresco * refresco)
iva = (total_pedido * 8)/100

print(f"el total es {total_pedido+iva}")