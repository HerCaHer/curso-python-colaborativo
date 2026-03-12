import os
os.system('cls' if os.name == 'nt' else 'clear')
admin = "admin"
password = "1234"
usuario, contrasena = input("Dame el usuario padresanto: "),input("Damel la contraseña: ")
comparacion = f"Acceso concedido {admin}" if usuario == admin and contrasena == password else f"Acceso denegado"
print(comparacion)