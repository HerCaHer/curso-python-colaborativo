# Definimos los datos de inicio para el generador de email
nombre = "Samuel Perez Zistecatl"
empresa = "Software Solutions"
dominio = ".com"

#generamos el email con los nombres y la empresa y dominio

nombre_minuscula = nombre.lower()
nombre_limpio = nombre_minuscula.replace(" ",".")

empresa_minuscula = empresa.lower()
empresa_limpia = empresa_minuscula.replace(" ", "")

print("*******Generador de Email*******")
print("Nombre de usuario: ", nombre)
print("Nombre normalizado: ",nombre_limpio)
print(f"Nombre de la empresa: {empresa} ")
print(f"Extencion del dominio: {dominio}")
print("Dominio del e-mail normalizado: "+ "@" + empresa_limpia + dominio)
print("Email Final generado: " + nombre_limpio + "@" + empresa_limpia + dominio)
print("*******Fin del programa*******")