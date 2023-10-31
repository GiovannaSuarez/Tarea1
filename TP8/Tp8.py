import funciones
import random
#1.	Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.
while True:
    num=float(input("Ingrese un numero positivo y devolvere cuantos digitos tiene  "))
    if num<0:
        print("El numero igresado es negativo, intente denuevo")
    else:
        break
#2.	Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.
#a=b n
print("Dame 2 numeros enteros  n y b, te dire si n es potencia de b")
n=int(input("n=  "))
b=int(input("b=  "))

if funciones.power_of(n,b):
    print(f"{n}, es potencia de {b}")
else:
    print(f"{n}, no es potencia de {b}")
#3.	Escribir una funcion recursiva que reciba como parámetros dos strings 
# a y b, y devuelva una lista con las posiciones en donde se encuentra b dentro de a. 
a="Un tete a tete con Tete"
b="te"
print(funciones.frequency(a,b))
#4.	Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, conociendo solo que:
#•	1 es impar.
#•	Si un número es impar, su antecesor es par; y viceversa.

while True:
    num=int(input("Ingese un numero natural y devolvere si o no par  "))
    if num<0:
        print("El numero ingresado no es natural, intente denuevo")
    else:
        break

print(f"El numero {num}{funciones.even(num)}")

print(f"El la cantidad de digitos que tiene la funcion es de {funciones.num_len(num)}")
#5.	Escribir una función recursiva que encuentre el mayor elemento de una lista.

numbers=list(range(20))
for p in range(len(numbers)-1):
    numbers[p]=random.randint(1,30)

print(f"Lista:\n{numbers}")

print(f"El numero mas grande de la lista es {funciones.max_number(numbers)}")

#6.	Escribir una función recursiva para replicar los elementos de una lista una cantidad n de veces. 
# Por ejemplo, replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])

p=[1,2,3,4,5]
print(funciones.replicate(p,p,4))
#7.	Implemente un algoritmo, usando una función recursiva, que resuelva la siguientesumatoria:
#K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
#● El programa debe pedir al usuario que ingrese un número n, y un número d,
#● Luego debe calcular el valor de K(n, p) usando una función recursiva,
#● Debe imprimir el resultado de K(n, p)
print("Ingrese los valores para la funcion K(n,p)")
n=float(input("n= "))
p=float(input("p= "))

#8.	El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera: 
# Las filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha). 
# Los valores que se encuentran en los bordes del triángulo son todos unos. 
# Cualquier otro valor se calcula sumando los dos valores contiguos de la fila de arriba. Escribí la función recursiva pascal(n, k) que calcula el 
# valor que se encuentra en la fila n y la columna k.
print("Ingrese los cordenadas de un numero en el triangulo de pascal y devolvere su valor en esa poscicion(los valores deben ser positivos)")
while True:
    f=int(input(f"Fila:  "))
    if f<0:
        print("El ingresado para las filas es negativo, intente denuevo")
    else:
        break
while True:
    c=int(input(f"Columna:  "))
    if c<0:
        print("El ingresado para las columnas es negativo, intente denuevo")
    else:
        break

print(f"El valor en la fila {f} y columna {c} es: {funciones.pascal(f,c)}")

print(f"El resultado de la funcion K({n},{p}), es igual a {funciones.K(n,p,0)}")
#9.	Escribí una función recursiva combinaciones(lista, k) que reciba una lista de caracteres únicos, y un número k, 
# e imprima todas las posibles cadenas de longitud k formadas con los caracteres dados (permitiendo caracteres repetidos).

funciones.combinations(["a","p"],3,"")

#10.	La norma ISO 216 especifica tamaños de papel. Es el estándar que define el popular tamaño de papel A4 (210 mm de ancho y 297 mm de largo). 
# Las hojas A0 miden 841 mm de ancho y 1189 mm de largo. A partir de la A0 las siguientes medidas, digamos la A(N+1), 
# se definen doblando al medio la hoja A(N). Siempre se miden en milímetros con números enteros: 
# entonces la hoja A1 mide 594 mm de ancho (y no 594.5) por 841 mm de largo.
A=int(input("Ingrese que tipo de hoja que desea (A1,A2,A3...)\nA "))

results=(funciones.paper_size(A,0,841,1189))
print(f"La dimenciones de la hoja A{A} son {results[1]} mm de ancho y {results[0]} mm de alto ")