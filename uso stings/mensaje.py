import pywhatkit
import datetime

# Número de teléfono con código de país (ej. México +52)
numero = "+522411031471"

# Mensaje a enviar
mensaje = "No se te olviden mis impresiones qlo"

# Hora de envío
hora_envio = 21  # 10 PM en formato 24 horas
minuto_envio = 55  # Minuto exacto

# Programar mensaje
pywhatkit.sendwhatmsg(numero, mensaje, hora_envio, minuto_envio)
