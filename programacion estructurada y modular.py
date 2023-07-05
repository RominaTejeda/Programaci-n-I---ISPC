'''1)Realice un programa que muestre el mensaje “Hola Aula X (Indicar el número de aula a la que pertenecen),
 ¿Qué tal?” en tres veces intercambiados entre ellos otro mensajes a su elección.'''

def mensajes_aula(mensaje):
    print(mensaje)
    respuesta = input("Ingresa tu respuesta: ")
    return respuesta

# Mensaje inicial
numero_aula = input("Ingresa el número de aula: ")
mensaje_inicial = f"Hola Aula {numero_aula}, ¿Qué tal?"
respuesta_inicial = mensajes_aula(mensaje_inicial)

# Segundo mensaje
mensaje_segundo = "¡Bienvenidos! ¿Estan listos para comenzar la clase?"
respuesta_segundo = mensajes_aula(mensaje_segundo)

# Tercer mensaje
mensaje_tercero = "¿leyeron el material indicado la clase anterior?"
respuesta_tercero = mensajes_aula(mensaje_tercero)

# Respuestas
print("Respuesta al mensaje inicial:", respuesta_inicial)
print("Respuesta al segundo mensaje:", respuesta_segundo)
print("Respuesta al tercer mensaje:", respuesta_tercero)

mensajes_aula()

'''2) A partir del siguiente ejemplo “Hola Ana, ¿Qué tal?” realizar el programa la ejecución del mismo 
con al menos otros dos nombres más, es decir, tres mensajes con tres nombres distintos. Recuerda: en estos ejercicios trabajamos argumentos.'''

def saludar(nombre):
    mensaje = f"Hola {nombre}, ¿Qué tal?"
    print(mensaje)

nombres = ["Ana", "Franco", "Paola"]

for nombre in nombres:
    saludar(nombre)

'''3)Realizar un programa de funciones que contengan 3 parámetros, el cual derive en una suma. Mostrar el resultado dos veces.'''

def sumar(a, b , c):
    resultado = a + b + c
    return resultado
resulado_suma = sumar(4, 5, 6)
print(resulado_suma)
resulado_suma = sumar(6, 5, 9)
print(resulado_suma)

'''4)Realice un programa que lea dos números (dos parámetros), 
compare si son IGUALES, en ese caso, mostrar un mensaje que muestre TRUE.'''

def comparacion():
   a = input('Ingrese un número:')
   b = input('Ingrese un segundo número:')
   if a==b :
      print('TRUE')
   else:
      print('FALSE')  
comparacion()

'''5)Realice un programa que contenga una función que se llame “sumayresta”,
 que la misma contenga dos variables locales nombradas suma y resta, respectivamente.
   Recuerda: en estos ejercicios trabajamos argumentos para este ejercicio sería dos.'''

def sumayresta(a,b):
    suma = a + b
    print(suma)
    resta = a - b
    print(resta)
sumayresta(10,3)