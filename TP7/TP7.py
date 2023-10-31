import Ordenamiento
#1.	Escribe un programa que tome una lista de números como entrada y 
# la ordene en orden ascendente utilizando el método de ordenamiento de burbuja.

numbers=[2,4,2,7,3,16,60,32]
p=0
numbers=Ordenamiento.bubble_sort(numbers)
for i in numbers:
    print(f"El valor numero {p+1} de la lista es: {i}")
    p=p+1
#2.	Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden ascendente utilizando el método de ordenamiento de selección.
arr=[]
while True:
    word=str(input("Ingrese una palabra  "))
    arr.append(word)
    word=int(input("¿Desea ingresar otra?\n[1].Si\n[2].No\n  "))
    if word==1:
        continue
    else:
        break
arr=Ordenamiento.selection_sort(arr)
p=1
for i in arr:
    print(f"La palabra en la poscicion {p} es {i}")
    p+=1
#3.	Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro (título, autor, año de publicación, etc.). 
# Luego, escribe un programa que ordene la lista de libros en función de un campo específico, como el año de publicación o el autor.
books=[{"Titulo":"Juego de Tronos","Autor":"George.R.R.Martin","Año de publicacion":"1996","Genero":"Novela"},{"Titulo":"Mort","Autor":"Terry Pratchett","Año de publicacion":"1987","Genero":"Alta Fantasia"},{"Titulo":"Viaje al oeste","Autor":"Wu Cheng'en","Año de publicacion":"1592","Genero":"Fantasia"},{"Titulo":"Don Quijote de la Mancha","Autor":"Miguel de Cervantes","Año de publicacion":"1605","Genero":"Satira"}]
temp_list=[]
books_final=[]
while True:
    rep=int(input("¿En base a que clave le gustaria ordenar?\n[1].Titulo\n[2].Autor\n[3].Año de publicacion\n[4].Genero\n "))
    if rep==1:
        user_key="Titulo"
    elif rep==2:
        user_key="Autor"
    elif rep==3:
        user_key="Año de publicacion"
    elif rep==4:
        user_key="Genero"
    else:
        print("Numero no valido, intente nuevamente")
        continue
    break
for i in books:
    temp_list.append(i[user_key])
temp_list=Ordenamiento.bubble_sort(temp_list)
books_final=temp_list
print(temp_list)
for i in books:
    for p in range(len(temp_list)):
        if i[user_key]==temp_list[p]:
            books_final[p]=i
print(f"El orden final de los elementos es:")
print("")
p=1
for i in books_final:
    print(f"Poscicion {p}:\nTitulo del libro: "+i["Titulo"]+"\nAutor: "+i["Autor"]+"\nAño de publicacion: "+i["Año de publicacion"]+"\nGenero: "+i["Genero"]+"\n")
    p+=1

#4.	Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según su 
# longitud. Puedes utilizar el método de ordenamiento de inserción.
words=[]
while True:
    word=str(input("Ingrese una palabra  "))
    words.append(word)
    word=int(input("¿Desea ingresar otra?\n[1].Si\n[2].No\n  "))
    if word==1:
        continue
    else:
        break

number=[]
final_order=list(range(len(words)))
number_word={}
word_word={}
for i in words:
    number_word[i]=len(i)
    word_word[i]=i
    number.append(len(i))
number=Ordenamiento.insert_sort(number)
for i in words:
    for p in range(len(number)):
        if number_word[i]==number[p]:
            final_order[p]=word_word[i]
            number_word[i]=-1
            number[p]=-2
p=1
for i in final_order:
    print(f"La palabra en la poscicion {p} es {i} con {len(i)} letras")
    print("")
    p=p+1
#5.	Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden descendente en lugar de ascendente.
#Modificando el ejercio 1
numbers=[2,4,2,7,3,16,60,32]
new_numbers=list(range(len(numbers)))
p=0
i=0
numbers=Ordenamiento.bubble_sort(numbers)
while len(numbers)>=1:
    new_numbers[i]=numbers[-1]
    del numbers[-1]
    i=i+1
for i in new_numbers:
    print(f"El valor numero {p+1} de la lista es: {i}")
    p=p+1
#6.	Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo de ordenamiento por conteo.
arr=[]
while True:
    number=int(input("Ingrese un numero "))
    arr.append(number)
    number=int(input("¿Desea ingresar otro?\n[1].Si\n[2].No\n  "))
    if number==1:
        continue
    else:
        break
arr = Ordenamiento.countSortNegative(arr)
p=1
for i in arr:
    print(f"El numero en la poscicion {p} es {i}")
    print("")
    p=p+1

#7.Crea una lista que contenga tanto números como cadenas de caracteres. Escribe un programa que ordene esta lista de manera que primero estén los 
# números ordenados de menor a mayor y luego las cadenas de caracteres ordenadas alfabéticamente.

words_numbers=[]
words=[]
numbers=[]
while True:
    rep=int(input(f"¿Desea ingresar datos usted mismo o usar una lista pre-creada?\n[1].Ingresar datos manualmente\n[2].Usar lista pre-creda\n  "))
    if rep==1:
        while True:
            element=input("Ingrese un elemento ")
            words_numbers.append(element)
            element=int(input("¿Desea ingresar otro?\n[1].Si\n[2].No\n  "))
            if element==1:
                continue
            else:
                break
        break
    if rep==2:
        words_numbers=["b",4,"lactosa",7,"a",5,"cuatro",2,8,10,"tres",6,"papas","b","amarillo",]
    else:
        print("Nuemero no valido, intente denuevo")
        continue
    break

for i in words_numbers:
    if type(i)==str:
        words.append(i)
    else:
        numbers.append(i)
numbers=Ordenamiento.bubble_sort(numbers)
words=Ordenamiento.bubble_sort(words)
for i in words:
    numbers.append(i)
p=1
for i in numbers:
    print(f"El elemento de la poscision  {p} es: {i} ")
    print("")
    p+=1


#8.	Implementa el algoritmo de ordenamiento Merge Sort y úsalo para ordenar una lista de números.
print(" ")
p=0
numbers=[8,25,13,16,18,4,9,22,666]
numbers=Ordenamiento.merge_sort(numbers)
for i in numbers:
    print(f"El valor numero {p+1} de la lista es: {i}")
    p=p+1
