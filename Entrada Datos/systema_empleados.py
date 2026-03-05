print("***Sistema de Empleados***")
nombre_empleado = str(input("Nombre del empleado "))
edad_empleado = int(input("Edad del Empleado "))
salario_empleado = float(input("Ingresa el salario: "))
es_jefe_departamento = input("Es jefe departamento(Si/NO) ")

# Vamos a convertit un tipo bool la cariable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == "si"


print("\nDatos del empleado")
print(f"Nombre: {nombre_empleado}")
print(f"Edad: {edad_empleado}")
print(f"Salario del empleado: {salario_empleado:.2f}")
print(f"Es jefe de departamento?: {es_jefe_departamento}")