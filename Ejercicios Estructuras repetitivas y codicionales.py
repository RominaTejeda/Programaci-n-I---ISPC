# 1 Realice un programa que lea 4 numeros y diga cuatos son pares y cuantos impares y devuelva la sumatoria de los pares.

num_pares = 0
num_impares = 0
acum_par = 0
acum_impar = 0
cont = 0

while cont < 4:
    numero=int(input('Ingrese un número: '))
    if numero % 2 == 0 :
       acum_par = acum_par + numero
       num_pares +=1
    else:
        acum_impar = acum_impar + numero
        num_impares +=1
    cont +=1            

print('Se han ingreso {} números pares y {} números impares. La suma de los pares {} y la de los impares es {}'.format(num_pares, num_impares, acum_par, acum_impar))

# 2 Leer 10 numeros y obtener la cantidad de mayores y la cantidad e menores a 100, cual es el num max y el num Min

mayores_100 = 0
menores_100 = 0
num_max = float('-inf')
num_min = float('inf')

for i in range(10):
    num = float(input("Ingrese un número: "))
    
    if num > num_max:
        num_max = num
    
    if num < num_min:
        num_min = num
    
    if num > 100:
        mayores_100 += 1
    elif num < 100:
        menores_100 += 1

print("Cantidad de números mayores a 100:", mayores_100)
print("Cantidad de números menores a 100:", menores_100)
print("Número máximo:", num_max)
print("Número mínimo:", num_min)  

# 3 Ingrese las edades de 15 personas y determinar cuantas mujeres, cuantos varones, cuantos mayores de edad y cuantos menores de edad

mujeres = 0
varones = 0
mayores_de_edad = 0
menores_de_edad = 0

for i in range(5):
    print(f"Persona {i+1}:")
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (f) femenino / (m) masculino: ").lower()
    
    if sexo == "f":
        mujeres += 1
    elif sexo == "m":
        varones += 1
    if edad >= 18:
        mayores_de_edad += 1
    else:
        menores_de_edad += 1

print("Cantidad de mujeres:", mujeres)
print("Cantidad de varones:", varones)
print("Cantidad de mayores de edad:", mayores_de_edad)
print("Cantidad de menores de edad:", menores_de_edad)

#4 Leer 10 números y mostrar solamente los números positivos, y su sumatoria
sumatoria = 0

for i in range(10):
    numero = float(input("Ingrese un número: "))
    
    if numero > 0:
        print(numero)
        sumatoria += numero
print("La sumatoria de los números positivos es:", sumatoria)

#5 Leer 15 números negativos y conventirlos a positivos e imprimir dichos números.

for i in range(15):
    numero = float(input("Ingrese un número negativo: "))
    
    if numero < 0:
        numero = -numero
        print(numero)
        