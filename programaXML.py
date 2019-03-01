from lxml import etree
doc = etree.parse('parques.xml')

lista_municipios = []

print("")
print("-------------------MENU--------------------")
print("(1) Mostrar todos los Municipios")
print("(2) Contar parques por Municipios")
print("(3) Fotos de los parques por Municipios")
print("(4) Datos del parque por CIF")
print("(5) Link de OpenStreetMap")
print("(0) Finalizar el programa")
print("-------------------------------------------")
print("")

condicion = int(input("¿Que opcion eliges?   "))
print("")

while condicion != 0:

    if condicion == 1:    #Opcion 1: mostrar municipios

        lista_mun = doc.xpath("/result/elements/item/grup_adreca/municipi_nom/text()")   #Lista de todos los municipios incluidas las lineas con \n que no son municipios

        for municipio in lista_mun:
            
            if municipio.startswith("\n") == False:   #quitamos las lineas con \n 
                
                lista_municipios.append(municipio)

        for municipio in sorted(set(lista_municipios)):   #quitamos los municipios duplicados y lo ordenamos

            print(municipio)


    print("")
    print("-------------------MENU--------------------")
    print("(1) Mostrar todos los Municipios")
    print("(2) Contar parques por Municipios")
    print("(3) Fotos de los parques por Municipios")
    print("(4) Datos del parque por CIF")
    print("(5) Link de OpenStreetMap")
    print("(0) Finalizar el programa")
    print("-------------------------------------------")
    print("")
    
    condicion = int(input("¿Que opcion eliges?   "))
    print("")

#print(doc.xpath())