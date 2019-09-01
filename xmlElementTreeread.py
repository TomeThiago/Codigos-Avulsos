from xml.etree.ElementTree import ElementTree

tree = ElementTree(file='caninos.xml')
root = tree.getroot()

#Lista os elementos abaixo do root
print(root.getchildren())

#Encontra o lobo
lobo = root.find('Lobo')

#Encontra o cachorro
cachorro = lobo.find('Cachorro')
print(cachorro.tag, cachorro.attrib)

#Remove a raposa
root.remove(root.find('Raposa'))
print(root.getchildren())