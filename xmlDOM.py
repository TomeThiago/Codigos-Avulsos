#importa a implementação minidom
import xml.dom.minidom

#Cria o documento
doc = xml.dom.minidom.Document()

#Para ler um documento que já existe
#doc = xml.dom.minidom.parse('caninos.xml')

#Cria elementos
root = doc.createElement('Canino')
lobo = doc.createElement('Lobo')
raposa = doc.createElement('Raposa')
coiote = doc.createElement('Coiote')
cachorro = doc.createElement('Cachorro')

#Cria atributos
cachorro.setAttribute('nome','Bandit')
cachorro.setAttribute('raca','Labrador')
cachorro.setAttribute('cor','Branco')

#Cria a estrutura
doc.appendChild(root)
root.appendChild(lobo)
root.appendChild(raposa)
lobo.appendChild(coiote)
lobo.appendChild(cachorro)

#Para acrescentar texto ao elemento
#tex = doc.createTextNode('Melhor amigo do homem...')
#cachorro.appendChild(tex)

#Mostra o XML formatado
print(doc.toprettyxml())