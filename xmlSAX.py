#SAX só permite leitura serial do documento XML. 
# Consome menos memoria que o DOM, porém menos recurso

import xml.sax

#A classe processa a árvore XML
class Handler(xml.sax.handler.ContentHandler):
	def __init__(self):
		xml.sax.handler.ContentHandler.__init__(self)
		self.prefixo = ''
	#É chamado quando uma novo tag é encontrada
	def startElement(self, tag, attr):
		self.prefixo += ' '
		print(self.prefixo + 'Elemento:', tag)
		for item in attr.items():
			print(self.prefixo + '- %s: %s' % item)

	#É chamado quando o texto é encontrado
	def characters(self, txt):
		if txt.strip():
			print(self.prefixo + 'txt:', txt)
	#É chamado quando o fim de uma tag é encontrado
	def end(self, name):
		self.prefixo = self.prefixo[:-2]

parser = xml.sax.make_parser()
parser.setContentHandler(Handler())
parser.parse('caninos.xml')