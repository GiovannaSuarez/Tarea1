import math

# Ejercicio 1
print("Ingrese la cantidad de años que tiene su computadora")
edad = float(input())
if edad <= 2:
  print("Su computadora es nueva")
else:
  print("Su computadora es vieja")
  print("")
  
# Ejercicio 2
print("Ingrese un numero")
num = float(input())
if num <= 0:
  print("Error: El numero ingresado es negativo o 0")
print("")

# Ejercicio 3
print("Ingrese el primer nombre:")
nombre1=(input())
print("Ingrese el segundo nombre:")
nombre2=input()
if nombre1["0"] == nombre2["0"]:
    print("Coincidencia")
else:
    print("No hay coincidencia")
print("")

# Ejercicio 4
print("¿A cual candidato quiere votar?")
print("[A]Partido rojo")
print("[B]Partido verdad")
print("[C]Partido azul")
rep = (str(input())).upper()
if rep == "A":
  print("Gracias por votar al partido rojo")
elif rep == "B":
  print("Gracias por votar al partido verdad")
elif rep == "C":
  print("Gracais por votar al partido azul")
else:
  print("Error:No ingreso una letra valida (", rep, ")")    
print("")

# Ejercicio 5
#Pedimos al usuario una letra, validamos que no sea más de un caracter y verificamos que sea una vocal.
letra=str(input("Ingrese una letra: ")).lower()
long=len(letra)
if long > 1:
    print("No se puede procesar su dato.")
elif letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("La letra ingresada es una vocal")
else:
    print("La letra ingresada NO es una vocal")
print("")

# Ejercicio 6 
year = int(input("Ingrese un año para saber si es biciesto o no: "))
if year%4==0 and year%100!=0:
    print(f"El año {year} es biciesto.")
elif year%4==0 and year%100==0 and year%400==0:
    print(f"El año {year} es biciesto.")
else:
    print(f"El año {year} no es biciesto")
print("")

# Ejercicio 7
print("Ingrese el primer numero")
num1 = float(input())
print("Ingrese el segundo numero")
num2 = float(input())
print("Ingrese el tercer numero")
num3 = float(input())
if num1 > num2:
  if num1 > num3:
    print(num1, " es el numero mas grande")
  else:
    print(num3, " es el numero mas grande")
else:
  if num2 > num3:
    print(num2, " es el numero mas grande")
  else:
    print(num3, " es el numero mas grande")
print("")

# Ejercicio 8
print("Ingrese el usuario: ")
usuario=input()
print("Ingrese la contraseña: ")
contraseña=input()
if usuario== "gwenevere" and contraseña=="excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
   print("Acceso denegado")
print("")
   
# Ejercicio 9
print("Ingrese su nombre: ")
nombre=input()
print("Ingrese su edad y sexo con el siguiente formato:  edad, s")
edads=input()
edad=(edads[0:edads.find(",")])
s=(edads[edads.find(",")+1:])
antm="abcdefghijkm"
postm="nlopqrstuvwxyz"
primerl=nombre[0]
if (s=="f" and primerl in antm):
    print("Estas en el grupo A")
elif (s=="m" and primerl in postm): 
    print("Estas en el grupo A")
else:
    print("Estas en el grupo B")
print("")

# Ejercicio 10
edad = int(input("Ingrese su edad: "))
if edad<=0:
    print(f"La edad ingresada ({edad}) no es correcta")
elif edad<4:
    print("Precio de la entrada: GRATIS")
elif edad<=18:
    print("Precio de la entrada: $500")
elif edad>18:
    print("Precio de la entrada: $1000")
print("")

# Ejercicio 11
print("¡Bienvenido a la pizzeria Napoli!")
print("¿Que tipo de pizza le gustaria pedir?")
print("[1].Pizza vegetariana")
print("[2].Pizza no vegetariana")
rep = int(input())
veg = 1
pizza_final = "No definido"
if rep == 1:
  print("Usted eligio pizza vegetariana")
  print("Elija uno de los siguientes ingredientes para agregar")
  print("[1].Pimiento")
  print("[2].Tofu")
  rep = int(input())
  veg = 0
elif rep == 2:
  print("Usted eligio pizza no vegetariana")
  print("Elija uno de los siguientes ingredientes para agregar")
  print("[1].Peperoni")
  print("[2].Jamon")
  print("[3].Salmon")
  rep = int(input())
  veg = 1
else:
  print("Error: El numero ingresado no es valido")
if veg == 0:
  if rep == 1:
    pizza_final = "Mozzarela,Tomate,Pimiento"
  elif rep == 2:
    pizza_final = "Mozzarela,Tomate,Tofu"
if veg == 1:
  if rep == 1:
    pizza_final = "Mozzarela,Tomate,Peperoni"
  elif rep == 2:
    pizza_final = "Mozzarela,Tomate,Jamon"
  elif rep == 3:
    pizza_final = "Mozzarela,Tomate,Salmon"
print("Los ingredientes de su pizza son:", pizza_final)
print("¡Gracias por usar Pizza Napoli!")
print("")

# Ejercicio 12	
año_act=int(input("Ingrese el año actual: "))
año_x=int(input("Ingrese cualquier otro año: "))
print("")
if año_act > año_x:
  años_pasados= (año_act - año_x)
  print("Pasaron ", años_pasados, "años desde", año_x)
