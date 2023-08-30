#EJERCICIO 15
# #Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo.
# Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. 
# Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.

import math
print("Si desea calcular el área de un TRIÁNGULO, ingrese la letra t")
print("Si desea calcular el área de un CÍRCULO, ingrese la letra C")
calcular=input().lower()
if calcular=="c":
    print("Ingrese la base: ")
    base=int(input())
    print("Ingrese la altura: ")
    altura=int(input())
    print("El área del triangulo es: ",(base*altura)/2)
else:
    calcular=="t"
    print("Ingrese el radio: ")
    radio=int(input())
    print("El área del círculo es: ",math.pi*radio**2)
    
    
#EJERCICIO 18
#Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
#La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
#Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes.
   
print("Ingrese cuántas horas ha trabajado este mes: ")
horastrab=float(input())
print("Ingrese su salario por hora: ")
salhora=float(input())
if horastrab==48:
    salario=horastrab*salhora
    print ("Usted ha trabajado el mínimo de horas, su salario de este mes es : $",salario)   
else:
    horastrab>48
    horasextra=horastrab-48
    salario=((horastrab-horasextra)*salhora)+horasextra*(salhora+(salhora*10/100))    
    print(f"Usted hizo {horasextra} horas extra. Su salario total es: ${salario}")
    
#EJERCICIO 20
#Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.
print("Ingrese las 4 notas del alumno, de una y apretando enter despues de ingresar cada una")    
n1=float(input())
n2=float(input())
n3=float(input())
n4=float(input())
promedio=(n1+n2+n3+n4)/4
if promedio>= 6:
    print(f"El alumno está APROBADO. Su promedio es: {promedio}")
else:
    print(f"El alumno está DESAPROBADO. Su promedio es: {promedio}")    



