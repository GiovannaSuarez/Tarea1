# #--------------------------------------//Ejercicio en clase / variables dimensionadas//--------------------------------------

#--------------------------------------------/ EJERCICIO 1 /--------------------------------------------

# # Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente
# # forma: (nombre, dni, destino). Por ejemplo:
# # *(‘Manuel Juarez’, 12345678, ‘San Juan’), (‘Silvana Paredes’, 62258472, ‘Mendoza’)+

# # Además en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo:
# # *(‘Buenos Aires’, ‘Argentina’), (‘Lisboa’, ‘Portugal’), (‘Mendoza’, ‘Argentina’)+

# # Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
# # 1 - Agregar pasajeros a la lista de viajeros.
# # 2 - Agregar ciudades a la lista de ciudades.
# # 3 - Dado el DNI de un pasajero, ver a qué ciudad viaja.
# # 4 - Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
# # 5 - Dado el DNI de un pasajero, ver a qué país viaja.
# # 6 - Dado un país, mostrar cuántos pasajeros viajan a ese país.
# # 7 - Salir del programa.

print("BIENVENIDO A LA BASE DE DATOS DE VIAJE")
data_passenger = [("Giovanna Suarez",42307448,"Italia")]
city_country = [("Venecia","Italia")]


while True:
    print("Selecciones una opción:")
    print("(1) Agregar pasajero)")
    print("(2) Agregar ciudades)")
    print("(3) Consultar ciudad de destino de algun pasajero)")
    print("(4) Consultar cantidad de pasajeros por ciudad)")
    print("(5) Consultar país de destino de algun pasajero)")
    print("(6) Consultar cantidad de pasajeros por país")
    print("(7) SALIR DEL PROGRAMA")
    option=int(input())
    
    if option==1:
        print("Seleccionó : (1) Agregar pasajero)")
        while True:
                name = str(input("Nombre del pasajero: ")).capitalize()
                dni = int(input("Ingrese DNI: "))
                city_country = str(input("Ciudad destino: ")).capitalize()
                data_passenger.append((name,dni,city_country))
                print("¿Desea agregar otro pasajero? Seleccione (1) ")
                print("Para finalizar selecciones (2)")
                option = input()
                if option == 1:
                    continue 
                else: 
                    break 
        print() 
        continue        
             
    elif option==2:
            print("Seleccionó (2) Agregar ciudades")
            city=str(input("Ingrese el nombre de la ciudad: ")).capitalize()
            country=str(input("Ingrse el pais en donde se encuentra la ciudad: ")).capitalize()
            city_country.append((city,country))
            print("Ciudad agregada con éxito")
            print()
            continue
            

    elif option==3:
            print("Seleccionó (3) Consultar ciudad de destino de algun pasajero")
            validation=False
            compare_dni=int(input("Ingrese el numero de dni del pasajero: "))
            
            for i in data_passenger:
                if i[1] == compare_dni:
                    print(f"El pasajero con dni {compare_dni}, se dirije a {i[2]}")
                    validation=True
                if validation==False:
                    print(f"Lo sentimos, no encontramos ese dni resgistrado {compare_dni}")
            print()
            continue
            
            
    elif option==4:
        print("Seleccionó (4) Consultar cantidad de pasajeros por ciudad")
        cant_passenger=0
        city_count=str(input("Ingrese la ciudad y contare cuantos pasajeros desean viajar a ella: ")).capitalize()
        for i in data_passenger:
            if i[2]==city_count:
                cant_passsenger=cant_passenger+1
        print(f"La cantidad de personas que viajan a {city_count} es {cant_passenger}")
        print()
        continue
           
    elif option==5:
            print("Seleccionó (5) Consultar país de destino de algun pasajero)")
            search_dni=False
            compare_dni=int(input("Ingrese el dni que desea revisar  "))
            for i in data_passenger:
                if i[1]==compare_dni:
                    city_country=i[2]
                    name=i[0]
                    search_dni=True
            if search_dni==False:
                print(f"Lo sentimos no pudimos encontrar el pais de destino para {city_country}")
            else:
                for i in city_country:
                    if i[0]==look_city:
                        print(f"El pasajero {name} se dirije a {i[1]}")
            print()
            continue
            
        
    elif option==6:
            print("Sleccionó (6) Consultar cantidad de pasajeros por país")
            cant_passenger=0
            look_country=str(input("Ingrese el nombre de un pais y revisare cuantos pasajeros viajan a dicho pais: ")).capitalize()
            for i in city_country:
                look_city=""
                if i[1]==look_country:
                    look_city=i[0]
                for i in data_passenger:
                    if i[2]==look_city:
                        city_count_amount=cant_passenger+1
            print(f"La cantidad de personas que viajan a {look_country} es {cant_passenger} ")
            print()
            continue
            
            
    elif option==7:
            print("Gracias por usar el programa")
    break
    
    
        
#--------------------------------------------/ EJERCICIO 2 /--------------------------------------------
        
