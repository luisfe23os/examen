print("Frutas pipe")
print("- - - - - - - - ")
print("1.digitar las frutas ")
print("2. fruta orden")
print("3. fruta mas barata")

canastas=[]
opcion=9
id=0

opcion = int(input("ingrese un numero "))
while opcion !=9:
    if opcion==1:
        op=int(input("ingrese el numero de frutas que desea"))
   
        for f in range(op):
            fruta={}
            id+=1
            fruta["id"]=id
            fruta["sele"]=input("digite la fruta")
            fruta["precio"]=float(input("valor de la fruta"))
            fruta["cantidad"]=int(input("cantidad de frutas"))
            canastas.append(fruta)
        print(canastas)
    if opcion==2:
        pass
    opcion = int(input("Ingrese un número (9 para salir): "))
    print("Saliendo del programa...")