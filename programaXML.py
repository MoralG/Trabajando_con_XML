from lxml import etree
doc = etree.parse('parques.xml')

#------------------------ Definicion de variable ----------------------------

lista_municipios = []
lista_parques = []
lista_CIF = []
dic_par = {}
dic_datos = {}
dic_vistas = {}

#----------------------------- Lista Municipios -----------------------------------

lista_mun = doc.xpath("/result/elements/item/grup_adreca/municipi_nom/text()")   #Lista de todos los municipios incluidas las lineas con \n que no son municipios

for municipio in lista_mun:
            
    if municipio.startswith("\n") == False:   #quitamos las lineas con \n 
                
        lista_municipios.append(municipio)

#-------------------------------- Lista CIF ---------------------------------------

lista_cif = doc.xpath("/result/elements/item/rel_municipis/grup_ajuntament/cif/text()") 

#------------------------------ Lista punt_id --------------------------------------

lista_id = doc.xpath("/result/elements/item/punt_id/text()")

#------------------------- Funcion Vistas y parque ---------------------------------


def municipio_vista(municipio,doc):

    for vist in doc.xpath('/result/elements/item/grup_adreca[municipi_nom="%s"]/..'%municipio):

        vistas = vist.xpath('./rel_municipis/municipi_vista/text()')[0]
        parques = vist.xpath('./adreca_nom/text()')[0]
        
        dic_vistas[parques] = vistas

    return dic_vistas

#---------------------------- Funcion Datos Parque ----------------------------------

def datos_parque(cif,doc):

    for datos in doc.xpath('/result/elements/item/rel_municipis/grup_ajuntament[cif="%s"]/../..'%cif):

        nombre_parque = datos.xpath('./adreca_nom/text()')[0]
        descripcion = datos.xpath('./descripcio/text()')[0]
        direccion = datos.xpath('./grup_adreca/adreca_completa/text()')[0]
        municipio = datos.xpath('./grup_adreca/municipi_nom')[0].text = ('\n')

        dic_datos[nombre_parque] = [descripcion,direccion,municipio]
    
    return dic_datos

#---------------------------- Funcion coordenadas ------------------------------------

def coordenadas(id,doc):

    coord = doc.xpath('/result/elements/item[punt_id = "%s"]/localitzacio/text()'%id)[0]

    lista_coordenada = coord.split(",")

    return lista_coordenada

#--------------------------------- Programa ------------------------------------------

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
        print("Nº de parques:",lista_municipios.count(contar_municipios))   #Contamos los municipios iguales que hay en la lista, ya que por cada municipio es un parque
        print("---------------------------")
        print("")

    if condicion == 3:     #Opcion 3: Fotos de los parques por Municipios

        print("")
        nom_municipios = input("Introduce Municipio: ")   
        print("")    

        while nom_municipios not in lista_municipios:

            print("")
            print("--------------------------")
            print("ERROR, no existe Municipio")
            print("--------------------------")
            print("")

            nom_municipios = input("Introduce Municipio: ")
        
        print("----------------------------- Vista ---------------------------------")

        for mun,vista in municipio_vista(nom_municipios,doc).items():       #Hacemos que nos muestre municipio y vista

            print(mun,"=",vista )

        
        print("---------------------------------------------------------------------")

    if condicion == 4:      #Opcion 4: Mostrar datos del parque por CIF

       
        print("")
        cif = input("Introduce CIF: ")   
        print("")    

        while cif not in lista_cif:

            print("")
            print("--------------------------")
            print("ERROR, no existe CIF")
            print("--------------------------")
            print("")

            cif = input("Introduce CIF: ") 
        
        print(datos_parque(cif,doc))

    if condicion == 5:      #Opcion 5: Mostrar link del OpenStreetView

        print("")
        punt_id = input("Introduce el punto id: ")   
        print("")    

        while punt_id not in lista_id:

            print("")
            print("--------------------------")
            print("ERROR, no existe id")
            print("--------------------------")
            print("")

            punt_id = input("Introduce el punto id: ")
        
        zoom = input("Introduce el zoom: ")   

        print("Parque:",doc.xpath('/result/elements/item[punt_id = "%s"]/adreca_nom/text()'%punt_id)[0])
        print("https://www.openstreetmap.org/#map=%s/%s/%s" %(zoom,coordenadas(punt_id,doc)[0],coordenadas(punt_id,doc)[1]))


    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
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