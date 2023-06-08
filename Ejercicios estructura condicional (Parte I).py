# 1 Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no, mostrando un mensaje.

letra_1=input('Ingese una letra ')
letra_2=input('Ingrese otra letra ')
if letra_1==letra_2:
   print("Las letras son iguales")
else:
   print("las letras son distintas")
   
# 2 Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostras mensaje en pantalla.   

palabra_1=input('Escriba una palabra ')
palabra_2=input('Escriba otra palabra ')
if palabra_1 == palabra_2:
   print('Las palabras son iguales')
else:
   print('Las palabras son distintas')

# 3 realizar un programa que permita ingresar"f" o "m" y determinar si vota en mesa femenina o masculina.

genero=input('Ingrese "F" para femenino o "M" para masculino ')
if genero=='F':
   print('Vota en mesa femenina')
else:
   print('Vota en mesa masculina')

# 4 Realice un programa que lea dos numeros y diga cual es mayor

num_uno=input('Ingrese un numero ')
num_dos=input('Ingrese otro numero ')
if num_uno < num_dos:
   print('El segundo numero es mayor')
elif num_uno > num_dos :
   print('El primer numero es mayor')
elif num_uno == num_dos:
   print('Los numeros son iguales')

# 5 Realice un programa que cambie de peso a dolares. Mejorelo, añadiendo el cambio de dolares a pesos y que sea el usuario quien decida que tipo de cambio quiere, si de dolares a pesos o vicersa

cantidad = float(input('Ingresen la cantidad a convertir: '))
valor_dolar= float(input('Ingrese valor del dolar hoy: '))
tipo_cambio= input('Elija la transaccion que desea realizar:\n'
                   '1 - Convertir Pesos Arg. a Dolares\n'
                   '2 - Cambiar Dolares a Pesos Arg.\n')
if tipo_cambio == '1':
   print('El monto equivale a', cantidad/valor_dolar, 'Dolares')
elif tipo_cambio == '2':
   print('El monto equivale a', cantidad*valor_dolar,'pesos')
 
# 6 Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje diciendo "puede votar", sino "no votar".

edad = input('Ingrese su edad: ')
if edad >= '16':
   print('Puede votar')
else:
   print('No puede votar')
   
   

