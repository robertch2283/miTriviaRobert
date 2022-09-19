import random #Import libreria random
import time
puntaje=random.randint(0,11) #implementamos puntaje

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print("Bienvenido a mi trivia sobre futbol \n ")
nombre = input("Ingresa tu nombre: ")
print("\n Hola", nombre,"! \n  ¿Estas listo para refrescar la memoria con el deporte rey? \n")

print("\n comenzaras con: ",puntaje,"puntos")

# Es importante dar instrucciones sobre cómo jugar:
print("Responder las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta:\n")
# Primera pregunta
print("\n 2) ¿En que año Argentina campeonó la copa América?")
print("Estoy seguro que te acuerdas!")
time.sleep(1)
print("Si no te acuerdas bien, aqui te muestro las     alternativas!")
time.sleep(1)
print("a) 2019")
print("b) 2020")
print("c) 2018")
print("d) 2021")
respuesta_1 = input("\nTu respuesta: ")

while respuesta_1 not in ("a","b","c","d"):
  respuesta_1 = input("Debes responder a,b,c,d ;Ingresa nuevamente tu respuesta: ")
if respuesta_1=="z":
    print("Esto es un mensaje secreto")
if respuesta_1 == "a":
  puntaje=puntaje-5
  print("Incorrecto", nombre, "! Argetina salió campeón el año 2021 ")
elif respuesta_1 == "b":
  puntaje=puntaje+5
  print("Incorrecto", nombre, "! Argetina salió campeón el año 2021 ")
elif respuesta_1 == "c":
  print("Incorrecto", nombre, "! Argetina salió campeón el año 2021 ")
  puntaje=puntaje/2
else:
  puntaje=puntaje*2
  print("Muy bien", nombre, "! respuesta correcta")
  print(RED+nombre, "llevas", puntaje, "puntos"+RESET)

  print("Nos vemos en 3 segundos, tomate un respiro")
  time.sleep(3)
  print("Continuemos!")
# Segunda pregunta
print("\n2) ¿Quien es el máximo goleador de la copa     del mundo? \n")
print("Estoy seguro que te acuerdas!.. aver             piensalo")
time.sleep(5)
print("Si no te acuerdas bien, aqui te muestro las     alternativas!")
time.sleep(3)
print("a) Ronaldo Nazario")
print("b) Cristiano Ronaldo")
print("c) Miroslav Klose")
print("d) Pelé")

respuesta_2 = input("\nTu respuesta: ")
while respuesta_2 not in ("a","b","c","d"):
  respuesta_2 = input("Debes responder a,b,c,d ;Ingresa nuevamente tu respuesta: ")
  if respuesta_2=="z":
    print("Esto es un mensaje secreto")
if respuesta_2 == "a":
    puntaje=puntaje+5
    print("Incorrecto", nombre, "! el goleador actual es Miroslav Klose ")
elif respuesta_2 == "b":
    puntaje=puntaje/2
    print("Incorrecto", nombre, "! el goleador actual es Miroslav Klose")
elif respuesta_2 == "d":
    puntaje=puntaje-5
    print("Incorrecto", nombre, "! el goleador actual es Miroslav Klose")
else:
    puntaje=puntaje*2
    print("Muy bien", nombre, "! respuesta correcta")
print(GREEN+nombre, "llevas", puntaje, "puntos"+RESET)
# tercera pregunta
print("\n3) ¿Quién es el actual campeón del mundo en futbol?  \n")

print("a) Brasil")
print("b) Alemania")
print("c) Croacia")
print("d) Francia")

respuesta_3 = input("\nTu respuesta: ")
while respuesta_3 not in ("a","b","c","d"):
  respuesta_3 = input("Debes responder a,b,c,d ;Ingresa nuevamente tu respuesta: ")
  if respuesta_3=="z":
    print("Esto es un mensaje secreto")
if respuesta_3 == "a":
    puntaje=puntaje/2
    print("Incorrecto", nombre, "! Francia es el actual campéon del mundo ")
elif respuesta_3 == "b":
    puntaje=puntaje-5
    print("Incorrecto", nombre, "! Francia es el actual campéon del mundo ")
elif respuesta_3 == "c":
    puntaje=puntaje+5
    print("Incorrecto", nombre, "! Francia es el actual campéon del mundo ")
else:
    puntaje=puntaje*2
    print("Muy bien", nombre, "! respuesta correcta")

print (MAGENTA+"Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos")