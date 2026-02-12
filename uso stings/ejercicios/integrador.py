frase = input("Ingresa una frase algo larga pa:")

frase_mayus = frase.upper()
longitud_frase = len(frase)
frase_sin_espacios =  frase.replace(" ","")
encontrar_palabra = frase.find("python")

print(f"La frase en mayusculas: {frase_mayus}")
print(f"La longitud de la frase es: {longitud_frase}")
print(f"Las primeras 3 letras son: {frase[0:3]}")
print(f"La frase sin espacios es: {frase_sin_espacios}")
print(f"La posicion de la palabra 'python' es:{encontrar_palabra}")