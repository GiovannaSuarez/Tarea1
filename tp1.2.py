# TRABAJO PRÁCTICO 1.2   
# 
# EJERCICIO 1 
base = float(input("Ingrese la base del triángulo:"))
altura = float(input("Ingrese la altura:"))
area = (base * altura) / 2
lado1 = float(input("Ingrese el valor del primer lado:"))
lado2 = float(input("Ingrese el valor del segundo lado:"))
lado3 = float(input("Ingrese el valor del tercer lado:"))
perimetro=print("El perímetro del triangulo es: ",(lado1+lado2+lado3))
print("El área del triangulo es: ",area)
print(" ")

# EJERCICIO 2
print("Dé las longitudes de los catetos")
cat1 = float(input("Cateto 1:"))
cat2 = float(input("Cateto 2:"))
hipot = (cat1**2 + cat2**2)**(1/2)
print("La hipotenusa de dicho triángulo mide", hipot)
print(" ")

# EJERCICIO 3
num1= float(input("Ingrese un número: "))
num2= float(input("Ingrese otro número: "))
sum= num1+num2
rest= num1-num2
multp= num1*num2
div= num1/num2
print("Segun los números ingresados:")
print("Suma:",sum, "\nResta:",rest, "\nMultiplicación:",multp,"\nDivision:",div)
print(" ")

# EJERCICIO 4
grados_f=float(input("Ingrese grados Fahrenheit: "))
grados_c=((grados_f-32)*5/9)
print(grados_f," equivalen a ",grados_c," grados celcius.")
print(" ")

# EJERCICIO 5
#¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?

#a) A = input(nombre, “¿Cuál es tu canción favorita?”)
# No se puede poner una variable dentro de un input.
A = (input("¿Cual es tu canción favorita? "))

#b)	precio = input(“Precio: “)
#   total = precio + (precio * 0.1)
# Falta poner que tipo de variable esta pidiendo, en la entrada de datos de precio; porque sino se toma como string y entonces no se puede hacer la cuenta de la linea siguiente.
precio = float(input("Precio: "))
total = precio + (precio*0.1)

#c)	edad = int(input(“Edad: “))
#   print(tu edad es, edad)
#El texto "tu edad es" no está entre comillas, entonces no se va a mostrar el mensaje final por pantalla.
edad = int(input("Edad: "))
print("tu edad es", edad)

#d)	edad = int(input(“Edad: “))
#   print(“Veamos si tu edad es 18…”, edad=18)
#En el print, la variable edad no esta siendo reasignada. Lo correcto sería colocar el signo(==), para que así se comparen los valores y obtengamos una respuesta logica.
edad = int(input("Edad: "))
print("Veamos si tu edad es 18…", edad==18)
print(" ")

# EJERCICIO 6
print("Ingrese el primer numero: ")
num1=float(input())
print("Ingrese el segundo numero: ")
num2=float(input())
print("Ingrese el tercer numero: ")
num3=float(input())
promedio=(num1+num2+num3)/3
print("El promedio de los numeros dados es:", promedio)
print(" ")

# EJERCICIO 7
print("Ingrese la cantidad de minutos que desee: ")
minutos=int(input())
horas=int(minutos/60)
print(minutos," equivalen a ",horas," horas y ",minutos-(horas*60)," minutos.")
print(" ")

# EJERCICIO 8
sueldo_base = float(input("Ingrese su sueldo base: "))
comision = 0.10
venta1 = float(input("Ingrese el monto de la primer venta: "))
venta2 = float(input("Ingrese el monto de la segunda venta: "))
venta3 = float(input("Ingrese el monto de la tercera venta: "))
sueldo_final = str(sueldo_base + comision*venta1 + comision*venta2 + comision*venta3)
print(f'Su sueldo final será de {sueldo_final}')
print(" ")

# EJERCICIO 9
precio_total = float(input("Ingrese el precio neto: "))
print("El precio con descuento del 15 por ciento es de: $", precio_total*0.85)
print(" ")

