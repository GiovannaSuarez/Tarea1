import TP5_Funciones
import math
#1----------------------------------------------------------------------------------------
# 	Escribir una función que, dado un número de DNI, retorne True si el número es válido y
#False si no lo es. Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.

rep = int(input("Ingresa un numero de dni y comprobare si es valido  "))
rep = TP5_Funciones.dni_cheker(rep)
if rep == True:
    print("El dni es valido")
else:
    print("El dni no es valido")
#2----------------------------------------------------------------------------------------
phrase = input("Ingrese una frase a continuación: ")
flipped_phrase_list = phrase[len(phrase)::-1]
print(f"La longitud de la última palabra es: {TP5_Funciones.last_word_len(flipped_phrase_list)}")
print("")

#3--------------------------------
# Escribir un programa que permita al usuario obtener un
# identificador para cada uno de los socios de un club.
# Para eso ingresará nombre completo y número de DNI de cada socio,
# indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.
#Precondición: el formato del nombre de los socios será: nombre apellido.
# Podría ingresarse más de un nombre, en cuyo caso será: nombre1, nombre2, apellido.
# Si un socio tuviera más de un apellido, el usuario solo ingresará uno.
#Se debe validar que el número de DNI tenga 7 u 8 dígitos.
# En caso contrario, el programa debe dejar al usuario en un bucle hasta que ingrese un DNI correcto.
#Por cada socio se debe imprimir su identificador único,
# el cual estará formado por: el primer nombre, la cantidad de letras del apellido y
# los 3 primeros dígitos de su DNI. Ejemplo:
#Nombre: María Ines Rosales
#DNI: 25469648
#ID -> Maria7254
username = ""
username1 = ""
username2 = ""
usersurename = ""
username = (str(
    input(
        "Ingrese el nombre y apellido con el formato \nSi es solo 1 nombre: nombre apellido \nSi son 2 nombres: nombre 1,nombre 2,apellido\n "
    ))).lower()
for i in range(0, len(username), 1):  #Separacion de datos de usuario
    if username[i] == " ":
        username1 = username[0:i]
        usersurename = username[i + 1:len(username)]
    elif username[i] == ",":
        for p in range(0, len(username) - 1, 1):
            if username[p] == ",":
                username1 = username[0:p]
                temp1 = p
                break
        for p in range(len(username) - 1, 0, -1):
            if username[p] == ",":
                usersurename = username[p + 1:len(username)]
                temp2 = p
                break
        username2 = username[temp1 + 1:temp2]
while True:  #Comprobacion de dni
    dni = int(input("Ingresa el dni del usuario  "))
    if TP5_Funciones.dni_cheker(dni) == True:
        break
    else:
        print("Dni no valido, intenten otra vez")
print(TP5_Funciones.id_maker(username1, usersurename, dni))
#4----------------------------------------------------------------------------------------
#4.	Crea un programa que pida dos número enteros 
# al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función que reciba los dos números, 
# y devuelve si el primero es múltiplo del segundo.
num=int(input("Ingrese el primer numero "))
num2=int(input("Ingrese el segundo numero "))
rep=TP5_Funciones.Multi_Checker(num,num2)
if rep==True:
    print(f"{num} es multiplo de {num2}")
else:
    print(f"{num} no es multiplo de {num2}")


#5----------------------------------------------------------------------------------------
day_num = int(input("Ingrese la cantidad de días a visualizar: "))
num = 1
while num<=day_num:
    min_temp = float(input("Ingrese la temperatura mínima: "))
    max_temp = float(input("Ingrese la temperatura máxima: "))
    print(f"La temperatura promedio del dia {num} es de:", TP5_Funciones.prom_temp(min_temp,max_temp))
    num = num + 1
print("")


#6----------------------------------------------------------------------------------------

message = str(input("Introduce una cadena:"))

print("La cadena con espaciado adicional: ",(TP5_Funciones.ExtraSpacing(message)))

print("")
#7----------------------------------------------------------------------------------------

numbers = []

for i in range(5):
	n = int(input("Ingrese un número: "))
	numbers.append(n)
vmax,vmin = (TP5_Funciones.CalculateMaxMin(numbers))
print("El valor máximo es ",vmax)
print("El valor mínimo es ",vmin)

print("")

#8----------------------------------------------------------------------------------------
# 	Diseñar una función que calcule el área y el perímetro de una circunferencia. 
# Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.

rad=input("Dame el radio de una circunferencia, mostrare el area y perimetro ")
TP5_Funciones.area_perimeter(rad)

#9----------------------------------------------------------------------------------------
# Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y 
# te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. 
# Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
#Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.

login_attempts=0

while True:
    if login_attempts>=3:
        print("Usted a exedido su limite de intentos")
        break
    else:
        username=input("Ingrese su nombre de usuario  ")
        password=str(input("Ingrese su contraseña  "))
        last=TP5_Funciones.login(username,password,login_attempts)
        login_attempts=last[1]
        if last[0]==True:
            print("Bievenido usuario")
            break
        else:
            print(f"Nombre de usuario o contraseña no validos, intentos restantes:{3-login_attempts}")
#10----------------------------------------------------------------------------------------



#11----------------------------------------------------------------------------------------
# Escribir una función que reciba otra función y una lista, 
# y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.   

lest=[12,10,19]
lest=TP5_Funciones.fuction_list(TP5_Funciones.double,lest)
print(lest)
#12----------------------------------------------------------------------------------------
#Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
print("Bienvenido/a")
phrase=input("Ingrese una frase: ")
print("Veamos la longitud de las palabras que la integran: ")
print(TP5_Funciones.phrase_dictionary(phrase))


#13----------------------------------------------------------------------------------------	
# Escribir una función que calcule el módulo de un vector.
print(TP5_Funciones.module((3, 4)))
print(TP5_Funciones.module((1, 2, 3)))
#14----------------------------------------------------------------------------------------
prime_number = int(input("Ingrese un número para ver si es primo o no: "))
prime = TP5_Funciones.prime_checker(prime_number)
if prime==True:
    print(f"El número {prime_number} es primo.")
elif prime==False:
    print(f"El número {prime_number} no es primo.")
print("")

#15----------------------------------------------------------------------------------------
print("Bienvenido/a")
print("Ingrese un número entero positivo para conocer su factorial   ")
number=int(input())
TP5_Funciones.funtion_factorial(number)

#16----------------------------------------------------------------------------------------
# Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número, 
# utilizando para ello una función que calcule la frecuencia.

num=int(input("Ingrese un numero  "))
while True:
    digit=int(input("Ingrese un digito  "))
    if len(str(digit))==1:
        break
    else:
        print("Error, lo ingresa es mas de un digito, intente denuevo")
print(f"La cantidad de veces que el digito {digit} se repite en {num} es: {TP5_Funciones.digit_counter(num,digit)}")
#17---------------------------------------------------------------------------------------- 
print("Ingrese números primos, o uno no primo para salir:")
prime_list = []
prime_number = True
biggest_number = 0
while True:
    num = int(input(">>> "))
    prime_number = TP5_Funciones.prime_checker(num)
    if prime_number==False:
        break
    else:
        if num>biggest_number:
            biggest_number = num
        temp = list(map(int, str(num)))
        prime_list.extend(temp)
        print(f"Suma de los dígitos de {num}: {TP5_Funciones.digit_counter2(num)}.")
digit = int(input("Ingrese un número para buscar cuántas veces aparece: "))
print(f"El número {digit} aparece {TP5_Funciones.frequency_digit_counter(prime_list,digit)} veces.")
print(f"El factorial del primo más grande ingresado ({biggest_number}) es {math.factorial(biggest_number)}.")