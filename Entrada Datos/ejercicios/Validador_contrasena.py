import os
os.system('cls' if os.name == 'nt' else 'clear')
contrasena = input("dame una contraseña padre")

tiene_numero = any(c.isdigit() for c in contrasena)
es_larga = len(contrasena) >= 8

print(f"La seguridad de la contraseña es: {es_larga}")