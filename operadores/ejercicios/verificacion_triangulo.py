import os
os.system('cls' if os.name == 'nt' else 'clear')
lado_a, lado_b , lado_c = int(input("Dame el lado a padresanto: ")), int(input("Dame el lado b padresanto: ")), int(input("Dame el lado c padresanto: "))
if ((lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a)) and (lado_a == lado_b == lado_c) : 
    print(f"es un triangulo Equilatero")
if ((lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a)) and ((lado_a == (lado_b != lado_c)) or (lado_a == (lado_c != lado_b)) or (lado_b == (lado_c != lado_a))) : 
    print(f"es un triangulo Isoceles")
if ((lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a)) and (lado_a != lado_b != lado_c) : 
    print(f"es un triangulo escaleno")
else:
    print("Las longitudes no pueden formar un triángulo")