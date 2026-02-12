# Programa reemplazar texto en una cadena
mensaje = "Hola Mundo, Mundo"
print(mensaje)

# Reemplazamos "Mundo" por "Python"
mensaje_nuevo = mensaje.replace("Mundo", "Python")
print(mensaje_nuevo)

# Reemplazamos solo la primera ocurrencia de "Mundo"
solo_uno = mensaje.replace("Mundo", "Dev" , 1)
print(solo_uno)