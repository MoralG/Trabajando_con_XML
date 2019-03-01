from lxml import etree
doc = etree.parse('parques.xml')

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

while condicion != 0:

    if condicion == 1:

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
    
#print(doc.xpath())