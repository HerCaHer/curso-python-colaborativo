print("*** Generador de email****")
nombre_usuario ="Ubaldo Acosta Soto"
#metodo .lower para convertir a minusculas
nombre_usuario_normalizado =nombre_usuario.lower()
#metodo. replace para pasar de " " a "."
nombre_usuario_normalizado=nombre_usuario_normalizado.replace(" ", ".")
print(f"Nombre usuario normalizado: {nombre_usuario_normalizado}")

print("\n")



print("*** Generador de email ***")
nombre_empresa = ("Global Mentoring")
extencion_dominio =(".com.mx")

#metodo .lower para pasar a minusculas
nombre_normalizado = nombre_empresa.lower()
#metodo .replace para quitar espacios
nombre_normalizado=nombre_normalizado.replace(" ", "")

print(f"nombre de la empresa {nombre_empresa}")
print(f"Extension del dominio: {extencion_dominio} " )
print(f"Dominio de email normalizado: @{nombre_normalizado}")
print(f"Email final generado: {nombre_usuario_normalizado}@{nombre_normalizado}{extencion_dominio}")
