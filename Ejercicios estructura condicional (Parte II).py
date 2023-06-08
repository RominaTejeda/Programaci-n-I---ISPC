# 1 - Introducir los lados de un triangulo y visualizar por pantalla si dicho triangulo es equilatero, isosceles o escaleno.

a = input('Ingrese medida del 1° lado del triángulo ')
b = input('Ingrese medida del 2° lado del triángulo ')
c = input('Ingrese medida del 3° lado del triángulo ')

if a == b == c :
   print ('El triángulo es Equilatero')
elif a == b != c or a == c != b or b == c != a:
   print ('El triánglo es Isosceles')
elif a != b != c :
   print ('El triángulo es Escaleno')

# 2 - Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago.

importe = float(input('Ingrese el importe a abonar: '))
forma_de_pago = input('Eliga la opcionde pago:\n'
                            '1 - Contado\n'
                            '2 - Tarjeta\n'
                            '3 - Débito\n')
if forma_de_pago == '1':
   porcentaje_contado = importe * 0.10
   print ('El monto a abonar es:', importe - porcentaje_contado)
elif forma_de_pago == '2':
   porcentaje_tarjeta = importe * 0.10
   print ('El monto a abonar es:', importe + porcentaje_tarjeta)
elif forma_de_pago == '3':
   porcentaje_debito = importe * 0.05
   print ('El monto a abonar es:', importe - porcentaje_debito)
   
#Realice un progra ma que lea tres numero, indique cual es mayor y determine si es par o impar

num_1=int(input('Ingrese el primer número: '))  

num_2=int(input('Ingrese el segundo número: ')) 

num_3=int(input('Ingrese el tercer número: '))  

if num_1 > num_2 and  num_1 > num_3:
   if num_1 % 2 == 0:
      print('El numero (',num_1,') es el mayor y es par.')
   else:
      print('El numero (', num_1,') es el mayor y es impar.')   
elif num_2 > num_1 and num_2 > num_3:
   if num_2 % 2 == 0:
      print('El numero (',num_2,') es el mayor y es par.')
   else:
      print('El numero (', num_2,') es el mayor y es impar.')  
elif num_3 > num_1 and num_3 > num_2:
   if num_3 % 2 == 0:
      print('El numero (',num_3,',) es el mayor y es par.')
   else:
      print('El numero (', num_3,') es el mayor y es impar.')  

# 4 Confeccione un programa que pida un numero del 1 al 7 y diga el dia de la semana que corresponde

num_semana = int ( input('Ingrese un número del 1 al 7: '))
if num_semana == 1:
   print('El numero seleccionado (',num_semana,') corresponde al dia Lunes de la semana.')
elif num_semana == 2:
   print('El numero seleccionado (',num_semana,') corresponde al dia Martes de la semana.')
elif num_semana == 3:
   print('El numero seleccionado (',num_semana,') corresponde al dia Miércoles de la semana.')
elif num_semana == 4:
   print('El numero seleccionado (',num_semana,') corresponde al dia Jueves de la semana.')
elif num_semana == 5:
   print('El numero seleccionado (',num_semana,') corresponde al dia Viernes de la semana.')
elif num_semana == 6:
   print('El numero seleccionado (',num_semana,') corresponde al dia Sábado de la semana.')
elif num_semana == 7:
   print('El numero seleccionado (',num_semana,') corresponde al dia Domingo de la semana.')
else:
   print('El carácter ingresado es incorrecto, por favor ingrese otro número.')   

# 5 Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.

num_mes = int(input('Elija un número del 1 al 12: '))  
if num_mes == 1:
   print('El N°',num_mes,' corresponde al mes de Enero.') 
elif num_mes == 2:
   print('El N°',num_mes,' corresponde al mes de Febrero.') 
elif num_mes == 3:
   print('El N°',num_mes,' corresponde al mes de Marzo.') 
elif num_mes == 4:
   print('El N°',num_mes,' corresponde al mes de Abril.') 
elif num_mes == 5:
   print('El N°',num_mes,' corresponde al mes de Mayo.') 
elif num_mes == 6:
   print('El N°',num_mes,' corresponde al mes de Junio.')
elif num_mes == 7:
   print('El N°',num_mes,' corresponde al mes de Julio.')    
elif num_mes == 8:
   print('El N°',num_mes,' corresponde al mes de Agosto.') 
elif num_mes == 9:
   print('El N°',num_mes,' corresponde al mes de Septiembre.')   
elif num_mes == 10:
   print('El N°',num_mes,' corresponde al mes de Octubre.')
elif num_mes == 11:
   print('El N°',num_mes,' corresponde al mes de Noviembre.') 
elif num_mes == 12:
   print('El N°',num_mes,' corresponde al mes de Diciembre.')   