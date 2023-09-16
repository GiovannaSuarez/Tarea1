import math
#1 english----------------------------------------------------------()
x = 0
while x <= 30:
  x = x + 1
  if x==4 or x==6 or x==10:
    print(f"Se saltó el el valor {x} de x.")
  elif x==15:
    print(f"Se rompió la ejecución del bucle cuando x valía {x}.")
    break
  else:
    print(x)
print("")
#1------------------------------------------------------------------()
list = []
exit = True
line_number = int(input("Cuantas lineas desea ingresar  "))
for i in range(line_number):
  temp = str(input("Ingrese una linea  "))
  list = list + [temp]
print("")  
while exit == True:
  for p in range(line_number):
    print(list[p].upper())
  break  
print("")
#2------------------------------------------------------------------()
bank_account = 0
bank_movements = 0
print("Bienvenido a Dinamite Bank. Las operaciones disponibles son:")
print("Retiros: R y el monto, ejemplo: R 200")
print("Depósitos: D y el monto, ejemplo: D 500")
print("Salir: Deje el espacio vacío y presione 'enter'")
while True:
    bank_input = input("Ingrese la operación y el monto con el formato dado:").upper()
    if len(bank_input)==0:
        break
    bank_operation = bank_input[0]
    if len(bank_input)>3:
        bank_movements = float(bank_input[2:])
    if bank_input[1]!=" ":
        print("Error. Ingrese una operación con el formato dado")
    if bank_operation=="D":
        if bank_movements<0:
            print("Error. No puede depositar negativamente. Intente nuevamente.")
        else: 
            bank_account = bank_account + bank_movements
    elif bank_operation=="R":
        if bank_movements<0:
            print("Error. No puede retirar negativamente. Intente nuevamente.")
        elif (bank_account-bank_movements)<0:
            print(f"Error. No puede retirar más fondos de los que ya tiene (${bank_account}). Intente nuevamente.")
        else:
            bank_account = bank_account - bank_movements
    else:
        print("Error. Ingrese una operación con el formato dado")
print(f"Ha salido con éxito. Su balance es de ${bank_account}")
print("")
#3------------------------------------------------------------------()
prime = 0
prime_number = 0
while True:
    num = int(input("Ingrese números mayores a 0 (o 0 para salir): "))
    if num==0:
       break
    elif num<0:
       print("Solo puede ingresar números positivos.")
       continue
    for i in range(num-1, 1, -1):
       if num%i==0:
            prime_number = 1
    if prime_number == 0:
        prime = prime + 1
        continue
    elif prime_number==1:
        prime_number = 0
        continue
print(f"usted ha ingresado {prime} números primos.")
print("")
#4------------------------------------------------------------------()
checker = 0
while True:
  while True:
    try:
      first_year = int(input("Ingrese un año: "))
    except ValueError:
      print("El número ingresado no es correcto. Intente nuevamente.")
      continue
    else:
      break
  while True:
    try:
      last_year = int(input("Ingrese otro año: "))
    except ValueError:
      print("El número ingresado no es correcto. Intente nuevamente.")
      continue
    else:
      break
  if first_year == last_year:
    print("No pueden ser iguales los años. Intente nuevamente.")
    continue
  else:
    break
if last_year < first_year:
  switch = first_year
  first_year = last_year
  last_year = switch
print(f"Los años biciestos y múltiplos de 10 entre {first_year} y {last_year} son:")
print("")
for i in range(first_year, last_year+1, 1):
  if ((i%4==0 and i%100!=0) or i%400==0) and i%10==0:
    checker = 1
    print(i, end=" ")
if checker == 0:
  print("No hay años biciestos y múltiplos de 10 en el rango elegido.")
print("")
print("") 
#5------------------------------------------------------------------()
print("Los numeros pares entre el 1 y el 20 son:")
for i in range(1, 21, 1):
  if i % 2 != 0:
    continue
  else:
    print(i)
print("")
#6------------------------------------------------------------------()
list = [1, 18, 3, 4, 10, 6, 12, 8, 20, 5, 11, 7, 13, 14, 15, 16, 17, 2, 19, 9]
exit = 1
while exit == 1:
  num_look = int(input("¿Que numero entre el 1 y 20 desea buscar? "))
  if num_look < 1 or num_look > 20:
    print("Ese numero no esta comprendido entre 1 y 20")
    print("Intente de nuevo")
    exit = 1
  else:
    exit = 0

for i in range(1, 21, 1):
  if list[i] == num_look:
    print(f"Numero {num_look} encontrado en la posición {i+1}")
    break
print("")
#7------------------------------------------------------------------()
import random

exit = True
while exit == True:
  print("")
  print("¡Elige una opcion si te atreves!")
  print("[1].Sorpresa")
  print("[2].50% ganas un millon de dolares 50%¡Mueres!")
  print("[3].Puedes ver que hay dentro de la caja misteriosa")
  print("[0].Salir :(")
  rep = int(input())
  print("")
  if rep == 1:
    print("¡Feliz cumpleaños!")
  elif rep == 2:
    num = random.randint(1, 2)
    if num == 1:
      print("Señoras y señores me complace anunciar que usted gano.... ¡UN MILLON DE DOLARES!")
    elif num == 2:
      print("Me temo que moriste...¡PERO SOBREVIVISTE!")
  elif rep == 3:
    num2 = random.randint(1, 6)
    if num2 == 1:
      print("Dentro de la caja hay...¡un vaso de leche!")
    elif num2 == 2:
      print("Dentro de la caja hay...¿Una piton?")
    elif num2 == 3:
      print("Dentro de la caja hay...¡Un chocolate milka!")
    elif num2 == 4:
      print("Dentro de la caja hay...¡Un cupon para un viaje!")
    elif num2 == 5:
      print("Dentro de la caja hay...¿Nada?")
    elif num2==6:
     print("Dentro de la caja hay...¡Un dinosaurio de plastico!")
  elif rep == 0:
    print("¡No me dejes!")
    break