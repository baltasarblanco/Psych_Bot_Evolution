#DESAFIO 3: Simular que recibo un log de error de un servidor y
#y tengo que extraer la info. clave automaticamente


#input: registro = "///ERROR_CODE: 503_Server-Down///"

#mi MISION - OUTPUT: Reescribir un script que transforme
#la basura en este rporte limpio

registro = "///ERROR_CODE: 503_Server-Down///"
status = "SISTEMA DE ALERTA"

print (status)
print (registro[3:29])