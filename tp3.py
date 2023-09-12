import math
#1--------------------------------------------------------------------------------()
word = str(input("Ingrese una frase cualquiera  "))
for n in range(10):
  print(word)
print("")  
#2--------------------------------------------------------------------------------()
age = int(input("Ingrese cual es su edad: "))
for n in range(age):
  if n == 0:
    print("En algun momento usted cumplio 1 año")
  else:
    print(f"En algun momento usted cumplio {n+1} años.")
print("")    
#3--------------------------------------------------------------------------------()
counter = 0
final_word = ""
num = int(input("Ingrese un numero entero positivo: "))
if num < 0:
  print("Error: Usted ingreso un numero negativo")
else:
  for n in range(num + 1):
    if n % 2 == 0:
      counter = counter + 1
    else:
      temp = str(n)
      if temp == "1":
        final_word = final_word + temp
      else:
        final_word = final_word + "," + temp
print(final_word)
print("")
#4--------------------------------------------------------------------------------()
final_word = ""
num = int(input("Ingrese un numero entero positivo: "))
if num < 0:
  print("Error: Usted ingreso un numero negativo.")
else:
  for n in range(num + 1):
    temp = str(n)
    if temp == "0":
      final_word = temp + final_word
    else:
      final_word = temp + "," + final_word
print(final_word)
print("")
#5--------------------------------------------------------------------------------()
i=int 
num=(int(input("Ingrese un numero: ")))
for i in range(num,0,-1):
  print(i, end= ",")
print(0)
print("")
#6--------------------------------------------------------------------------------()
triangle = int(input("Ingrese la altura del triángulo: "))
x=0
body="*"
while x <= triangle:
    print(body * x)
    x = x + 1
print("")
#7--------------------------------------------------------------------------------()
for n in range(11):
  print(f"Tabla del {n}")  
  for i in range(11):
    if n == 0 or i == 0:
      print("")
    else:
      print(f"{n}x{i}={n*i}")
print("")      
#8--------------------------------------------------------------------------------()
columns = int(input("Ingrese la cantidad de columnas: "))
columns=columns*2
for n in range(columns + 2):
  print("")
  for i in range(n - 1, 0, -2):
    if i % 2 == 0:
      numbers=1
    else:
      print(i, end=" ")
print("")
#9--------------------------------------------------------------------------------()
password="Excalibur"
check=0
while check==0:
  rep=str(input("Ingrese la contraseña: "))
  if rep==password:
    print("Bienvenido a Camelot")
    check=1
  else:
    print("Contraseña no valida, intenta de nuevo")
    check=0
print(" ")  
#10-------------------------------------------------------------------------------()
prime_number = 0
number = int(input("Ingrese un entero positivo para saber si es primo o no: "))
for i in range(number-1, 1, -1):
    if number%i == 0:
        prime_number = 1
if prime_number==0:
    print(f"El numero {number} es primo.")
elif prime_number==1:
    print(f"El numero {number} no es primo.")
print(" ")
#11-------------------------------------------------------------------------------()
final_word = ""
word = str(input("Ingrese una palabra: "))
l = len(word)
for n in range(l-1 , -1, -1):
  final_word = final_word + word[n]
print(final_word)
print(" ")  
#12-------------------------------------------------------------------------------()
phrase = input("Escriba una frase: ")
letter = input("Ingrese la letra a contar: ")
alphabet = "abcdefghijklmnñopqrstuvwxyz"
counter = 0
alphabet_checker = 0
for n in range (0, len(alphabet), 1):
    a = alphabet[n]
    if letter==a:
        alphabet_checker = 1
if alphabet_checker==1:
    for i in range (0,len(phrase),1):
        b=phrase[i]
        if letter==b:
            counter = counter + 1
    print(f"La letra {letter} fue encontrada {counter} veces en la frase.")
else:
    print(f"No ha ingresado una letra ({letter}). Inténtelo nuevamente.")
print(" ")
#13-------------------------------------------------------------------------------()
print("Escriba cualquier cosa para escuchar eco, o")
print("escriba 'salir' para dejar de escuchar el eco:")
words = "example"
while words != "salir":
    words = input(">>> ")
    if words != "salir":
        echo = words
        print("Eco:", echo)
print("Saliste con éxito.")
print(" ")
#14-------------------------------------------------------------------------------()
num_1= int(input("Ingrese un número entero: "))
num_2 = int(input("Ingrese otro número entero: "))
print(" ")
if num_2 < num_1:
    switch = num_2
    num_2 = num_1
    num_1 = switch
print(f"Los números pares entre {num_1} y {num_2} son:")
for n in range(num_1, num_2+1, 1):
    if n%2 == 0:
        print(end=f"{n} ")
print(" ")
print(" ")
print(f"Los números impares entre {num_1} y {num_2} son:")
for n in range(num_1, num_2+1, 1):
    if n%2 != 0:
        print(end=f"{n} ")
print(" ")
print(" ")
#15-------------------------------------------------------------------------------()
number = int(input("Ingrese un número entero positivo para conocer sus divisores: "))
divisors = ""
for i in range(number, 1, -1):
    if number%i == 0:
        divisors = divisors + str(i)
        divisors = divisors + ", "
