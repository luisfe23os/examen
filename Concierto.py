print("welcome a Music Day")
print("-- - - - -- - - - - - -")
print("1. Registrar grupo musical")
print("2. Mostrar bandas que no se han presentado")
print("3. Cambiar Hora de presentacion")
print("4. Retirar grupo musical")
print("5. Salir")
op=9
bandas=[]
id=0

while op != 5:
    grupo={}
    op = int(input("Digite una opcion"))
    if op == 1:
        id+=1
        print("registro de grupos ")
        grupo["id"]=id
        grupo["nombre"]=input("Digite nombre de banda ")
        grupo["genero"]=input("Digite genero musical ")
        grupo["hora"]=input("Digite hora de presentacion ")
        grupo["pago"]=float(input("valor pagado "))
        grupo["estado"]=input("1 -si ya se presento O 2- si no se ha presentado ")
        print(f"Se ha completado el registro su ID para la presentacion es -> {grupo['id']}")
        bandas.append(grupo)
        # prueba para ver que si se esten guardando los grupos
        print(bandas)
    elif op == 2:
        grupos_no_presentados = []  # Crear una lista para almacenar grupos no presentados
        for grupo in bandas:
            if grupo["estado"] == "2":
                grupos_no_presentados.append(grupo)  # Agregar el grupo a la lista
        if grupos_no_presentados:
            print("Grupos que no se han presentado:")
            for grupo in grupos_no_presentados:
                print(f"{grupo['id']}, {grupo['nombre']}")
        else:
            print("Aun no hay grupos que no se hayan presentado")
        
         

        # for grupo in bandas:
        #     if grupo["estado"] =="2":
        #         print("Grupos que no se han presentado ")
        #         print(f"{grupo['id']},{grupo['nombre']}")
        # else:
        #      print("aun no hay grupos que no se hayan presentado")

    elif op == 3:
        id_ba= int(input("ingrese el id del grupo que desea cambiar su hora de presentacion "))

        for grupo in bandas:
            if grupo["id"] == id_ba:
                 nhora=input("Ingrese la nueva hora de presentacion ")
                 grupo["hora"]=nhora
                 print("se ha actualizado la hora de presentacion")
                 print(f"{grupo['id']},{grupo['nombre']},{grupo['hora']}")
            else:
                print("no se ha encontrado una banda con el id ingresado")
    elif op == 4:
            print("En esta opcion vas a elimar un grupo musical de la presentacion")
            id_ba=int(input("Ingrese el id de la banda que desea retirar "))
            estado=False
        
            for grupo in bandas:
                if grupo["id"]==id_ba:
                    bandas.remove(grupo) 
                    estado=True 
                    print("se ha retirado la banda") 
                    
                else:
                    print("no se ha encontrado una banda con el id indicado")
    elif op==5:
        print("saliendo del programa...")
        
    else:
        print("opcion invalida")



