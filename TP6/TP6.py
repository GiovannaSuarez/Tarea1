import random
import TP6_Funciones
import math
#1-------------------------------------------------------------------------------------
#1.Solicitar al usuario que ingrese números, estos deben guardarse en una lista. 
#Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.
YellowSubmarine=[]
while True:
    rep = float(input("Ingrese un numero para guardar en una lista , ingrese 0 para salir  "))
    if rep == 0:
        break
    else:
        YellowSubmarine.append(rep)
#2-------------------------------------------------------------------------------------
#2.	A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, 
#eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

number=float(input("Ingrese un numero, si el numero ingresado esta en la lista, lo eliminare  "))
for i in range(len(YellowSubmarine)):
    if YellowSubmarine[i]==number:
        del YellowSubmarine[i]
        break
#3-------------------------------------------------------------------------------------
#3.	Imprimir la sumatoria de todos los números de la lista.
totalNumber=0
for i in range(len(YellowSubmarine)):
    totalNumber=totalNumber+YellowSubmarine[i]
print(f"La suma total de los numeros de la lista es {totalNumber}")
#4-------------------------------------------------------------------------------------
#4.	Solicitar al usuario otro número y crear una lista con los elementos de la lista original, 
# que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
RedSubmarine=[]
user_number=float(input("Ingrese un numero, creare una nueva lista con los numeros menores al ingresado   "))
for i in range(len(YellowSubmarine)):
    if YellowSubmarine[i]<user_number:
        RedSubmarine.append(YellowSubmarine[i])
print("Lista impresa:  ")
for i in range(len(RedSubmarine)):
    print(RedSubmarine[i])
#5-------------------------------------------------------------------------------------
#5.	Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número de la 
# lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2], 
# la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]
p_amount=0
PinkSubmarine=[]
PurpleSubmarine=[4,2,4,2,7,9,1,9]
for i in PurpleSubmarine:
    for p in range(len(PurpleSubmarine)):
        if PurpleSubmarine[p]==i:
            p_amount=p_amount+1
    PinkSubmarine.append((i,p_amount))
    p_amount=0
for i in PinkSubmarine:     
    copy_amount=0
    for p in range(len(PinkSubmarine)):
        if PinkSubmarine[p]==i:
            copy_amount=copy_amount+1
    if copy_amount>1:
        for p in range(len(PinkSubmarine)):
            if PinkSubmarine[p]==i:
                del PinkSubmarine[p]
                break
print(f"Lista original: \n{PurpleSubmarine}")
print(f"Lista nueva: \n{PinkSubmarine}")
#6------------------------------------------------------------------------------------
#6
print("ESCUELA")
print()

print("Nivel Primario")
primary_students = set()

while True:
    name1 = input("Ingrese el nombre de pila del estudiante (o 'x' para finalizar): ")
    if name1 == 'x':
        break
    primary_students.add(name1)

print()
print("Nivel Secundario")
secundary_students = set()

while True:
    name2 = input("Ingrese el nombre de pila del estudiante (o 'x' para finalizar): ")
    if name2 == 'x':
        break
    secundary_students.add(name2)

print()
print("a. Nombres de todos los alumnos sin repeticiones:")
all_students = primary_students.union(secundary_students)
print(all_students)

print()
print("b. Nombres que se repiten entre los alumnos de nivel primario y secundario:")
repeated_names = primary_students.intersection(secundary_students)
print(repeated_names)

print()
print("c. Nombres de nivel primario que no se repiten en nivel secundario:")
unique_names_primary = primary_students.difference(secundary_students)
print(unique_names_primary)
#7-------------------------------------------------------------------------------------
#7.	Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. 
# Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados
letters=[]
words=[]
#Obener todas las palabras
for i in range(50):
    words.append(str(input(f"Ingrese la frase o palabra numero {i+1}   ")).lower())
#Guardar todas las letras en una lista sin que se repitan
for i in words:
    for p in range(len(i)):
        found_match=False
        for j in letters:
            if i[p]==j:
                found_match=True
        if not found_match:
            letters.append(i[p])