# EJERCICIO 10
parcial1 = float(input("Ingrese la nota del parcial 1: "))
parcial2 = float(input("Ingrese la nota del parcial 2: "))
parcial3 = float(input("Ingrese la nota del parcial 3: "))
prom_parciales = ((parcial1 + parcial2 + parcial3 ) / 3) * 0.55
final = float(input("Ingrese la nota del Final:"))
final = final * 0.30
trabajo_final = float(input("Ingrese la nota del TP Final: "))
trabajo_final = trabajo_final * 0.15
nota_final = prom_parciales + final + trabajo_final
print("La nota final de la materia es de:", nota_final)
print(" ")

# EJERCICIO 11
x1 = float(input("Ingrese un número: "))
x2 = float(input("Ingrese otro número: "))
distancia = abs(x1 - x2)
print("La distancia entre dichos números es de:", distancia)
print(" ")

# EJERCICIO 12
numero = float(input("Ingrese un número: "))
print("La raiz cuadrada del n° es:", numero**(1/2), " y la raiz cúbica es:", numero**(1/3))
print(" ")

# EJERCICIO 13
num = int(input("Ingrese un número entero de dos cifras: "))
lista = str(num)
print(lista[::-1])
print(" ")

# EJERCICIO 14
A = int(input("Ingrese un número A : "))
B = int(input("Ingrese otro número B : "))
C = A
A = B
B = C
print("El valor invertido de las variables ingresadas son:\nA:",A, "\nB:",B )
print(" ")

# EJERCICIO 15
HH = int(input("Ingrese la hora de salida: "))
MM = int(input("Minutos: "))
SS = int(input("Segundos: "))
hh = int(input("Ingrese la duración del viaje en horas: "))
mm = int(input("Minutos: "))
ss = int(input("Segundos: "))
dif_s = int((ss+SS)/60)
dif_m = int((mm+MM)/60)
dif_h = int((hh+HH)/60)
seg_f = ss + SS - dif_s * 60
min_f = mm + MM + dif_s - dif_m * 60
h_f = hh + HH + dif_m - dif_h * 60
print(f"Usted salió a las {HH}:{MM}:{SS}hs y llegará a las {h_f}:{min_f}:{seg_f}hs")
print(" ")

# EJERCICIO 16
nombre = (input("Ingrese su Nombre: "))
apellido1 = (input("Ingrese su primer apellido: "))
apellido2 = (input("Ingrese su segundo apellido: "))
print("Las iniciales de el nombre y los apellidos ingresados son:")
print("Nombre: ",nombre[0].upper(), "\nApellido1: ",apellido1[0].upper(), "\nApellido2: ",apellido2[0].upper())
print(" ")

# EJERCICIO 17
usuario = input("Ingrese su nombre: ")
print(f"Ahora estas en la matrix, {usuario}.")
print(" ")

# EJERCICIO 18
comanda = float(input("Ingrese el valor de la comida: "))
servicio = comanda * 0.062
propina = comanda * 0.1
print(end= "Valor de la comida: $")
print(comanda)
print(end= "Costo del servicio: $")
print(servicio)
print(end= "Propina: $")
print(propina)
print(end= "Precio final: $")
print(comanda + servicio + propina)
print(" ")

# EJERCICIO 19
print("Ingrese el numero del dia:")
dia=int(input())
print("Ingrese el numero del mes:")
mes=int(input())
print("Ingrese el año:")
año=int(input())
print("La fecha de hoy es: ", dia,"/",mes,"/",año)
print(" ")

# EJERCICIO 20
print("Ingrese el numero del dia:")
temp=int(input())
if temp<10:
 fecha="0"+str(temp)
else:
 fecha=str(temp) 
print("Ingrese el numero del mes:")
temp=int(input())
if temp<10:
 fecha=fecha+"0"+str(temp)
else:
 fecha=fecha+str(temp) 
print("Ingrese el año")
temp=int(input())
if temp<10:
 fecha=fecha+"0"+str(temp)
else:
 fecha=fecha+str(temp) 
print("La fecha es:",fecha)
print(" ")

# EJERCICIO 21
consumo = float(input("Ingrese la cantidad recorrida promedio con 1l de combustible: "))
tanque = float(input("Ingrese la capacidad del tanque: "))
recorrido = float(input("Ingrese cuántos kilómetros va a recorrer: "))
num_final = (recorrido / consumo) / tanque
print(f"En total va a necesitar {num_final} tanques de combustible para realizar el viaje.")