divisors = divisors + "1"
print(f"Los divisores de {number} son:")
print(divisors)
print(" ")
#16-------------------------------------------------------------------------------()
numb = float(input("Ingrese la cantidad de números a escribir: "))
n = 1
negative = 0
keyboard_input = 1
while n <= numb:
    keyboard_input = float(input(f"Ingrese el número {n}: "))
    n = n + 1
    if keyboard_input < 0:
        negative = negative + 1
print(f"Usted ha ingresado {negative} números negativos.")
print(" ")
#17-------------------------------------------------------------------------------()
value_o = 0
value_a = 0
value_e = 0
value_i = 0
value_u = 0.
word = (str(input("Ingrese una frase  "))).lower()
p = len(word)
for i in range(p):
  if word[i] == "a":
    value_a = 1
  elif word[i] == "e":
    value_e = 1
  elif word[i] == "i":
    value_i = 1
  elif word[i] == "o":
    value_o = 1
  elif word[i] == "u":
    value_u = 1   
if value_a == 1:
  print("Contiene a")
if value_e == 1:
  print("Contiene e")
if value_i == 1:
  print("Contiene i")
if value_o == 1:
  print("Contiene o")
if value_u == 1:
  print("Contiene u")
print("")
#18-------------------------------------------------------------------------------()
num = 0
temp = 1
for n in range(10):
  if n == 0:
    print(0)
  else:
    fibo = num + temp
    print(fibo)
    temp=num
    num=fibo
print("")    
#19-------------------------------------------------------------------------------()
goal = float(input("Ingrese el total que desea juntar: "))
cash_total = 0
print("Empezemos a guardar dinero.")
input_checker = 0
while input_checker == 0:
    cash_savings = float(input("Ingrese dinero en la alcancía: "))
    if cash_savings <=0:
        print("Incorrecto, no puede meter esa cantidad. Inténtelo nuevamente.")
    else:
        input_checker = 1
        cash_total = cash_total + cash_savings
input_checker = 0
while input_checker == 0:
    print(f"Todavía falta dinero! Necesitamos ${goal - cash_total} para el objetivo.")
    cash_savings = float(input("Ingrese más dinero a l8a alcancía: "))
    if cash_savings <=0:
        print("Incorrecto, no puede meter esa cantidad. Inténtelo nuevamente.")
    else:
        cash_total = cash_total + cash_savings
        if cash_total >= goal:
                input_checker = 1
if cash_total > goal:
    extra = cash_total - goal
    print(f"Felicidades! Ha alcanzado el objetivo de ${goal}, y ahorró ${extra} de más.")
else:
    print(f"Felicidades! Ha alcanzado el objetivo de ${goal}.")
print(" ")
#20-------------------------------------------------------------------------------()
read = 1
sumatory = 0
while read != 0:
    print("Ingrese números de a uno para sumarlos, o")
    read = int(input("ingrese 0 para dejar de agregar: "))
    sumatory = sumatory + read
    print("")
print(f"La sumatoria de los números ingresados es {sumatory}")
print(" ")
#21-------------------------------------------------------------------------------()
read = 1
biggest = 0
while read != 0:
    print("Ingrese un número o ingrese")
    read = int(input("0 para terminar: "))
    if read > biggest:
        biggest = read
print(f"El número más grande ingresado es el {biggest}")
print(" ")
#22-------------------------------------------------------------------------------()
even_numbers = 0
rep = 1
final = 0
while rep == 1:
  final = 0
  final_s = ""
  num = int(input("Ingrese un numero "))
  num_s = str(num)
  num_len = len(num_s)
  if num % 2 == 0:
    even_numbers = even_numbers + 1
  for p in range(num_len):
    final = int(num_s[p]) + final
    if p == 0:
      final_s = final_s + num_s[p]
    else:
      final_s = final_s + "+" + num_s[p]
  print(final_s, "=", final)
  print("¿Desea ingresa otro numero?")
  rep2 = int(input("[1].Si  [-1].No  "))
  if rep2 == -1:
    rep = 0
  else:
    rep = 1
print(f"Usted ingreso un total de {even_numbers} numeros pares")
print("")
#23-------------------------------------------------------------------------------()
bill = 0
bill_input = 1
while bill_input != 0:
    print("Ingrese el monto del producto,")
    bill_input = float(input("o 0 para terminar: "))
    bill = bill + bill_input
print(f"El monto total de la factura es de ${bill}")
print(" ")
#24-------------------------------------------------------------------------------()
bill = 0
bill_input = 1
while bill_input != 0:
    print("Ingrese el monto del producto,")
    bill_input = float(input("o 0 para terminar: "))
    if bill_input < 0:
        print("El monto ingresado es incorrecto, ingrese uno nuevo.")
    else:
        bill = bill + bill_input
if bill < 1000:
    print(f"El monto total de la factura es de ${bill}")
else:
    bill = bill * 0.9
    print(f"El monto total de la factura (con descuento incluido) es de ${bill}")
print(" ")
#25-------------------------------------------------------------------------------()
factorial_result = 1
factorial = int(input("Ingrese un entero para conocer su factorial: "))
if factorial == 0:
    print("El factorial de 0 es 1.")
elif factorial > 0:
    fact = factorial
    while factorial > 0:
        factorial_result = factorial_result * factorial
        factorial = factorial - 1
    print(f"El factorial de {fact} es {factorial_result}.")
else:
    print("No está definido el factorial de un número negativo.")