#1------------------------------------------------------------------------------------------------------
class person:
    def __init__(self,nombre="Desconocido",edad=-1,dni="1234567"):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
    def set_nombre(self,nombre):
        self.nombre=nombre
    def get_nombre(self):
        return self.nombre
    

    def set_edad(self,edad):
        while True:
            if edad>124:
                edad=int(input("Edad no valida, intente denuevo  "))
            else:
                self.edad=edad
                break
    def get_edad(self):
        return self.edad
    
    def set_dni(sefl,dni):
        while True:
            dni_string=str(dni)
            if len(dni_string)>7 or len(dni_string)<0:
                dni=int(input("Dni no valido, ingrese otro   "))
            else:
                sefl.dni=dni
                break


    def mostrar(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nDni: {self.dni}")
    
    def esMayorDeEdad(self):
        if self.edad>=18:
            return True
        elif self.edad==-1:
            return -1
        else:
            return False
#2-----------------------------------------------------------------------------------------------
#2.	Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
#•	Un constructor, donde los datos pueden estar vacíos.
#•	Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
#•	mostrar(): Muestra los datos de la cuenta.
#•	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
#•	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
class acount:
    def __init__(self,owner,amount=0):
        self.owner=owner
        self.amount=amount
    def set_owner(self,owner):
        self.owner=owner
    def get_owner(self):
        return self.owner
    def set_amount(self,amount):
        self.amount=amount
    def get_amount(self):
        return self.amount
    def show(self):
        print(f"Titular: {self.owner}\nCantidad en la cuenta: {self.amount}")    
    def deposit(self,depo):
        if depo>=1:
            self.amount=self.amount+depo
    def withdraw(self,wd):
        if wd<0:
            self.amount=self.amount+wd
        else:
            self.amount=self.amount-wd
#3.	Desarrollar un programa que cargue los datos de un triángulo. 
#Implementar una clase con los métodos para inicializar los atributos, 
#imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).
class triangle:
    def __init__(self,side1=1,side2=1,side3=1):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def get_side1(self):
        return self.side1
    def set_side1(self,side1):
        while True:
            if side1<1:
                side1=float(input("El numero ingresado para el lado 1  no es valido,intende denuevo  "))
            else:
                self.side1=side1
                break
    def get_side2(self):
        return self.side2
    def set_side2(self,side2):
        while True:
            if side2<1:
                side2=float(input("El numero ingresado para el lado 2  no es valido,intende denuevo  "))
            else:
                self.side2=side2
                break
    def get_side3(self):
        return self.side3
    def set_side3(self,side3):
        while True:
            if side3<1:
                side3=float(input("El numero ingresado para el lado 3  no es valido,intende denuevo  "))
            else:
                self.side3=side3
                break

#4.	Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:
#•	Añadir contacto
#•	Lista de contactos
#•	Buscar contacto
#•	Editar contacto
#•	Cerrar agenda

class diary:
    def __init__(self,username):
        self.username=username
    def set_username(self,username):
        self.username=username
    def get_username(self):
        return self.username
    

    def menu_start(self):
        contacts=[]
        while True:
            rep=int(input(f"Bienvenido/a {self.username}, ¿que accion le gustaria ejecutar?\n[1].Anadir contacto\n[2].Lista de contactos\n[3].Buscar contacto\n[4].Editar contacto\n[5].Cerrar agenda\n  "))
            if rep==1:
                contacts=self.add_contact(contacts)
            elif rep==2:
                self.list_contact(contacts)
            elif rep==3:
                self.search_contact(contacts)
            elif rep==4:
                self.edit_contact(contacts)
            elif rep==5:
                print(f"Opcion{rep}")
                break   
            else:
                print("Numero no valido, intente denuevo")
            
            
    def add_contact(self,contacts):
        name=(str(input("Ingrese el nombre del nuevo contacto  "))).capitalize()
        while True:
            phonenumber=int(input("Ingrese el numero del nuevo contacto  "))
            phonenumber_str=str(phonenumber)
            if len(phonenumber_str)>0 and len(phonenumber_str)<=8:
                break
            else:
                print("Numero de telefono no valido, intenten denuevo")
        email=str(input("Ingrese el el email del nuevo contacto  "))
        contacts.append({"contactname":name,"phonenumber":phonenumber,"email":email})
        return contacts
    def list_contact(self,contacts):
        if len(contacts)==0:
            print("La lista de contactos esta vacia\n")
        else:
            p=1
            print("Lista de contactos")
            for i in contacts:
                print(f"[{p}]."+(i["contactname"]))
                print("")
                p+=1
    def search_contact(self,contacts):
        found=False
        look_contact=(str(input("Ingrese el nombre de la persona que esta buscando  "))).capitalize()
        for i in range(len(contacts)):
            if contacts[i]["contactname"]==look_contact:
                contact_pos=i
                found=True
        if found:
            print("Se encontro al contacto"+(contacts[i]["contactname"])+" su informacion es: \nNumero: "+str(contacts[i]["phonenumber"])+"\nEmail: "+(contacts[i]["email"]))
        else:
            print("Lo sentimos no pudimos encontrar a la persona que busca")
    def edit_contact(self,contacts):
        print("¿Que contacto te gustaria modificar?")
        self.list_contact(contacts)
        look_contact=int(input(  ))
        while True:
            element=int(input("Que valor desea modificar:\n[1].Nombre\n[2].Numero\n[3].Email\n  "))
            if element==1:
                element="contactname"
            elif element==2:
                element="phonenumber"
            elif element==3:
                element="email"
            else:
                print("Numero no valido, intente denuevo")
                continue
            break
        new_value=input(f"Ingrese el nuevo valor que desea ingresar\n")
        contacts[look_contact-1][element]=new_value
        print("Operacion exitosa...")
        


