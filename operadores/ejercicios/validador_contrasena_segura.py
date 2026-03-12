import os
os.system('cls' if os.name == 'nt' else 'clear')

print("--- Validador de Seguridad (Sentencias de Control) ---\n")

password = input("Ingresa tu contraseña: ")

# Inicializamos una variable de control (bandera) y una lista de errores
es_valida = True
errores = []

# 1. Validación de Longitud (Operador Relacional)
if len(password) < 8:
    errores.append("Debe tener al menos 8 caracteres.")
    es_valida = False

# 2. Validación de Mayúsculas (Sentencia de Control con any)
if not any(c.isupper() for c in password):
    errores.append("Falta al menos una letra mayúscula.")
    es_valida = False

# 3. Validación de Números (Sentencia de Control con any)
if not any(c.isdigit() for c in password):
    errores.append("Falta al menos un número.")
    es_valida = False

# 4. Validación de Espacios (Operador de Validación)
if ' ' in password:
    errores.append("No debe contener espacios en blanco.")
    es_valida = False

# --- Bloque de Decisión Final ---
print("\n" + "="*30)
if es_valida:
    print("✅ ¡CONTRASEÑA SEGURA!")
    print("Cumple con todos los estándares.")
else:
    print("❌ CONTRASEÑA INSEGURA")
    print("Requisitos faltantes:")
    # Ciclo para mostrar cada error encontrado
    for error in errores:
        print(f"  - {error}")
print("="*30)