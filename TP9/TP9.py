import Clases
#1.	Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
#•	Un constructor, donde los datos pueden estar vacíos.
#•	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
#•	mostrar(): Muestra los datos de la persona.
#•	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
person1=Clases.person()
person1.mostrar()
if person1.esMayorDeEdad():
    print("La persona es mayor de edad")
elif person1.esMayorDeEdad()==-1:
    print("No hay datos para la persona")
else:
    print("La persona no es mayor de edad")

#2.	Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
#•	Un constructor, donde los datos pueden estar vacíos.
#•	Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
#•	mostrar(): Muestra los datos de la cuenta.
#•	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#•	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
acount1=Clases.acount("Emilio",2000)
acount1.show()
acount1.deposit(200)
acount1.deposit(-200)
acount1.withdraw(400)
acount1.withdraw(-400)
acount1.show()
#3.	Desarrollar un programa que cargue los datos de un triángulo. 
#Implementar una clase con los métodos para inicializar los atributos, 
#imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).
max_side=-1
triangle1=Clases.triangle()

side=float(input((f"Ingrese el valor la lado 1:  ")))
triangle1.set_side1(side)
side=float(input((f"Ingrese el valor la lado 2:  ")))
triangle1.set_side2(side)
side=float(input((f"Ingrese el valor la lado 3:  ")))
triangle1.set_side3(side)
temp_list=[triangle1.get_side1(),triangle1.get_side2(),triangle1.get_side3()]
for i in range(len(temp_list)):
    if temp_list[i]>max_side:
        max_side=temp_list[i]
        max_side_pos=i+1
print(f"El lado mas largo del triangulo es el lado {max_side_pos} con un valor de {max_side}")

if triangle1.get_side1()==triangle1.get_side2() and triangle1.get_side2()==triangle1.get_side3():
    print("El triangulo es Equilatero")
elif triangle1.get_side1()!=triangle1.get_side2() and triangle1.get_side1()!=triangle1.get_side3() and triangle1.get_side2()!=triangle1.get_side3():
    print("El triangulo es escaleno")
else:
    print("El triangulo es isolceles")
#4.	Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:
#•	Añadir contacto
#•	Lista de contactos
#•	Buscar contacto
#•	Editar contacto
#•	Cerrar agenda
name=str(input("Ingrese su nombre"))
diary1=Clases.diary(name)