#Crear diccionario
letters_counter={}
for i in letters:
    letters_counter[i]=0
#Contar todas las letras
words=str(words)
for i in range(len(words)):
    for p in letters:
        if words[i]==p:
            letters_counter[f"{p}"]=letters_counter[f"{p}"]+1
#Mostrar la inforamcion recolectada
print("")
for i in letters:
    print(f"La letra o simbolo {i} aparecio un total de {letters_counter[i]}\n  ")
#8-------------------------------------------------------------------------------------
#8.	Diez equipos de la liga inter-barrial identificados con los números 1, 2, 3, 4, …, 10, participaron en un campeonato de fútbol con modalidad todos contra todos.
#Escriba un programa que:
#o	Lea el cuadro de goles en un arreglo de dos dimensiones.
#o	Muestre para cada equipo la cantidad de triunfos, empates y derrotas.
#o	Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
#o	Determine la cantidad de puntos obtenidos por cada equipo.

#o	Lea el cuadro de goles en un arreglo de dos dimensiones.
results=list(range(10))
while True:
    rep=int(input(f"¿Desea usar una lista de resultados pre-creada o llenar la informacion a mano?\n[1].Usar resultados pre-creadados\n[2].Llenar resultados a mano\n  "))
    if rep==1:
        results=[[0,4,2,1,5,3,0,2,4,7],[5,0,3,2,3,0,1,4,6,2],[0,2,0,1,4,2,5,3,5,0],[1,0,2,0,5,4,2,3,1,6],[7,4,2,3,0,5,1,4,0,0],[5,1,2,4,5,0,3,0,2,4],[4,7,0,2,4,3,0,1,6,2],[5,3,2,4,1,0,7,0,5,1],[2,6,2,0,1,4,5,7,0,0],[7,4,2,4,1,6,0,5,3,0]]
        break
    elif rep==2:
        results=TP6_Funciones.manual_fill(results)
        break
    else:
        print("Numero no valido, intente denuevo")

#o	Muestre para cada equipo la cantidad de triunfos, empates y derrotas.   
#o	Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
#o	Determine la cantidad de puntos obtenidos por cada equipo.
for i in range(0,10):
    temp_victorys=0
    temp_loses=0
    temp_ties=0
    total_positive_score=0
    total_negative_score=0
    for p in range(0,10):
        if i==p:
            continue
        else:
            if results[i][p]>results[p][i]:
                temp_victorys+=1
            elif results[i][p]<results[p][i]:
                temp_loses+=1
            else:
                temp_ties+=1
            total_positive_score=total_positive_score+results[i][p]
            total_negative_score=total_negative_score+results[p][i]
        if total_positive_score>total_negative_score:
            final_score=total_positive_score-total_negative_score
        else:
            final_score=total_negative_score-total_positive_score
    print(f"Equipo {i+1}:\nVictorias:{temp_victorys}\nDerrotas:{temp_loses}\nEmpates:{temp_ties}\nDiferencia entre los goles marcados y recibidos:{final_score}\nPuntos totales del equipo:{(temp_victorys*3)+temp_ties}\n  ")

#9-------------------------------------------------------------------------------------
#9.	Escribir un programa que simule el juego clásico de Memoria (Memotest) utilizando matrices. 
#El juego consiste en un t
# ablero de cartas boca abajo y el objetivo es encontrar todas las parejas de cartas iguales.

table=[]
table_hidden=[["?","?","?","?"],["?","?","?","?"],["?","?","?","?"]]
cards=[1,1,2,2,3,3,4,4,5,5,6,6]
for i in range(3):
    temp_table=[]
    for p in range(4):
        if len(cards)-1==-1:
            random_temp=0
        else:
            random_temp=random.randint(0,len(cards)-1)  
        value_temp=cards[random_temp]
        del cards[random_temp]
        temp_table.append(value_temp)
    table.append(temp_table)


