import os
import sys

# Limpieza de pantalla profesional
os.system('cls' if os.name == 'nt' else 'clear')
a = 10
b = 3

#Suma
suma = a + b
print(f"Suma: {suma}")

#Resta
resta = a - b
print(f"Resta: {resta}")

#Multiplicacion
multiplicacion = a * b
print(f"Multiplicacion: {multiplicacion}")

#Division
division = a / b
print(f"Division: {division:.2f}")


# Division entera // 
division_entera = a // b

print(f"Division entera: {division_entera}")

# Modulo (%) residuo de la division
modulo = a % b
print( f"Residuo de la division: {modulo}")

# Exponente (potencia)

exponente = a ** b
print(f"El exponente es: {exponente}")