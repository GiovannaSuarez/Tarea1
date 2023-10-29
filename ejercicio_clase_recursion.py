#EJERCICIOs en clase RECURSIONES

#---(1)---
# Escribir una función que simule el siguiente experimento: Se tiene una rata en una 
# jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma 
# probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5 
# minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula. 
# La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad, pero 
# quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.
# La función debe devolver el tiempo que tarda la rata en salir de la jaula.


import random

import random

def experiment_ratita(time_accumulated=0):
    choice = random.choice([1, 2, 3])
    if choice == 1:
        time_accumulated += 3
    elif choice == 2:
        time_accumulated += 5
    else:
        time_accumulated += 7
        return time_accumulated
    return experiment_ratita(time_accumulated)

time_out = experiment_ratita()
print("La rata tardó", time_out , "minutos en salir de la jaula.")


#---(2)---
#funcion para dar vuelta el número ingresado
def f(n):
    s=str(n)
    if len(s)<=1:
        return s
    return s[-1] + f(int(s[:-1])) 

print("Bienvenido al mundo del revés")
ff=int(input("Ingrese un número y te mostraremos cómo se veria: "))
print(f(ff))
