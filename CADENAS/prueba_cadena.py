from idlelib.replace import replace
# como lo solucione
print("*** Generador de Email***")
nombre_usuario= "Ubaldo Acosto Soto"
print(f"Nombre usuario: {nombre_usuario}")
nombre_usuario_minusculas =nombre_usuario.lower()
nombre_usuario_normalizado = nombre_usuario_minusculas.replace(" ",".")
print(f"Nombre usuario normalizado: {nombre_usuario_normalizado}")




#como lo propone el curso
#generador de Email
print("*** Generador de Email***")
#tiene espacios al inicio y al final
nombre_usuario ="   Ubaldo Acosto Soto    "
print("Nombre usuario normalizado: ", nombre_usuario)

#usar el metodo .lower para pasar a minusculas
nombre_normalizado =nombre_normalizado.lower()

#usar el metodo .replace para cambiar espacios por puntos
nombre_normalizado=nombre_normalizado.replace(" ",".")

#usar el metodo strip para quitar espacios al inicio y al fin de la cadena
nombre_normalizado = nombre_usuario.strip()

print(f"Nombre usuario normalizado: {nombre_normalizado}")

