import os
import sys

# Limpieza de pantalla profesional
os.system('cls' if os.name == 'nt' else 'clear')

print("--- Encuesta de Satisfacción ---\n")

try:
    # 1. Nombre (No vacío)
    nombre = input("Nombre: ").strip()
    if not nombre:
        sys.exit("Error: El nombre no puede estar vacío.")

    # 2. Edad (18 - 99)
    edad = int(input("Edad (18-99): "))
    if not (18 <= edad <= 99):
        sys.exit("Error: La edad debe estar entre 18 y 99 años.")

    # 3. Correo (Debe contener '@' y '.')
    correo = input("Correo electrónico: ").strip()
    if "@" not in correo or "." not in correo:
        sys.exit("Error: Formato de correo inválido (falta '@' o '.').")

    # 4. Nivel de Satisfacción (1-5)
    satisfaccion = int(input("Nivel de satisfacción (1-5): "))
    niveles = {1: "Muy insatisfecho", 2: "Insatisfecho", 3: "Neutral", 4: "Satisfecho", 5: "Muy satisfecho"}
    if satisfaccion not in niveles:
        sys.exit("Error: El nivel debe ser un número del 1 al 5.")

    # 5. Comentarios (Opcional)
    comentarios = input("Comentarios adicionales (opcional): ").strip()
    comentarios_final = comentarios if comentarios else "Sin comentarios."

    # --- Resumen Final ---
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Resumen de la Encuesta ---")
    print(f"Usuario:      {nombre}")
    print(f"Edad:         {edad} años")
    print(f"Contacto:     {correo}")
    print(f"Experiencia:  {niveles[satisfaccion]}")
    print(f"Comentarios:  {comentarios_final}")

except ValueError:
    sys.exit("Error: Entrada inválida. Asegúrate de usar números donde se solicita.")