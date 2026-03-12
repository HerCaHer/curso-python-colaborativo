print('*** Operadores de Asignación ***')
numero = 5
print(f'Valor de numero: {numero}')
numero = 10
print(f'Valor de numero: {numero}')
cadena = 'Saludos desde Python'
print(f'Valor de la cadena: {cadena}')

x, y, z = 5, 'Hola', -9.15
print(f'Valor de x = {x}, y = {y}, z = {z}')

a = b = c = 10
print(f'Valor a = {a}, b = {b}, c = {c}')

x, y = 5, 10
print(f'Valores iniciales x = {x}, y = {y}')

x, y = y, x
print(f'Invertir los valores x = {x}, y = {y}')

nombre, apellido = input('Ingresa tu nombre y apellido separados por coma: ').split(',')
print(f'Nombre: {nombre.strip()}, Apellido: {apellido.strip()}')