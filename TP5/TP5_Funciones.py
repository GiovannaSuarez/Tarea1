import math
#1----------------------------------------------------------------------------------------
def dni_cheker(dni):
    dni_string = str(dni)
    if len(dni_string) >= 7 and len(dni_string) < 9:
        return True
    else:
        return False
#2----------------------------------------------------------------------------------------
# Longitud de la ultima palabra
def last_word_len (phrase):
    phrase = list(phrase)
    while True:
        if phrase[0]==" ":
            phrase.remove(phrase[0])
        else:
            break
    phrase = "".join(phrase)
    word_len = len(phrase[0:phrase.find(" ")])
    return word_len
#3----------------------------------------------------------------------------------------
# el primer nombre, la cantidad de letras del apellido y
# los 3 primeros dígitos de su DNI.
#ID -> Maria7254
def id_maker(username1, usersurename, dni):
    id = "ID ->" + username1.capitalize() + str(len(usersurename)) + (str(dni))[0:3]
    return id
#4----------------------------------------------------------------------------------------
#Crea una función que reciba los dos números, 
# y devuelve si el primero es múltiplo del segundo.

def Multi_Checker(num,multi):
    if num%multi==0:
        return True
    else:
        return False

#5----------------------------------------------------------------------------------------
# Promedio de temperatura
def prom_temp (min_temp, max_temp):
    prom = (min_temp + max_temp)/2
    return prom

#6----------------------------------------------------------------------------------------
# Ejercicio 6 (funcion)

def ExtraSpacing(txt):
	txt_con_espacio = txt.replace(""," ")
	return txt_con_espacio

#7----------------------------------------------------------------------------------------
# Ejercicio 7 (funcion)

def CalculateMaxMin(list_num):
	return (max(list_num),min(list_num))
#8----------------------------------------------------------------------------------------
#área y el perímetro
#perimetro=2.pi.r
#area=pi.r^2
def area_perimeter(rad):
    rad=float(rad)
    print(f"El perimetro de la circunferencia es {int(2*math.pi*rad)} y el area de la circunferencia es {int(math.pi*rad**2)}")

#9----------------------------------------------------------------------------------------
#devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”

def login(username,password,login_attempts):
    last=[]
    if username=="usuario1" and password=="asdasd":
        last.append(True)
        last.append(login_attempts)
        return last
    else:
        last.append(False)
        login_attempts=login_attempts+ 1
        last.append(login_attempts)
        return last
#10----------------------------------------------------------------------------------------



#11----------------------------------------------------------------------------------------
def fuction_list(function,A):
    lest=[]
    for i in A:
        lest.append(function(i))
    return lest
def double(num):
    return num*2
#12----------------------------------------------------------------------------------------""
#Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
def phrase_dictionary(phrasse):
    palabras_divididas = phrasse.split(" ")
    for i in palabras_divididas:
        dictionary={i:len(i)}
        print(dictionary)
        

#13----------------------------------------------------------------------------------------
def sum_square(x, y):
    
    return x + y ** 2

def module(v):
    from functools import reduce
    return int(reduce(sum_square, v, 0) ** 0.5)
#14----------------------------------------------------------------------------------------
# Números primos
def prime_checker (num):
    is_prime = True
    for i in range (2, num, 1):
        if num%i==0:
            is_prime = False
    return is_prime

#15----------------------------------------------------------------------------------------
def funtion_factorial(number_):   
    facto_amount=0
    while True:
        print(f"El factorial del número {number_} es : { math.factorial(number_)}")
        facto_amount=facto_amount+1
        rep=int(input("Ingrese otro número o ingrese 0 para salir  "))
        if rep==0:
            print(f"La cantidad total de numeros leidos es de: {facto_amount}")
            break
        else:
            number_=rep
#16----------------------------------------------------------------------------------------
def digit_counter(num,digit):
    counter=0
    strig_num=str(num)
    string_digit=str(digit)
    for i in range(len(strig_num)):
        if strig_num[i]==string_digit:
            counter=counter+1
    return counter 

#17----------------------------------------------------------------------------------------
# Contador de frecuencia del digito
def frequency_digit_counter(num, digit):
    counter = num.count(digit)
    return counter


# Sumador de digitos
def digit_counter2 (counter):
    number_counter = 0
    for i in range (0, len(str(counter)), 1):
        number_counter = number_counter + int(str(counter)[i])
    return number_counter


