#MENÚ DE 4 COMIDAS. SE ELIGE UNA OPCIÓN Y SE ARROJA PRECIO. (pizza, panchitooo y hamburguesa con papas)

print("¡Bienvenido al food truck Dinamita!")
print("¿Qué quiere comer hoy?")
bill = 0

while True:
    print("[1]. Hamburguesa")
    print("[2]. Pancho")
    print("[3]. Pizza")
    print("[4]. Terminar pedido")
    option = input("Elija una opción del menu: ")
    
    if len(option)==1 and (option=="1" or option=="2" or option=="3" or option=="4"):
        option = int(option)
        
        #--------------------------------------------------
        if option==1:
            print("¿Desea acompañar su hamburguesa?")
            print("[1]. Con Papas chicas ($1700)")
            print("[2]. Con Papas grandes ($2000)")
            print("[3]. Sin papas ($1200)")
            print("[4]. Volver al menú principal")
            option_burger = input(">>> ")
            if len(option_burger)==1 and (option_burger=="1" or option_burger=="2" or option_burger=="3" or option_burger=="4"):
                option_burger = int(option_burger)
                if option_burger==1:
                    bill = bill + 1700
                    print(f"Su pedido es: Hamburguesa con Papas chicas. Total del pedido: ${bill}")
                    print("¿Desea agregar algo más?")
                    option = 0
                elif option_burger==2:
                    bill = bill + 2000
                    print(f"Su pedido es: Hamburguesa con Papas grandes. Total del pedido: ${bill}")
                    print("¿Desea agregar algo más?")
                    option = 0
                elif option_burger==3:
                    bill = bill + 1200
                    print (f"Su pedido es: Hamburguesa. Total del pedido: ${bill}")
                    print("¿Desea agregar algo más?")
                    option = 0
                elif option_burger==4:
                    option = 0
            else:
                print("ERROR, elija una opción válida.")
                option = 0
        
        #--------------------------------------------------
        elif option==2:
            print("¿Desea acompañar su pancho?")
            print("[1]. Aderezos completo")
            print("[2]. Sin aderezos")
            print("[3]. Volver al menú principal")
            option_hotdog = input(">>> ")
            if len(option_hotdog)==1 and (option_hotdog=="1" or option_hotdog=="2" or option_hotdog=="3"):
                option_hotdog = int(option_hotdog)
                if option_hotdog==1:
                    bill = bill + 1200
                    print(f"Su pedido es: Pancho Con Aderezos. Total del pedido: ${bill}")
                    print("¿Desea agregar algo más?")
                elif option_hotdog==2:
                    bill = bill + 1000
                    print(f"Su pedido es: Pancho Sin Aderezo. Total del pedido: ${bill}")
                    print("¿Desea agregar algo más?")
                elif option_hotdog==3:
                    option = 0
            else:
                print("ERROR, elija una opción válida.")
                option = 0
                
        #--------------------------------------------------        
        elif option==3:
            print("¿Que pizza desea?")
            print("[1]. Muzza")
            print("[2]. Especial")
            print("[3]. Volver al menú principal")
            option_pizza = input(">>> ")
            if len(option_pizza)==1 and (option_pizza=="1" or option_pizza=="2" or option_pizza=="3"):
                option_pizza = int(option_pizza)
                if option_pizza==1:
                    bill = bill + 2000
                    print(f"Su pedido es: Pizza Muzza. Total del pedido: ${bill}")
                    print("¿Desea agregar algo más?")
                elif option_pizza==2:
                    bill = bill + 2500
                    print(f"Su pedido es: Pizza Especial. Total del pedido: ${bill}")
                    print("¿Desea agregar algo más?")
                elif option_pizza==3:
                    option = 0
            else:
                print("ERROR, elija una opción válida.")
                option = 0

        #--------------------------------------------------
        elif option==4:
            break
        elif option==0:
            continue
    else:
        print("ERROR, ingrese una opción válida.")
        continue
print(f"El total de su pedido es de: ${bill}")
print("Gracias por elegirnos")
#fin