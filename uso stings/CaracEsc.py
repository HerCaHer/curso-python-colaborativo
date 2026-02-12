txt = "We are the so-called \"Vikings\" from the north."

# Single Quote para prevenir que Python interprete caracteres especiales:
txt = 'It\'s alright.'
print(txt) 

# Ejemplos para backslash de caracteres de escape en Python
txt = "This will insert one \\ (backslash)."
print(txt) 

# Ejemplo de saltos de línea 
txt = "Hello\nWorld!"
print(txt) 

# Ejemplo de retorno de carro
txt = "Hello\rWorld!"
print(txt) 

# Ejemplo de tabulación
txt = "Hello\tWorld!"
print(txt) 

# Ejemplo de retroceso
txt = "Hello \bWorld!"
print(txt) 


# Una barra invertida seguida de tres números enteros dará como resultado un valor octal:
txt = "\110\145\154\154\157"
print(txt) 

# Una barra invertida seguida de una 'x' y un número hexadecimal representa un valor hexadecimal:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

# Cadenas crudas
txt = r"c:\newfolder\test.txt"
print(txt)