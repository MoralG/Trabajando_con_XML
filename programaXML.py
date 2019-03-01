from lxml import etree
doc = etree.parse('parques.xml')

#------------------------ Definicion de variable ----------------------------

lista_municipios = []
lista_parques = []
dic_par = {}

#----------------------------- Municipios -----------------------------------

lista_mun = doc.xpath("/result/elements/item/grup_adreca/municipi_nom/text()")   #Lista de todos los municipios incluidas las lineas con \n que no son municipios

for municipio in lista_mun:
            
    if municipio.startswith("\n") == False:   #quitamos las lineas con \n 
                
        lista_municipios.append(municipio)

#----------------------------------------------------------------------------


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

        for municipio in sorted(set(lista_municipios)):   #quitamos los municipios duplicados y lo ordenamos

            print(municipio)

    if condicion == 2:     #Opcion 2: Contar los parques por Municipios

        contar_municipios = input("Introduce Municipio: ")

        while contar_municipios not in lista_municipios:

            print("")
            print("--------------------------")
            print("ERROR, no existe Municipio")
            print("--------------------------")
            print("")

            contar_municipios = input("Introduce Municipio: ")
        
        print("")
        print("---------------------------")
        print("Municipio:",contar_municipios)
        print("Nº de parques:",lista_municipios.count(contar_municipios))
        print("---------------------------")
        print("")





            #lista_par = doc.xpath("/result/elements/item/adreca_nom/text()")
            #
            #for parque in lista_par:
            #
            #    if parque.startswith("\n") == False:   #quitamos las lineas con \n 
            #    
            #        lista_parques.append(parque)
            #
            #for municipio in  
            
            

           # dic_par[doc.xpath("/result/elements/item/grup_adreca/municipi_nom/text()")]=

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