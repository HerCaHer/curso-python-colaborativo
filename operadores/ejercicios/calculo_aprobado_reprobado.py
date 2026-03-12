import os
os.system('cls' if os.name == 'nt' else 'clear')

calificacion = int(input("Dame tu calificacion padresanto(0 - 100): "))
comparacion = f"La calificacion: {calificacion}  esta aprobado" if calificacion >= 60 and calificacion <=100 else f"La calificacion: {calificacion} estas reprobado"
print(comparacion)