elif año_act < año_x:
  años_faltantes= (año_x - año_act)
  print("Faltan ", años_faltantes, "años para", año_act)
print("")

# Ejercicio 13
a=int(input("Ingrese un número: "))
b=int(input("Ingrese un segundo número: "))
if a>0 and b>0: 
    if a<b and b%a==0:
        print(f"{b} es múltiplo de {a}.")
    elif b<a and a%b==0:
        print(f"{a} es múltiplo de {b}.")
    else:
        print("Ninguno es múltiplo del otro.")
else:
    print("Los números ingresados son nulos o negativos.")
print("")

# Ejercicio 14
print("Ingrese los coeficientes de la recta, en orden (a*x + b = 0)")
a=int(input("Ingrese a: "))
b=int(input("Ingrese b: "))
if a==0 and b==0:
    print("La solución son todos los reales.")
elif a==0:
    print("La ecuación no tiene solución.")
else:
    x=(-b/a)
    print("La solucion es", x)
print("")

# Ejercicio 15
print("~ ÁREAS ~")
print("¿Que área desea calcular? Seleccione una opción:")
letra=str(input("T = área del triángulo  //  C = área del círculo")).upper()
if letra == "T":
    bas=float(input("Ingrese la base del triangulo: "))
    alt=float(input("Ingrese la altura del triangulo: "))
    areaT= (bas*alt)/2
    print("El área de su triángulo es: ", areaT)
elif letra == "C":
    rad=float(input("Ingrese el radio del circulo: "))
    x=math.pi/2
    areaC= x*(rad^2)
    print("El área de su círculo es: ", areaC)
else:
    print("La letra ingresada no es correcta")
print("")

# Ejercicio 16
print("Ingrese dos números, 'a' y 'b' y la operación a realizar entre ellos, por ejemplo: 28 + 5")
print("(Las operaciones aceptadas son '+' suma; '-' resta; '*' multiplicación; '/' division)")
print("Ayuda: para decimales, use un punto '.' en lugar de la coma ','")
ayb = input(">>>>> ")
a = float(ayb[0:ayb.find(" ")])
b = float(ayb[ayb.find(" ")+3:])
operacion = ayb[ayb.find(" ")+1]
suma = a + b
resta = a - b
multip = a * b
div = a / b
if operacion=='+' or operacion=='-' or operacion=='*' or operacion=='/':
    if operacion=='+':
        print(f"La suma {a} + {b} da {suma}.")
    elif operacion=='-':
        print(f"La resta {a} - {b} da {resta}.")
    elif operacion=='*':
        print(f"La suma de {a} * {b} da {multip}.")
    elif operacion=='/':
        if b!=0:
            print(f"La división {a} / {b} da {div}.")
        else:
            print("La división por 0 no se puede realizar")
else:
  print("La operación ingresada no es válida.")
print("")

# Ejercicio 17
dia = input("Ingrese un día de la semana: ")
dia = dia.lower()
if dia!="lunes" and dia!="martes" and dia!="miercoles" and dia!="miércoles" and dia!="jueves" and dia!="viernes":
  print(f"ERROR: El día ingresado ({dia}) no corresponde a un día de la semana.")
else:
  if dia=="lunes":
    print("El día ingresado es", dia)
  elif dia=="martes":
    print("El día ingresado es", dia)
  elif dia=="miercoles" or dia=="miércoles":
    print("El día ingresado es", dia)
  elif dia=="jueves":
    print("El día ingresado es", dia)
  elif dia=="viernes":
    print("El día ingresado es", dia)
print("")

# Ejercicio 18
print("~ SALARIO ~")
CantHMes=float(input("¿Cuántas horas trabajo este mes?:"))
SalarioH=float(input("¿Cuánto recibe por hora trabajada?:"))
hMin=192
Salario= CantHMes*SalarioH
if CantHMes > 192:
    hExtra= CantHMes - 192
    print("Usted trabajo:",hExtra, "horas extra")
    SalarioT= (Salario + (hExtra*0.1))
    print(f"Su salario total (con la bonificación por las horas extras) es: ${SalarioT}")
else:
    print("Usted no ha trabajado horas extras este mes.")
    print(f"Su salario total (sin bonificación) es: ${Salario}")
print("")

# Ejercicio 19
lapiz = int(input("Ingrese la cantidad de lápices a comprar: "))
precio_unitario = 60
if lapiz<1000:
  precio_final = lapiz * precio_unitario
  print(f"El precio total a pagar es de ${precio_final}")
elif lapiz>=1000:
  precio_final = (lapiz * precio_unitario) * 0.93
  print(f"El precio total a pagar es de ${precio_final}, quedando en {round((60*0.93),2)} c/lapiz")
  print("")

# Ejercicio 20
print("ingrese a continuación sus 4 notas de a una.")
n1 = int(input("Nota 1: "))
n2 = int(input("Nota 2: "))
n3 = int(input("Nota 3: "))
n4 = int(input("Nota 4: "))
prom = (n1 + n2 + n3 + n4)/ 4
if n1<0 or n1>10 or n2<0 or n2>10 or n3<0 or n3>10 or n4<0 or n4>10:
  print(f"Las notas ingresadas no son correctas.")
else:
  if prom >= 6:
    print(f"El promedio de sus notas es de {prom}, por lo tanto SI APRUEBA.")
  else:
    print(f"El promedio de sus notas es de {prom}, por lo tanto NO APRUEBA.")