# #Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual
# #contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
# #(‘Nuria Costa’, 5, 1234.5,’Calle 1 – 456’), (‘Jorge Russo’, 7, 3999, ‘Calle 2 – 741’)+
# #Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y
# #retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente
# #puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que
# #contenga cada domicilio una sola vez.



def addresses(sales):
    addresses=set()
    for sale in sales:
        addresses.add(sale[3])
    return addresses

customers=[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
print("Lista de compras del mes de los clientes de una empresa:")
print(customers)
print("Domicilios a los cuales deben enviarse facturas de compra: ")
print(addresses(customers))

#--------------------------------------------/ EJERCICIO 3 /--------------------------------------------

#Crear un programa para gestionar datos de los socios de un club, permitiendo:
#- Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar
#son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). El programa debe iniciar
#con los datos de los socios fundadores ya cargados:
#o Socio n°1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
#o Socio n°2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
#o Socio n°3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
#- Informar cantidad de socios del club.
#- Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
#- Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad
#ingresaron el 14/03/2018.
#- Solicitar el nombre y apellido de un socio y darle de baja (eliminarlo del listado)
#- Imprimir el listado de socios completo.

#socios
partners = [{"number_s":"1","name":"Amanda Núñez","date_admission":"17032009","fee_paid":"aldia"},{"number_s":"2","name":"Bárbara Molina","date_admission":"17032009","fee_paid":"aldia"},{"number_s":"3","name":"Lautaro Campos","date_admission":"17032009","fee_paid":"aldia"}]

print ("BIENVENIDO AL SISTEMA DE SOCIOS DEL CLUB")
print()
print("Seleccione que acción desea realizar:")
print("(1) Cargar información de un socio nuevo")
print("(2) Ver cantidad total de socios")
print("(3) Actulizar estado de deuda de un socio") #registrar que ha pagado todas las cuotas
print("(4) Modificar fecha de ingreso de todos los socios")
print("(5) Dar de baja a un socio")
print("(6) Imprimir lista de todos los socios")
print("(7) Salir del programa")

option=int(input())

while True:
    if option==1:
        print("Seleccionó (1) Cargar información de un socio nuevo")
        validation=False
        while True:
            number_s_=str(input("Ingrese el número del nuevo socio: "))
            for i in range(len(partners)):
                partners_aux=partners[i]
                if number_s_==partners_aux["number_s"]:
                    validation=False
                    break
                else:
                    validation=True
            if validation==False:
                    print("ERROR - El numero ingresado ya corresponde a un miembro asociado, intente de nuevo")
            else:
                break        
       
        name_=str(input("Ingrese el Nombre y Apellido: "))
        date_admission_=str(input("Ingrese la fecha de ingreso con el siguiente formato: (ddmmaaaa) "))
        fee_paid_=int(input("Si el socio tiene la cuota al día, presione (1), en caso contrario, presione (2)"))
        if fee_paid_==1:
            fee_paid_=("aldia")
        else:
            fee_paid_=("adeudacuota")  
        partners.append({"number_s":number_s_,"name":name_,"date_admission":date_admission_,"fee_paid":fee_paid_}) 
        print("Usuario agregado correctamente")   
    
    elif option==2:
        print("Seleccionó (2) Ver cantidad total de socios")
        cant_partners=1
        for i in range(len(partners)):
            cant_partners=cant_partners+1   
        print(f"En este momento, el club tiene un total de : {cant_partners} socios")
        break
    
    elif option==3:
        print("Seleccionó (3) Actulizar estado de deuda de un socio")
        compare_fee_paid=(input("Ingrese el número de socio para registrar que tiene la cuota al día: "))
        validation_=False
        for i in range(len(partners)):
            aux=partners[i]
            if compare_fee_paid==aux["number_s"]:
                partners_aux=i
                validation_=True
        if validation_==False:
            print("ERROR - Número de socio no encontrado, intente nuevamente")    
        else:
            (partners[partners_aux])["fee_paid"]="aldia"
            print("INFORMACIÓN ACTUALIZADA - El usuario se encuentra al día con las cuotas")       
        
    elif option==4: 
        print("Seleccionó (4) Modificar fecha de ingreso de todos los socios")
        for i in range(len(partners)):
            (partners[i])["date_admission"]="13/03/2018"
        print("INFORMACIÓN ACTUALIZADA")   
        break
        
    elif option==5:
        print("Seleccionó (5) Dar de baja a un socio")
        unsubscribe=int(input("Ingrese el número del socio que quiere dar de baja: "))
        for i in range(len(partners)):
            auxdel=partners[i]
            if auxdel["number_s"]==unsubscribe:        
                del partners[i]
        print("OPERACIÓN COMPLETADA CON EXITO - El socio ha sido dado de baja")
        break
    elif option==6:
        print("Seleccionó (6) Imprimir lista de todos los socios")
        for i in range(len(partners)):
            print("-------------------------------------")
            print(f"Socio número {i} : ")
            print (partners)
        break
    elif option==7:
        print("SALIENDO DEL SISTEMA")
        break         
                


        

           
           
        
            



