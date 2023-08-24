#EJERCICIO EN CLASE 22/08

import math

print("Ingrese el dia de la semana, luego fecha")
print("Ejemplo: lunes,01/03")
fecha=input()
dia=fecha[0:fecha.find(",")].lower()
DD=int(fecha[fecha.find(",")+2:fecha.find("/")])
MM=int(fecha[fecha.find("/")+1:])

if DD>31 or MM>12:
    print("Error al ingresar los datos")  
    quit()
 

if dia=="lunes" or dia=="martes" or dia=="miercoles":
    print("¿Hubo examen? escriba si o no: ")    
    exam=input()    
    if exam=="si":
        print("¿Cuántos aprobados?:")
        examaprob=int (input())
        print("¿Cuántos desaprobados?:")
        examdes=int (input())
        total=int (examaprob+examdes) 
        print("El porcentaje de alumnos aprobados es del: ",(examaprob*100)/total,"%")
if dia=="jueves":
   print("¿Cuántos alumnos asistieron a la clase?")
   alum=int(input())
   print("¿Cuántos alumnos son en total?")
   alumtotal=int (input())
   if alum>=(alumtotal/2):
       print("Asistió la mayoria")
   else:
       print("No asistió la mayoria")   
if dia=="viernes":
    if (DD==1 and MM==1) or (DD==1 and MM==7):
     print("Comienzo de nuevo ciclo. Ingrese la cantidad de alumnos:")
     totalum=int (input())
     print("¿Cuál es el arancel por alumno?")
     arancel=int (input())
     ingtotal=arancel*totalum
     print("el ingreso total de este ciclo será: $",ingtotal)
else:
    print("error al ingresar el día")   
           