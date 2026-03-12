import os
os.system('cls' if os.name == 'nt' else 'clear')
calcular_anio = int(input("Dame un anio padresanto(4 dijitos): "))

comparacion = f"El año {calcular_anio} es bisiesto" if (calcular_anio % 4 == 0 and calcular_anio % 100 != 0) or (calcular_anio % 400 == 0) else f"El año {calcular_anio} no es bisiesto"
print(comparacion)