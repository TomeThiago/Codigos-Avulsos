import sys
from PyQt5 import QtGui, QtCore

class Main(QtGui.QWidget):
    """
	Janela Principal
	"""
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		#Muda a geometria da janela
		self.setGeometry(200,200,200,100)

		#Muda o titulo
		self.windowTitle('Teste')

		#Cria um botão
		quit = QtGui.QPushButton('Fechar', self)
		quit.setGeometry(10,10,60,35)

		#Conecta o sinal gerado pelo botão com a função
		#que encerra o programa
		self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))

#Cria um objeto "aplicação Qt", que trata os eventos
app = QtGui.QGuiApplication(sys.argv)
#Cria a janela principal
qb = Main()
qb.show()

#Inicia a "aplicação Qt"
sys.exit(app.exec_())