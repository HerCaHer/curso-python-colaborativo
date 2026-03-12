import os
os.system('cls' if os.name == 'nt' else 'clear')
promedio_general, nivel_socioeconomico, hermanos_universidad = float(input("Dame el promedio general padresanto: ")), int(input("Dame tu tipo de nivel socioecoomico (1: Bajo, 2: Medio, 3: Alto): ")), input("tienes hermanos en la universidad(sí/no): ")
if promedio_general >= 8.5 and (nivel_socioeconomico == 1 and hermanos_universidad.strip().upper() == "SI" ) : 
    print(f"Eres candidato a beca")
else:
    print("No eres candidato a beca")