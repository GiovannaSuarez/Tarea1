#EJERCICIO DE FUNCIONES
#DEFINICION DE FUNCIONES
#El error del código es que en vez de pasarle a la función las variables
#(x,y) , le pasaba (a,b) 

def most(x,y):
    if (x>y):
        return x
    else:
        return y 
    
def least (x,y):
    if (x<y):
        return x
    else:
        return y 
    
#programa principal

x=int(input("Un número: "))
y=int(input("Otro número: "))

print(most(x-3, least(x+2, y-5)))       