win_condition=0
lose_condition=10
print("¡Bievenido al Memotest Dinamita!")
while True:
    if lose_condition<1:
        win=False
        break
    elif win_condition>=6:
        win=True
        break
    else:
        TP6_Funciones.show_table(table_hidden)
        print(f"Intentos restantes:{lose_condition}")
        row=int(input("Ingresa el numero de la fila  "))
        colum=int(input("Ingrese el numero de la columna  "))
        table_hidden[row][colum]=table[row][colum]
        row_temp=row
        colum_temp=colum
        while True:
            TP6_Funciones.show_table(table_hidden)
            row=int(input("Ingresa el numero de la fila  "))
            colum=int(input("Ingrese el numero de la columna  "))
            if row==row_temp and colum==colum_temp:
                print("¡No puedes seleccionar la misma poscicion tontin!, intenta denuevo")
            else:
                break
        if table[row_temp][colum_temp]==table[row][colum]:
            table_hidden[row][colum]=table[row][colum]
            win_condition=win_condition+1
            print("¡Acertaste!")
        else:
            table_hidden[row][colum]=table[row][colum]
            TP6_Funciones.show_table(table_hidden)
            table_hidden[row][colum]="?"
            table_hidden[row_temp][colum_temp]="?"
            lose_condition=lose_condition-1
            print("¡Fallaste!")
            print(" ")
    
if win:
    print("¡Ganaste!")
else:
    print("¡Perdiste!")
#10------------------------------------------------------------------------------------
#10.Teniendo una matriz cuadrada de cualquier dimensión, obtener lo siguiente:
#a.	la diagonal principal.
#b.	la diagonal inversa.
#d=2/b**2+a**2

cube=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

dig_main=math.sqrt(len(cube)**2+len(cube[len(cube)-1])**2)
dig_inver=dig_main

print(f"La diagonal principal es igual a {dig_main} y la diagonal inversa es {dig_inver}")
#11------------------------------------------------------------------------------------
#11.Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
cambio_diccionario={'EURO':'€', 'DOLLAR':'$', 'YEN':'¥'}
print("Bienvenido")
print("Ingrese una de las siguientes divisas para conocer su símbolo: ")
print("Euro")
print("Dollar")
print("Yen")
divisa=str(input()).upper()

for i in cambio_diccionario.keys():
    if i == divisa:
        print (f"El símbolo para la divisa {divisa} es : {cambio_diccionario[i]}")
#12.Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un 
# diccionario. Después debe mostrar por pantalla el mensaje ‘<nombre> tiene <edad> 
# años, vive en <dirección> y su número de teléfono es <teléfono>’.

name=str(input("Ingrese su nombre  ")).capitalize()
while True:
    age=int(input("Ingrese su edad  "))
    if age<=0:
        print("La edad ingresada no es valida, intente denuevo")
    else:
        break
location=str(input("Ingrese su direccion  "))
while True:
    phonenumbrer=int(input("Ingrese su numero de telefono (debe tener  9 digitos)   "))
    if len(str(phonenumbrer))<9 or len(str(phonenumbrer))>9:
        print("Numero no valido, intente denuevo")
    else:
        break
data={"name":name,"age":age,"location":location,"phonenumber":phonenumbrer}
print(f"{data['name']} tiene {data['age']} años, vive en {data['location']} y su numero de telefono es {data['phonenumber']}")
#13---------------------------------------------------------------------------------------------------------------------------------------
#13.Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, 
# un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario 
# debe mostrar un mensaje informando de ello.
fruit_price={'pera':600,'manzana':500,'banana':700,'naranja':650,'frutilla':800,'melon':800,'mandarina':850,'cereza':950}
while True:
    fruit=str(input("Ingrese una fruta: ")).lower()
    if fruit in fruit_price:
        print(f"Seleccionó {fruit}")
        break
    else:
        print("La fruta no se encuentra en el diccionario, intente nuevamente...") 
        continue   

cant_k=int(input(f"¿El precio de cuántos kilos de {fruit} desea conocer?"))            
for i in fruit_price:
    if i == fruit:
        total=cant_k*fruit_price[i]
        print (f"Para {cant_k}k de {fruit}, el total seria: ${total}")