from Motocicleta import Motocicleta
#variables
moto1 = Motocicleta ("Azul","123456",2,2,"Honda","CBR 600","101199",300,250)
moto2 = Motocicleta ("Negro","1234567",2,2,"Yamaha","R6 600","161299",118,185)

print("BIENVENIDO")
#menu para arrancar y detener las motos
while True:
    
    print("-----------------")
    print("MENÚ PRINCIPAL")
    print("Seleccione una opción")
    print("(1) Ver motocicleta 1")
    print("(2) Ver motocicleta 2")
    print("(3) CONSULTAR el precio desde la clase")
    print("(4) Salir")
    print("-----------------")
    print()
    option=int(input())
    if option==1:
        print("-----------------")
        print("Seleccionó: HONDA CBR 600")
        print("Qué desea hacer?")
        print("(1) ARRANCAR la motocicleta")
        print("(2) DETENER la motocicleta")
        print("(3) ACTUALIZAR el precio")
        print("(4) VOLVER al menú principal")
        print("-----------------")
        opmoto1=int(input())
        if opmoto1==1:
            moto1.arrancar()
            print("-----------------")
            print("Volviendo al menú")
            print("-----------------")
            print()
            continue
        elif opmoto1==2:
            moto1.detener()
            print("-----------------")
            print("Volviendo al menú")
            print("-----------------")
            print()
            continue
        elif opmoto1==3:
            print("Ingrese el nuevo precio: ")
            moto1.precio=input()
            print(f"Se ha actualizado el precio de la moto 1 : {moto1.marca} {moto1.modelo} : $ {moto1.precio} ")
            print()
        elif opmoto1==4:
            continue
        else:
            print("-----------------")
            print("OPCION INCORRECTA, intente nuevamente")  
            print()
            continue
    elif option==2:
        print("-----------------")
        print("Seleccionó: YAMAHA R6 600")
        print("Qué desea hacer?")
        print("(1) ARRANCAR la motocicleta")
        print("(2) DETENER la motocicleta")
        print("(3) ACTUALIZAR el precio")
        print("(4)Volver al menú principal")
        print("-----------------")
        print()
        opmoto2=int(input())
        if opmoto2==1:
            moto2.arrancar()
            print("-----------------")
            print("Volviendo al menú")
            print("-----------------")
            print()
            continue
        elif opmoto2==2:
            moto2.detener()
            print("-----------------")
            print("Volviendo al menú")
            print("-----------------")
            print()
            continue
        elif opmoto2==3:
            print("Ingrese el nuevo precio: ")
            moto2.precio=input()
            print(f"Se ha actualizado el precio de la moto 1 : {moto2.marca} {moto2.modelo} : $ {moto2.precio} ")
            print()
        elif opmoto2==4:
            continue
        else:
            print("-----------------")
            print("OPCION INCORRECTA, intente nuevamente") 
            print("-----------------")
            print() 
            continue
    elif option==3:
        print() 
        moto2.precio_desde_metodo()
        moto1.precio_desde_metodo()  
        print()
    elif option==4:
        break
    else:
        print("-----------------")
        print("OPCION INCORRECTA, intente nuevamente") 
        print("-----------------")
        print() 
        continue
        
    
# prueba atributo dinamico 
# moto1.precio=5000000   
# print("Se ha actualizado el precio de la moto 1 : {moto1.marca} {moto1.modelo} ")
# print (moto1.precio)