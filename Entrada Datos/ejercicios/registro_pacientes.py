"""import random
import string

longitud = 2
# Genera una lista de letras y las une en una cadena
letras_aleatorias = ''.join(random.choices(string.ascii_letters, k=longitud))
print(letras_aleatorias)
import random
import string

# Conjunto de caracteres
todos = string.digits + string.punctuation

# Generar una cadena de 10 caracteres aleatorios
longitud = 10
contrasena = ''.join(random.choices(todos, k=longitud))
print(contrasena)"""
import random
import string
import os
os.system('cls' if os.name == 'nt' else 'clear')
print("--- Generador de Contraseñas Seguras ---\n")
longitud = int(input("Longitud deseada (mínimo 8): "))
quiere_mayus = input("¿Incluir mayúsculas? (si/no): ").lower() == "si"
quiere_nums = input("¿Incluir números? (si/no): ").lower() == "si"
quiere_syms = input("¿Incluir símbolos? (si/no): ").lower() == "si"

# 2. Validación de longitud con un diccionario (estilo que prefieres)
validacion = {True: "Longitud aceptable", False: "Alerta: Longitud muy corta (mínimo 8)"}
print(f"\nEstado: {validacion[longitud >= 8]}")

# 3. Construcción del pool de caracteres
# Iniciamos con minúsculas (obligatorias por defecto para asegurar contenido)
caracteres = string.ascii_lowercase
caracteres += string.ascii_uppercase if quiere_mayus else ""
caracteres += string.digits if quiere_nums else ""
caracteres += string.punctuation if quiere_syms else ""

# 4. Generación de la contraseña
# random.choices selecciona caracteres al azar del pool creado
password = ''.join(random.choices(caracteres, k=longitud))

print(f"Tu nueva contraseña es: {password}")