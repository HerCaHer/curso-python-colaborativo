import os
os.system('cls' if os.name == 'nt' else 'clear')
grados_celsius = float(input("Dame la temperatura en Grados celsius: " ))

formula_resuelta = (grados_celsius * (9/5)) + 32
print(f"la conversion de {grados_celsius} a Fahrenheit es: {formula_resuelta:.2f}")