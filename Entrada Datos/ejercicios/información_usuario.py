import os
os.system('cls' if os.name == 'nt' else 'clear')
nombre_usuario = input("Dame tu nombre completo padresanto: ")
ciudad_usuario = input("Dame la cuidad donde radicas actualmente: ")
profesion_usuario = input("Dame la profecion que ejerces o no: ")

print(f"Hola {nombre_usuario} espero te encuentres bien en {ciudad_usuario} ya que te dedicas a {profesion_usuario}")