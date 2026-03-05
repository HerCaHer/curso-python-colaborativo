print("*** Generador de Emails ***")
nombre_usuario, apellidos_usuario, nombre_empresa, extencion_dominio = input("Nombre de usuario: "),input("Apellidos del usuario: "), input("Dame el nombre de la empresa: "), input("Dame la extencion de dominio: ") 
nombre_minus = nombre_usuario.lower()
nombre_normalizado = nombre_minus.replace(" ",".")
apellido_minus = apellidos_usuario.lower()
apellido_normalizado = apellido_minus.replace(" ",".")
empresa_minus = nombre_empresa.lower()
nombre_empresa_normalizada =  empresa_minus.replace(" ","")

print(f"El correo generado es: {nombre_normalizado}.{apellido_normalizado}@{nombre_empresa_normalizada}{extencion_dominio}")

# solucion mas pequeña
#print("*** Generador de Emails ***")
#nombre, apellidos, empresa, dominio = input("Nombre: "), input("Apellidos: "), input("Empresa: "), input("Extensión de dominio: ")
#print(f"El correo generado es: {nombre.lower().replace(' ', '.')}.{apellidos.lower().replace(' ', '.')}@{empresa.lower().replace(' ', '')}{dominio}")