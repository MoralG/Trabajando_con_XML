from lxml import etree
doc = etree.parse('parques.xml')

print(doc.xpath("//nom/text()"))