# Programa: funcion bool

# 1. numeros (int y float)

print(bool(0))
print(bool(0.0))
print(bool(42))

# 2. Texto (Strings)
# Cadenas vacias = nada = false
print(bool(""))

# cadena con espacio o texto = Algo = true 

print(bool(" "))
print(bool("Hola"))

# 3. None (Ausencia total)
vacio = None
print(bool(vacio))

print(bool(False))
print(bool(True))