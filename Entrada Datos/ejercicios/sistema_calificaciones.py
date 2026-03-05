import os
os.system('cls' if os.name == 'nt' else 'clear')
calificacion_1 , calificacion_2, calificacion_3 = float(input("Dame tu primera calificacion padresanto: ")), float(input("Dame tu segunda calificacion padresanto: ")), float(input("Dame tu teercera calificacion padresanto: "))
calificacion_final = (calificacion_1 + calificacion_2 + calificacion_3)/3
calificacion_final = f"aprobado" if calificacion_final >= 6 else "reprobado"

print(calificacion_final)