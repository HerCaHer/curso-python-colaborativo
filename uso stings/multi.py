# Inicializamos la variable acumuladora
resultado = 0

# Ciclo para leer 5 números
for contador in range(1, 6):
    numero = float(input(f"Ingrese el número {contador}: "))
    resultado += numero * contador  # Se multiplica por el contador y se suma al resultado

# Mostrar el resultado final
print("El valor final de la variable es:", resultado)