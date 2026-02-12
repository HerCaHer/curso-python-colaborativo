# Como aprendimos en el capítulo Variables de Python, no podemos combinar cadenas y números de esta manera:
age = 36
txt = "My name is John, I am " , age
print(txt)

'''
Cuerdas F
F-String se introdujo en Python 3.6 y ahora es la forma preferida de formatear cadenas.
Para especificar una cadena como una f-string, simplemente coloque un fdelante del literal de cadena y agregue llaves {}como marcadores de posición para variables y otras operaciones.
'''
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Agregue un marcador de posición para la pricevariable:
price = 59
txt = f"The price is {price} dollars"
print(txt)


# Mostrar el precio con 2 decimales:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Realice una operación matemática en el marcador de posición y devuelva el resultado:
txt = f"The price is {20 * 59} dollars"
print(txt)