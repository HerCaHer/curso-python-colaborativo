# Programa: aplicar el concepto de slicing en cadenas de texto

texto = "PROGRAMACION"

# Ejemplo [inicio:fin]
print(texto[0:4]) # Imprime "PROG"

#  Atajos para omitir el inicio o el fin [:fin] o [inicio:]
print(texto[:4]) #Imprime "PROG"    
print(texto[8:]) # Imprime "ACION"

# Indices negativos para contar desde el final
print(texto[-5:]) # Imprime "ACION

# Slicing con pasos [inicio:fin:paso]
print(texto[::-1]) # Imprime "PORMCIN"
