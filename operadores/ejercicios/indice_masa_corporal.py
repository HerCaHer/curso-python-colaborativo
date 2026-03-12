import os
os.system('cls' if os.name == 'nt' else 'clear')
peso, altura = float(input("Dame tu peso padresanto: ")),float(input("Dame tu altura padresanto: "))
IMC = peso / (altura ** 2)
if IMC < 18.5 : 
    print("Bajo peso")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Normal")
elif IMC >= 25 and IMC <= 29.9:
    print("Sobrepeso")
elif IMC >= 30:
   print( "Obesidad")
